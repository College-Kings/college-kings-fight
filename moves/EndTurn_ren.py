from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from game.fight.FightStance_ren import FightStance

"""renpy
init python:
"""


@dataclass
class EndTurn:
    name: str = "End Turn"
    description: str = "End your turn and retain up to 2 stamina"
    stamina_cost: int = 0
    end_stance: Optional[FightStance] = None
    effect: str = "Save up to 2 Stamina to use next turn."
