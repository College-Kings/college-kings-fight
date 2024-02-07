screen fight_overview(fight, title):
    modal True
    style_prefix "fight_overview"

    default difficulties = ("Easy", "Normal", "Hard", "Oscar")
    default difficulty_index = 1
    default hovering_opponent = False

    python:
        player = fight.player
        opponent = fight.opponent

    add "fight_background"

    text title style "fight_overview_title" xalign 0.5 ypos 50

    # Player info
    hbox:
        align (0.5, 0.5)
        spacing 100

        for competitor in (fight.player, fight.opponent):
            frame:
                xysize (898, 771)
                background "fight_frame_background"

                hbox:
                    xpos 55
                    spacing 10

                    add Transform(competitor.character.profile_picture, xysize=(80, 80)) yalign 0.5

                frame:
                    xysize (810, 682)
                    pos (44, 41)
                    padding (10, 10)

                    hbox:
                        xalign 0.5
                        ypos 45
                        spacing 2

                        for i in range(int(competitor.max_health)):
                            add Transform("#f00", size=((750/competitor.max_health) - 2, 20))

                    vbox:
                        align (0.5, 0.5)
                        spacing 25

                        hbox:
                            spacing 50

                            text "BASIC ATTACKS" yalign 0.5

                            grid 2 2:
                                spacing 10

                                for attack in competitor.base_attacks:
                                    button:
                                        background "fight_attack_idle"
                                        hovered SetScreenVariable("hovering_opponent", competitor != fight.player)
                                        tooltip attack.description
                                        action NullAction()
                                        xysize (206, 58)
                                        padding (5, 5)

                                        text attack.name align (0.5, 0.5)

                        hbox:
                            spacing 35

                            text "SPECIAL ATTACK" yalign 0.5

                            vpgrid:
                                cols 2
                                spacing 10
                                allow_underfull True

                                for attack in competitor.special_attacks:
                                    button:
                                        background "fight_attack_idle2"
                                        selected_background "fight_attack_hover"
                                        selected (competitor.special_attack == attack)
                                        xysize (206, 58)
                                        padding (5, 5)
                                        hovered SetScreenVariable("hovering_opponent", competitor != fight.player)
                                        tooltip attack.effect
                                        if competitor == fight.player:
                                            hover_background "fight_attack_hover"
                                            action SetField(competitor, "special_attack", attack)
                                        else:
                                            action NullAction()

                                        text attack.name align (0.5, 0.5)

                        hbox:
                            spacing 25

                            text "QUIRK" yalign 0.5

                            grid 3 2:
                                spacing 10

                                for quirk in fight_quirks:
                                    button:
                                        idle_background "fight_attack_idle2"
                                        selected_background "fight_attack_hover"
                                        insensitive_background "fight_attack_insensitive"
                                        selected (competitor.quirk == quirk)
                                        xysize (206, 58)
                                        padding (5, 5)
                                        hovered SetScreenVariable("hovering_opponent", competitor != fight.player)
                                        tooltip quirk.description
                                        if competitor == fight.player:
                                            hover_background "fight_attack_hover"
                                            action SetField(competitor, "quirk", quirk)
                                        elif competitor.quirk == quirk:
                                            action NullAction()

                                        text quirk.name align (0.5, 0.5)
                frame:
                    xysize (190, 50)
                    xpos 612
                    padding (10, 10)

                    text "COMPETITOR" size 16 align (0.5, 0.5)

    $ tooltip = GetTooltip()

    if not hovering_opponent:
        fixed:
            pos (65, 767)
            xysize (791, 100)

            if tooltip:
                text "[tooltip]" align (0.5, 0.5)

    else:
        fixed:
            pos (1064, 767)
            xysize (791, 100)

            if tooltip:
                text "[tooltip]" align (0.5, 0.5)

    hbox:
        xpos 100
        yalign 1.0
        yoffset -100
        spacing 20

        text "DIFFICULTY:"

        imagebutton:
            idle "left_arrow"
            if difficulty_index > 0:
                action [SetScreenVariable("difficulty_index", difficulty_index - 1),
                    SetField(opponent, "max_health", opponent.max_health * 1/1.25),
                    SetField(opponent, "attack_multiplier", opponent.attack_multiplier - 0.5),
                    SetField(opponent, "max_stamina", opponent.max_stamina * 1/1.25)]
            yalign 0.5

        frame:
            xsize 100
            yalign 0.5

            text difficulties[difficulty_index] xalign 0.5

        imagebutton:
            idle "right_arrow"
            if difficulty_index < len(difficulties) - 1:
                action [SetScreenVariable("difficulty_index", difficulty_index + 1),
                    SetField(opponent, "max_health", opponent.max_health * 1.25),
                    SetField(opponent, "attack_multiplier", opponent.attack_multiplier + 0.5),
                    SetField(opponent, "max_stamina", opponent.max_stamina * 1.25)]
            yalign 0.5

    hbox:
        align (0.5, 1.0)
        yoffset -25
        spacing 20

        imagebutton:
            idle "fight_play_fight_idle"
            hover "fight_play_fight_hover"
            insensitive "fight_play_fight_insensitive"
            sensitive (player.special_attack is not None and player.quirk is not None)
            action [Function(FightService.start_fight, fight), Call("fight_start_turn", fight, opponent, player)]
            yalign 0.5

        imagebutton:
            idle "fight_skip_fight_idle"
            hover "fight_skip_fight_hover"
            insensitive "fight_skip_fight_insensitive"
            sensitive (player.special_attack is not None and player.quirk is not None)
            action [SetField(opponent, "max_health", int(opponent.max_health)),
                SetField(opponent, "max_stamina", int(opponent.max_stamina)),
                Jump(fight.end_label)]
            yalign 0.5

    if not (persistent.enabled_tutorials["fight_preparation_tutorial"] and persistent.enabled_tutorials["fight_tutorial"]):
        textbutton "SHOW ALL FIGHT TUTORIALS":
            align (1.0, 1.0)
            offset (-100, -100)
            text_font "fonts/Montserrat-Bold.ttf"
            text_size 20
            action [SetDict(persistent.enabled_tutorials, "fight_preparation_tutorial", True), SetDict(persistent.enabled_tutorials, "fight_tutorial", True), Show("fight_preparation_tutorial")]

    if config_debug and competitor == fight.player:
        $ attack = renpy.random.choice(competitor.special_attacks)
        $ quirk = renpy.random.choice(fight_quirks)

        timer 0.1 action [
            SetField(competitor, "special_attack", attack),
            SetField(competitor, "quirk", quirk),
            SetField(opponent, "max_health", int(opponent.max_health)),
            SetField(opponent, "max_stamina", int(opponent.max_stamina)),
            Call("fight_start_turn", fight, opponent, player)
        ]

    if persistent.enabled_tutorials["fight_preparation_tutorial"]:
        on "show" action Show("fight_preparation_tutorial")


screen fight_player_turn(fight, player, opponent):
    tag fight_screen
    style_prefix "fight_turn"

    default selected_move = None
    default player_max_stamina = max(player.current_stamina, player.max_stamina)

    add opponent.stance_image

    use health_bars(fight.player, fight.opponent, selected_move)

    frame:
        background "fight_stance"
        xalign 0.5
        ypos 50
        xysize (568, 63)
        style_prefix "fight_turn_stance"

        hbox:
            align (0.5, 0.5)

            for i in FightStance:
                frame:
                    align (0.5, 0.5)

                    if i == player.stance:
                        xysize (164, 81)

                        add "fight_stance_current"

                        vbox:
                            align (0.5, 0.5)

                            text "CURRENT STANCE" size 14 xalign 0.5
                            text i.name xalign 0.5

                    elif selected_move is not None and i == selected_move.ideal_stance:
                        xysize (135, 63)

                        add "fight_stance_ideal"

                        vbox:
                            align (0.5, 0.5)

                            text "IDEAL STANCE" size 14 xalign 0.5
                            text i.name xalign 0.5

                    elif selected_move is not None and i == selected_move.end_stance:
                        xysize (135, 63)

                        add "fight_stance_end"

                        vbox:
                            align (0.5, 0.5)

                            text "END STANCE" size 14 xalign 0.5
                            text i.name xalign 0.5

                    else:
                        xysize (135, 63)

                        text i.name align (0.5, 0.5)

    hbox:
        xalign 0.5
        yalign 1.0
        yoffset -50
        spacing -17

        for move in player.base_attacks + [player.special_attack] + player.turn_moves:
            button:
                if move.ideal_stance == player.stance:
                    idle_background "fight_actions_ideal_idle"
                    hover_background "fight_actions_ideal_hover"
                    selected_background "fight_actions_ideal_hover"
                else:
                    idle_background "fight_actions_idle"
                    hover_background "fight_actions_hover"
                    selected_background "fight_actions_hover"
                insensitive_background "fight_actions_insensitive"
                sensitive (player.current_stamina >= move.stamina_cost)
                selected (selected_move == move)
                if selected_move == move:
                    action [SetScreenVariable("selected_move", None), Hide("action_info")]
                else:
                    action [SetScreenVariable("selected_move", move), Show("action_info", None, fight, player, opponent, move)]
                xysize (234, 172)
                padding (45, 45)

                vbox:
                    align (0.5, 0.5)
                    spacing 5

                    text move.name xalign 0.5

                    hbox:
                        xalign 0.5
                        spacing 5

                        for i in range(1, player.max_stamina + 1):
                            if i > move.stamina_cost:
                                add "fight_action_stamina_empty"
                            else:
                                add "fight_action_stamina_filled"

    vbox:
        xpos 50
        yalign 1.0
        yoffset -20
        spacing 5

        text "STAMINA" size 15

        hbox:
            spacing 5

            for i in range(1, player_max_stamina + 1):
                if i > player.current_stamina:
                    add "fight_stamina_empty"
                else:
                    add "fight_stamina_filled"

    if config_debug:
        $ move = random.choice(player.base_attacks + player.turn_moves)
        timer 0.1 action [Function(FightService.set_stance_bonus, player, move), Call("fight_attack_turn", fight, opponent, player, move)]

    if persistent.enabled_tutorials["fight_tutorial"]:
        on "show" action Show("fight_tutorial")

style fight_turn_text is text:
    size 26
    color "#fff"
    font "fonts/Montserrat-Regular.ttf"
    text_align 0.5

style fight_turn_stance_text is text:
    size 24
    color "#fff"
    font "fonts/BebasNeue-Regular.ttf"
    text_align 0.5


screen health_bars(player, opponent, move=None):
    default bar_size = 550.0
    default guard_segment_size = (bar_size - FightService.MAX_GUARD) / FightService.MAX_GUARD
    default opponent_health_segment_size = (bar_size - opponent.max_health) / opponent.max_health
    default player_health_segment_size = (bar_size - player.max_health) / player.max_health

    hbox:
        xalign 1.0
        xoffset -20
        ypos 50
        spacing 10

        vbox:
            yalign 0.5
            spacing 5

            # Opponent Guard
            hbox:
                xalign 0.5
                spacing 1

                if hasattr(move, "damage"):
                    for i in range(opponent.current_guard - move.damage):
                        add Transform("#00f", size=(guard_segment_size, 25))

                    for i in range(min(opponent.current_guard, move.damage)):
                        add Transform("fight_guard_animation", size=(guard_segment_size, 25))

                    for i in range(FightService.MAX_GUARD - opponent.current_guard):
                        add Transform("#404040", size=(guard_segment_size, 25))

                else:
                    for i in range(1, FightService.MAX_GUARD + 1):
                        if i > opponent.current_guard:
                            add Transform("#404040", size=(guard_segment_size, 25))
                        else:
                            add Transform("#00f", size=(guard_segment_size, 25))

            # Opponent Health
            hbox:
                xalign 0.5
                spacing 1

                if hasattr(move, "damage"):
                    for i in range(opponent.max_health - min(opponent.current_health, (move.damage - opponent.current_guard)) - (opponent.max_health - opponent.current_health)):
                        add Transform("#f00", size=(opponent_health_segment_size, 35))

                    for i in range(min(opponent.current_health, (move.damage - opponent.current_guard))):
                        add Transform("fight_health_animation", size=(opponent_health_segment_size, 35))

                    for i in range(opponent.max_health - opponent.current_health):
                        add Transform("#404040", size=(opponent_health_segment_size, 35))

                else:
                    for i in range(1, opponent.max_health + 1):
                        if i > opponent.current_health:
                            add Transform("#404040", size=(opponent_health_segment_size, 35))
                        else:
                            add Transform("#f00", size=(opponent_health_segment_size, 35))

        add Transform(opponent.character.profile_picture, xysize=(65, 65))

    hbox:
        pos (20, 50)
        spacing 10

        add Transform(player.character.profile_picture, xysize=(65, 65))

        vbox:
            yalign 0.5
            spacing 5

            # Player Guard
            hbox:
                xalign 0.5
                spacing 1

                for i in range(1, FightService.MAX_GUARD + 1):
                    if i > player.current_guard:
                        add Transform("#404040", size=(guard_segment_size, 25))
                    else:
                        add Transform("#00f", size=(guard_segment_size, 25))

            # Player Health
            hbox:
                xalign 0.5
                spacing 1

                for i in range(1, player.max_health + 1):
                    if i > player.current_health:
                        add Transform("#404040", size=(player_health_segment_size, 35))
                    else:
                        add Transform("#f00", size=(player_health_segment_size, 35))


screen action_info(fight, player, opponent, move):
    style_prefix "fight_turn"

    default player_max_stamina = max(player.current_stamina, player.max_stamina)

    vbox:
        align (0.5, 1.0)
        yoffset -250
        spacing 35

        if move.ideal_stance == player.stance or move.ideal_stance is None:
            frame:
                xysize (428, 132)
                background "fight_action_stance_info"
                padding (12, 48, 12, 12)

                text move.effect align (0.5, 0.5) text_align 0.5 size 13

        frame:
            xysize (428, 142)
            background "fight_action_info"
            padding (15, 15)

            vbox:
                xalign 0.5
                spacing 15

                frame:
                    ysize 30

                    if hasattr(move, "damage") and move.damage is not None:
                        text "Damage: {}".format(move.damage) size 15 yalign 0.5

                    text move.name size 30 align (0.5, 0.5)

                    hbox:
                        align (1.0, 0.5)
                        spacing 2

                        for i in range(1, player_max_stamina + 1):
                            if i > move.stamina_cost:
                                add Transform("fight_stamina_empty", zoom=0.4)
                            else:
                                add Transform("fight_stamina_filled", zoom=0.4)

                text move.description size 13 text_align 0.5 xalign 0.5

            button:
                align (0.5, 1.0)
                yoffset 60
                idle_background "fight_action_use_idle"
                hover_background "fight_action_use_hover"
                action [Hide("action_info"), Function(FightService.set_stance_bonus, player, move), Call("fight_attack_turn", fight, opponent, player, move)]
                xysize (160, 96)
                padding (32, 32)

                text "USE" align (0.5, 0.5)


screen fight_debug(player, opponent):
    zorder 1000
    style_prefix "fight_turn"

    frame:
        pos (50, 100)
        background "#fff"

        vbox:
            text "Player Guard: {}".format(player.current_guard)
            text "Player Health: {}".format(player.current_health)
            text "Player Stance: {}".format(player.stance)
            text "Player Stamina: {}".format(player.current_stamina)

            null height 10

            text "Opponent Guard: {}".format(opponent.current_guard)
            text "Opponent Health: {}".format(opponent.current_health) 
            text "Opponent Stance: {}".format(opponent.stance) 
            text "Opponent Stamina: {}".format(opponent.current_stamina)


style fight_overview_title is montserrat_extra_bold_64:
    color "#fff"

style fight_overview_text is text:
    font "fonts/Montserrat-ExtraBold.ttf"
    color "#fff"
    size 20
    text_align 0.5