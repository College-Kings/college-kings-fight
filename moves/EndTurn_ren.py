from dataclasses import dataclass
from typing import Optional

from game.fight.FightStance_ren import FightStance

"""renpy
init python:
"""


@dataclass(frozen=True)
class EndTurn:
    name: str = "End Turn"
    ideal_stance: Optional[FightStance] = None
    description: str = "End your turn and retain up to 2 stamina"
    stamina_cost: int = 0
    end_stance: Optional[FightStance] = None
    effect: str = "Save up to 2 Stamina to use next turn."


end_turn = EndTurn()
