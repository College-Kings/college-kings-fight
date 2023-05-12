from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

from game.characters.ICharacter_ren import ICharacter
from game.fight.FightStance_ren import FightStance
from game.fight.moves.types_ren import BaseAttack, FightMove
from game.fight.quirks.FightQuirk_ren import FightQuirk
from game.fight.moves.SpecialMove_ren import SpecialMove

"""renpy
init 10 python:
"""


@dataclass
class Fighter:
    character: ICharacter
    stance: FightStance
    max_health: int
    max_stamina: int
    attack_multiplier: float
    quirk: Optional[FightQuirk]

    current_health: int
    current_guard: int
    current_stamina: int

    stance_bonus: Optional[BaseAttack] = None
    stance_images: dict[FightStance, str] = field(default_factory=dict)
    turn_moves: list[FightMove] = field(default_factory=list)
    base_attacks: list[BaseAttack] = field(default_factory=list)
    special_attacks: list[SpecialMove] = field(default_factory=list)
    special_attack: Optional[SpecialMove] = None
    previous_moves: list[FightMove] = field(default_factory=list)

    @property
    def display_health(self) -> int:
        return max(self.current_health, 0)

    @property
    def display_guard(self) -> int:
        return max(self.current_health, 0)

    @property
    def stance_image(self) -> str:
        return self.stance_images[self.stance]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.character})"

    def __hash__(self) -> int:
        return hash(self.character)

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Fighter):
            return NotImplemented

        return self.character == __value.character
