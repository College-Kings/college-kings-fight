from typing import Optional

from game.characters.ICharacter_ren import ICharacter
from game.characters.PlayableCharacters_ren import PlayableCharacter
from game.fight.FightStance_ren import FightStance
from game.fight.Fight_ren import Fight
from game.fight.Fighter_ren import Fighter
from game.fight.moves.BodyHook_ren import BodyHook
from game.fight.moves.Kick_ren import Kick
from game.fight.moves.SpecialMove_ren import SpecialMove
from game.fight.moves.Turtle_ren import turtle
from game.fight.moves.EndTurn_ren import end_turn
from game.fight.moves.types_ren import BaseAttack, FightMove
from game.fight.quirks.FightQuirk_ren import FightQuirk

"""renpy
init python:
"""


class FightService:
    MAX_GUARD: int = FightStance.DEFENSIVE.value + 1  # Turtle stance bonus

    @staticmethod
    def create_fighter(
        character: ICharacter,
        stance: FightStance,
        max_health: int = 20,
        max_stamina: int = 8,
        attack_multiplier: float = 1.0,
        quirk: Optional["FightQuirk"] = None,
    ) -> "Fighter":
        return Fighter(
            character,
            stance,
            max_health,
            max_stamina,
            attack_multiplier,
            quirk,
            current_health=max_health,
            current_guard=stance.value,
            current_stamina=max_stamina,
            turn_moves=[turtle, end_turn],
        )

    @staticmethod
    def set_stance(fighter: "Fighter", stance: FightStance) -> None:
        fighter.stance = stance
        fighter.current_guard = stance.value

    @staticmethod
    def set_stance_images(
        fighter: "Fighter", stance_images: dict[FightStance, str]
    ) -> None:
        if isinstance(fighter.character, PlayableCharacter):
            raise ValueError("Playable characters cannot have stance images")

        fighter.stance_images = stance_images

    @staticmethod
    def set_stance_bonus(fighter: "Fighter", move: "BaseAttack") -> None:
        if fighter.stance == move.ideal_stance:
            fighter.stance_bonus = move
        else:
            fighter.stance_bonus = None

    @staticmethod
    def add_base_attack(fighter: "Fighter", move: "BaseAttack") -> None:
        fighter.base_attacks.append(move)

    @staticmethod
    def add_special_attack(fighter: "Fighter", move: SpecialMove) -> None:
        fighter.special_attacks.append(move)

    @staticmethod
    def set_special_attack(fighter: "Fighter", move: SpecialMove) -> None:
        fighter.special_attack = move
        if move not in fighter.special_attacks:
            fighter.special_attacks.append(move)

    @staticmethod
    def set_quirk(fighter: "Fighter", quirk: "FightQuirk") -> None:
        fighter.quirk = quirk

    @staticmethod
    def start_fight(fight: Fight) -> None:
        if fight.player is None or fight.opponent is None:
            raise ValueError("Fight must have a player and an opponent")

        fight.opponent.max_health = int(fight.opponent.max_health)
        fight.opponent.max_stamina = int(fight.opponent.max_stamina)
        fight.opponent.current_health = int(fight.opponent.max_health)
        fight.opponent.current_stamina = int(fight.opponent.max_stamina)

        fight.stats = {
            fight.player: {
                "guards_broken": 0,
                "damage_dealt": 0,
                "damage_blocked": 0,
                "damage_taken": 0,
            },
            fight.opponent: {
                "guards_broken": 0,
                "damage_dealt": 0,
                "damage_blocked": 0,
                "damage_taken": 0,
            },
        }

    @staticmethod
    def get_primed_multiplier(
        fighter: "Fighter", fight: Fight, move: "FightMove"
    ) -> float:
        if fight.player is None or fight.opponent is None:
            raise ValueError("Fight must have a player and an opponent")

        if isinstance(fighter.character, PlayableCharacter):
            return 1.0

        try:
            if fight.move_list[-1][fight.player].count(move) != 2:
                return 1.0

            if fighter.current_health / float(fighter.max_health) <= 0.25:
                return 0.7
            elif 0.25 < fighter.current_health / float(fighter.max_health) <= 0.5:
                return 0.4
            else:
                return 0.1

        except IndexError:
            return 1.0

    @staticmethod
    def get_reckless_multiplier(fighter: "Fighter", fight: Fight) -> float:
        if fight.player is None or fight.opponent is None:
            raise ValueError("Fight must have a player and an opponent")

        if isinstance(fighter.character, PlayableCharacter):
            return 1.0

        try:
            if (
                fight.move_list[-5][fight.player][-1] != turtle
                and fight.move_list[-3][fight.player][-1] != turtle
            ):
                return 1.0

            if fighter.current_health / float(fighter.max_health) <= 0.25:
                return 1.9
            elif 0.25 < fighter.current_health / float(fighter.max_health) <= 0.5:
                return 1.6
            else:
                return 1.3

        except IndexError:
            return 1.0

    @staticmethod
    def get_calculating_multiplier(fighter: "Fighter", fight: Fight) -> float:
        if fight.player is None or fight.opponent is None:
            raise ValueError("Fight must have a player and an opponent")

        if isinstance(fighter.character, PlayableCharacter):
            return 0

        try:
            if fight.move_list[-4][fighter] != fight.move_list[-2][fighter]:
                return 0

            if fight.opponent.current_health / float(fight.opponent.max_health) <= 0.25:
                return 0.9
            elif (
                0.25
                < fight.opponent.current_health / float(fight.opponent.max_health)
                <= 0.5
            ):
                return 0.6
            else:
                return 0.3

        except IndexError:
            return 0

    @staticmethod
    def get_stance_multiplier(fighter: "Fighter", fight: Fight) -> float:
        if isinstance(fighter.stance_bonus, BodyHook):
            return 1.2

        if isinstance(fighter.stance_bonus, Kick) and fighter.current_stamina == 5:
            return 1.2

        return 1.0
