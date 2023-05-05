label move_attack(fight, target, attacker, move, move_damage):
    $ fight.stats[attacker.name]["damage_dealt"] += move_damage
    $ fight.stats[target.name]["damage_blocked"] += max(move_damage - target.guard, 0)

    if move_damage > target.guard and target.guard <= 0 and not attacker.stance_bonus == "Jab":
        $ fight.stats[attacker.name]["guards_broken"] += 1

        # Quirk: Backlash
        if isinstance(target.quirk, Backlash):
            $ attacker.health -= 3

    if target.guard < move_damage or attacker.stance_bonus == "Jab":
        scene expression move.images["hit_image"]
        with vpunch

        $ target.health -= (damage - target.guard)
        $ target.guard = 0

    else:
        scene expression move.images["blocked_image"]
        with vpunch

        $ target.guard -= move.damage

    pause 1.0

    return


label fight_start_turn(fight, target, attacker):
    hide screen phone_icon

    scene black

    if attacker == fight.player.fighter:
        show text "{size=100}Your Turn{/size}"
    else:
        show text "{size=100}Opponent's turn{/size}"

    pause 1.0

    $ overwhelmed_multiplier = 1

    if attacker == fight.opponent.fighter:
        # Overwhelmed
        if len(fight.move_list[-1][target.name]) >= 4:
            if attacker.health / float(attacker.max_health) <= 0.25:
                $ overwhelmed_multiplier = 1.9
            elif 0.25 < attacker.health / float(attacker.max_health) <= 0.5:
                $ overwhelmed_multiplier = 1.6
            else:
                $ overwhelmed_multiplier = 1.3

    $ attacker.guard = round(attacker.stance.value * overwhelmed_multiplier)

    if isinstance(target.stance_bonus, Hook):
        $ attacker.stamina -= 2

    $ fight.move_list.append({attacker.name: []})

    if attacker == fight.player.fighter:
        call screen fight_player_turn(fight, attacker, target)
    else:
        call fight_attack_turn(fight, target, attacker) from _call_fight_attack_turn


label fight_attack_turn(fight, target, attacker, move=None):
    $ renpy.set_return_stack([])

    show screen health_bars(fight.player, fight.opponent)

    if move is None:
        if attacker.special_attack is not None and attacker.special_attack.is_sensitive(fight, target, attacker) and attacker.stamina >= attacker.special_attack.stamina_cost:
            $ move = attacker.special_attack
        elif any(move.ideal_stance == attacker.stance and move.stamina_cost <= attacker.stamina for move in attacker.base_attacks):
            $ move = renpy.random.choice(list(filter(lambda move: move.ideal_stance == attacker.stance and move.stamina_cost <= attacker.stamina, attacker.base_attacks)))
        else:
            $ move = renpy.random.choice(list(filter(lambda move: move.stamina_cost <= attacker.stamina, attacker.base_attacks + attacker.turn_moves)))

    $ fight.move_list[-1][attacker.name].append(move)

    if move == end_turn or isinstance(move, EndTurn):
        $ attacker.stamina = attacker.max_stamina + min(attacker.stamina, 2)
        $ attacker.guard = attacker.stance.value
        call fight_start_turn(fight, attacker, target) from _call_fight_start_turn

    elif move == turtle or isinstance(move, Turtle):
        $ attacker.guard = FightStance.DEFENSIVE.value

        # Stance Bonus
        if attacker.stance == FightStance.SOLID:
            $ attacker.guard += 1

        call fight_start_turn(fight, attacker, target) from _call_fight_start_turn_1

    if hasattr(move, "images") and not move.images:
        $ raise NotImplementedError("Move {} is missing images.".format(move.name))

    $ attacker.stamina -= move.stamina_cost

    scene expression move.images["start_image"]
    pause 1.0

        # Player attacks
        # Opponent Approachs
    $ primed_multiplier = target.get_primed_multiplier(fight, move) 

    $ reckless_multiplier = target.get_reckless_multiplier(fight)

    if attacker == fight.player.fighter: 
        # Calculating
        $ attacker.health -= round(move.damage * target.get_calculating_multiplier(fight))

    # Stance Bonus
    $ stance_multiplier = target.get_stance_multiplier(fight)

    # Quirk: The Great Equalizer
    $ the_great_equalizer_multiplier = attacker.quirk.effect(attacker, target, move) if isinstance(attacker.quirk, TheGreatEqualizer) else 1.0

    # Quirk: In The Zone
    $ in_the_zone_multiplier = attacker.quirk.effect(attacker, target, move) if isinstance(attacker.quirk, InTheZone) else 1.0

    # Quirk: Double Time
    $ double_time_multiplier = 2.0 if isinstance(attacker.quirk, DoubleTime) or isinstance(target.quirk, DoubleTime) else 1.0

    # Quirk: All In
    $ all_in_multiplier = 2.0 if isinstance(attacker.quirk, DoubleTime) or isinstance(target.quirk, DoubleTime) else 1.0

    $ damage = round(move.damage * primed_multiplier * reckless_multiplier * stance_multiplier * the_great_equalizer_multiplier * in_the_zone_multiplier * double_time_multiplier * all_in_multiplier)

    # Seeing Red quirk
    if isinstance(attacker.quirk, SeeingRed) and not fight.move_list[-1][attacker.name]:
        $ damage *= 2

    call move_attack(fight, target, attacker, move, damage) from _call_move_attack

    if target.health <= 0:
        hide screen health_bars
        show screen phone_icon
        jump expression fight.end_label

    # Set end stance
    if move.end_stance is not None:
        $ attacker.stance = move.end_stance

    if attacker.stamina > 0:
        if attacker == fight.player.fighter:
            call screen fight_player_turn(fight, fight.player.fighter, fight.opponent.fighter)
        else:
            call fight_attack_turn(fight, target, attacker) from _call_fight_attack_turn_1

    else:
        # Seeing Red quirk
        if isinstance(attacker.quirk, SeeingRed) and attacker.stance == FightStance.AGGRESSIVE:
            $ attacker.guard = 0
        else:
            $ attacker.guard = attacker.stance.value
        $ attacker.stamina = attacker.max_stamina
        call fight_start_turn(fight, attacker, target) from _call_fight_start_turn_2
