from typing import Union
from game.fight.moves.BodyHook_ren import BodyHook

from game.fight.moves.EndTurn_ren import EndTurn
from game.fight.moves.Hook_ren import Hook
from game.fight.moves.Jab_ren import Jab
from game.fight.moves.Kick_ren import Kick
from game.fight.moves.Turtle_ren import Turtle
from game.fight.moves.SpecialMove_ren import SpecialMove

"""renpy
init python:
"""

TurnMove = Union[EndTurn, Turtle]

BaseAttack = Union[BodyHook, Hook, Jab, Kick]

FightMove = Union[TurnMove, BaseAttack, SpecialMove]
