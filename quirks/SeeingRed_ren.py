import re

from game.fight.Fighter_ren import Fighter
from game.fight.moves.types_ren import BaseAttack
from game.fight.quirks.FightQuirk_ren import FightQuirk

"""renpy
init python:
"""


class SeeingRed(FightQuirk):
    def __init__(self) -> None:
        self.name: str = re.sub("[A-Z]", " ", self.__class__.__name__).strip()
        self.description = (
            "Ending in Aggressive Stance leaves no guard, but your first attack next turn does "
            "double damage "
        )

    def effect(self, attacker: Fighter, target: Fighter, move: BaseAttack) -> float:
        return 1.0
