from dataclasses import dataclass
from typing import Optional

from game.fight.FightStance_ren import FightStance

"""renpy
init python:
"""


@dataclass(frozen=True)
class Turtle:
    name: str = "Turtle"
    ideal_stance: FightStance = FightStance.SOLID
    description: str = "End turn and set stance to Defensive"
    stamina_cost: int = 4
    end_stance: Optional[FightStance] = FightStance.DEFENSIVE
    effect: str = "+1 Guard"


turtle = Turtle()
