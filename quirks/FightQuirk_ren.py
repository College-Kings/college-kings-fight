from abc import abstractmethod
from typing import Protocol

from game.fight.Fighter_ren import Fighter
from game.fight.moves.types_ren import BaseAttack

"""renpy
init python:
"""


class FightQuirk(Protocol):
    @abstractmethod
    def effect(
        self, attacker: "Fighter", target: "Fighter", move: BaseAttack
    ) -> float: ...
