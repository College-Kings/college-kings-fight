import re

from game.fight.Fighter_ren import Fighter
from game.fight.moves.BaseAttack_ren import BaseAttack
from game.fight.quirks.FightQuirk_ren import FightQuirk

"""renpy
init python:
"""


class AllIn(FightQuirk):
    def __init__(self) -> None:
        self.name: str = re.sub("[A-Z]", " ", self.__class__.__name__).strip()
        self.description = "Deal 100% more Damage, take 100% more Damage"

    def effect(self, attacker: Fighter, target: Fighter, move: BaseAttack) -> float:
        return 1.0
