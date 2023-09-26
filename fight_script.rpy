label move_attack(fight, target, attacker, move, move_damage):
    $ fight.stats[attacker]["damage_dealt"] += move_damage
    $ fight.stats[target]["damage_blocked"] += max(move_damage - target.current_guard, 0)

    if move_damage > target.current_guard and target.current_guard <= 0 and not attacker.stance_bonus == "Jab":
        $ fight.stats[attacker]["guards_broken"] += 1

        # Quirk: Backlash
        if isinstance(target.quirk, Backlash):
            $ attacker.current_health -= 3

    if target.current_guard < move_damage or attacker.stance_bonus == "Jab":
        scene expression move.images["hit_image"]
        with vpunch

        $ target.current_health -= (damage - target.current_guard)
        $ target.current_guard = 0

    else:
        scene expression move.images["blocked_image"]
        with vpunch

        $ target.current_guard -= move.damage

    pause 1.0

    return


label fight_start_turn(fight, target, attacker):
    hide screen phone_icon

    scene black

    if attacker == fight.player:
        show text "{size=100}Your Turn{/size}"
    else:
        show text "{size=100}Opponent's turn{/size}"

    pause 1.0

    $ overwhelmed_multiplier = 1

    if attacker == fight.opponent:
        # Overwhelmed
        if len(fight.move_list[-1][target]) >= 4:
            if attacker.current_health / float(attacker.max_health) <= 0.25:
                $ overwhelmed_multiplier = 1.9
            elif 0.25 < attacker.current_health / float(attacker.max_health) <= 0.5:
                $ overwhelmed_multiplier = 1.6
            else:
                $ overwhelmed_multiplier = 1.3

    $ attacker.current_guard = round(attacker.stance.value * overwhelmed_multiplier)

    if isinstance(target.stance_bonus, Hook):
        $ attacker.current_stamina -= 2

    $ fight.move_list.append({attacker: []})

    if attacker == fight.player:
        call screen fight_player_turn(fight, attacker, target)
    else:
        call fight_attack_turn(fight, target, attacker) from _call_fight_attack_turn


label fight_attack_turn(fight, target, attacker, move=None):
    $ renpy.set_return_stack([])

    show screen health_bars(fight.player, fight.opponent)

    if move is None:
        if attacker.special_attack is not None and attacker.special_attack.is_sensitive(fight, target, attacker) and attacker.current_stamina >= attacker.special_attack.stamina_cost:
            $ move = attacker.special_attack
        elif any(move.ideal_stance == attacker.stance and move.stamina_cost <= attacker.current_stamina for move in attacker.base_attacks):
            $ move = renpy.random.choice(list(filter(lambda move: move.ideal_stance == attacker.stance and move.stamina_cost <= attacker.current_stamina, attacker.base_attacks)))
        else:
            $ move = renpy.random.choice(list(filter(lambda move: move.stamina_cost <= attacker.current_stamina, attacker.base_attacks + attacker.turn_moves)))

    if not fight.move_list:
        $ fight.move_list.append({attacker: []})

    $ fight.move_list[-1][attacker].append(move)

    if move == end_turn or isinstance(move, EndTurn):
        $ attacker.current_stamina = attacker.max_stamina + min(attacker.current_stamina, 2)
        $ attacker.current_guard = attacker.stance.value
        call fight_start_turn(fight, attacker, target) from _call_fight_start_turn

    elif move == turtle or isinstance(move, Turtle):
        $ attacker.current_guard = FightStance.DEFENSIVE.value

        # Stance Bonus
        if attacker.stance == FightStance.SOLID:
            $ attacker.current_guard += 1

        call fight_start_turn(fight, attacker, target) from _call_fight_start_turn_1

    if hasattr(move, "images") and not move.images:
        $ raise NotImplementedError("Move {} is missing images.".format(move.name))

    $ attacker.current_stamina -= move.stamina_cost

    scene expression move.images["start_image"]
    pause 1.0

        # Player attacks
        # Opponent Approachs
    $ primed_multiplier = FightService.get_primed_multiplier(target, fight, move) 

    $ reckless_multiplier = FightService.get_reckless_multiplier(target, fight)

    if attacker == fight.player: 
        # Calculating
        $ attacker.current_health -= round(move.damage * FightService.get_calculating_multiplier(target, fight))

    # Stance Bonus
    $ stance_multiplier = FightService.get_stance_multiplier(target, fight)

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
    if isinstance(attacker.quirk, SeeingRed) and not fight.move_list[-1][attacker]:
        $ damage *= 2

    call move_attack(fight, target, attacker, move, damage) from _call_move_attack

    if target.current_health <= 0:
        hide screen health_bars
        show screen phone_icon
        jump expression fight.end_label

    # Set end stance
    if move.end_stance is not None:
        $ attacker.stance = move.end_stance

    if attacker.current_stamina > 0:
        if attacker == fight.player:
            call screen fight_player_turn(fight, fight.player, fight.opponent)
        else:
            call fight_attack_turn(fight, target, attacker) from _call_fight_attack_turn_1

    else:
        # Seeing Red quirk
        if isinstance(attacker.quirk, SeeingRed) and attacker.stance == FightStance.AGGRESSIVE:
            $ attacker.current_guard = 0
        else:
            $ attacker.current_guard = attacker.stance.value
        $ attacker.current_stamina = attacker.max_stamina
        call fight_start_turn(fight, attacker, target) from _call_fight_start_turn_2
