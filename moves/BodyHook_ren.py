from dataclasses import dataclass
from typing import Optional

from game.fight.moves.BaseAttack_ren import BaseAttack
from game.fight.FightStance_ren import FightStance

"""renpy
init python:
"""


@dataclass
class BodyHook(BaseAttack):
    images: dict[str, str]
    description: str = "A devastating attack to your opponent's body"
    damage: int = 1
    stamina_cost: int = 2
    end_stance: Optional[FightStance] = FightStance.SOLID
    effect: str = "+20% Damage to next attack this turn"

    def __post_init__(self) -> None:
        super().__init__("Body Hook", ideal_stance=FightStance.FORWARD)
