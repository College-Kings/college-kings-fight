from game.fight.Fighter_ren import Fighter
from game.fight.moves.types_ren import BaseAttack
from game.fight.quirks.FightQuirk_ren import FightQuirk

"""renpy
init 10 python:
"""


class Backlash(FightQuirk):
    def __init__(self) -> None:
        self.name: str = "Backlash"
        self.description = "When your Guard is broken, deal damage to your opponent"

    def effect(self, attacker: Fighter, target: Fighter, move: BaseAttack) -> float:
        return 1.0


backlash = Backlash()
