from dataclasses import dataclass
from typing import Optional

from game.fight.FightStance_ren import FightStance

"""renpy
init python:
"""


@dataclass
class BodyHook:
    images: dict[str, str]
    name: str = "Body Hook"
    ideal_stance: FightStance = FightStance.FORWARD
    description: str = "A devastating attack to your opponent's body"
    damage: int = 1
    stamina_cost: int = 2
    end_stance: Optional[FightStance] = FightStance.SOLID
    effect: str = "+20% Damage to next attack this turn"
