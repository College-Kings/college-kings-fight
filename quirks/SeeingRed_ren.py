from game.fight.Fighter_ren import Fighter
from game.fight.moves.types_ren import BaseAttack
from game.fight.quirks.FightQuirk_ren import FightQuirk

"""renpy
init 10 python:
"""


class SeeingRed(FightQuirk):
    def __init__(self) -> None:
        self.name: str = "Seeing Red"
        self.description = (
            "Ending in Aggressive Stance leaves no guard, but your first attack next turn does "
            "double damage "
        )

    def effect(self, attacker: Fighter, target: Fighter, move: BaseAttack) -> float:
        return 1.0


seeing_red = SeeingRed()
