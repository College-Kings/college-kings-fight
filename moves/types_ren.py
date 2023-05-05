from __future__ import annotations
from typing import Union

from game.fight.moves.EndTurn_ren import EndTurn
from game.fight.moves.Turtle_ren import Turtle
from game.fight.moves.BaseAttack_ren import BaseAttack
from game.fight.moves.SpecialMove_ren import SpecialMove

"""renpy
init python:
"""

TurnMove = Union[EndTurn, Turtle]

FightMove = Union[TurnMove, BaseAttack, SpecialMove]
