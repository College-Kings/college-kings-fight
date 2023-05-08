from __future__ import annotations
from typing import Optional

from game.fight.FightStance_ren import FightStance
from game.fight.moves.types_ren import BaseAttack, FightMove
from game.fight.quirks.FightQuirk_ren import FightQuirk
from game.fight.Fight_ren import Fight
from game.fight.moves.SpecialMove_ren import SpecialMove
from game.fight.moves.Turtle_ren import turtle
from game.fight.moves.EndTurn_ren import end_turn


"""renpy
init python:
"""


class Fighter:
    MAX_GUARD: int = FightStance.DEFENSIVE.value + 1  # Turtle stance bonus

    def __init__(
        self,
        name: str,
        stance: FightStance,
        health: int = 20,
        stamina: int = 8,
        attack_multiplier: int = 1,
        quirk: Optional[FightQuirk] = None,
    ) -> None:
        self.name: str = name
        self._stance: FightStance = stance
        self.stamina: int = stamina
        self.max_health: int = health
        self.attack_multiplier: int = attack_multiplier
        self.quirk: Optional[FightQuirk] = quirk

        self.max_stamina: int = stamina
        self.stance_bonus: Optional[str] = None

        self._health: int = health
        self._guard: float = stance.value

        self.turn_moves: list[FightMove] = [turtle, end_turn]
        self.base_attacks: list[BaseAttack] = []
        self.special_attacks: list[SpecialMove] = []
        self.special_attack: Optional[SpecialMove] = None
        self.previous_moves: list[FightMove] = []

    @property
    def health(self) -> int:
        return int(self._health)

    @health.setter
    def health(self, value: int) -> None:
        self._health = max(value, 0)

    @property
    def guard(self) -> int:
        return int(self._guard)

    @guard.setter
    def guard(self, value: int) -> None:
        self._guard = max(value, 0)

    @property
    def stance(self) -> FightStance:
        return self._stance

    @stance.setter
    def stance(self, stance: FightStance) -> None:
        self._stance = stance
        self._guard = stance.value

    def set_stance_bonus(self, move: BaseAttack) -> None:
        if self.stance == move.ideal_stance:
            self.stance_bonus = move.name
        else:
            self.stance_bonus = None

    def get_primed_multiplier(self, fight: Fight, move: FightMove) -> float:
        return 1.0

    def get_reckless_multiplier(self, fight: Fight) -> float:
        return 1.0

    def get_calculating_multiplier(self, fight: Fight) -> float:
        return 0

    def get_stance_multiplier(self, fight: Fight) -> float:
        if self.stance_bonus == "Body Hook":
            return 1.2

        # Stance Bonus: Kick
        if self.stance_bonus == "Kick" and self.stamina == 5:
            return 1.2

        return 1.0

    def add_special_attack(self, move: SpecialMove) -> None:
        self.special_attacks.append(move)

    def set_special_attack(self, move: SpecialMove) -> None:
        self.special_attack = move
        if move not in self.special_attacks:
            self.special_attacks.append(move)
