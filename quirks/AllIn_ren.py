from game.fight.Fighter_ren import Fighter
from game.fight.moves.types_ren import BaseAttack
from game.fight.quirks.FightQuirk_ren import FightQuirk

"""renpy
init 10 python:
"""


class AllIn(FightQuirk):
    def __init__(self) -> None:
        self.name: str = "All In"
        self.description = "Deal 100% more Damage, take 100% more Damage"

    def effect(self, attacker: Fighter, target: Fighter, move: BaseAttack) -> float:
        return 1.0


all_in = AllIn()
