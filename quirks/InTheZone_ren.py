from game.fight.Fighter_ren import Fighter
from game.fight.moves.types_ren import BaseAttack
from game.fight.quirks.FightQuirk_ren import FightQuirk

"""renpy
init 10 python:
"""


class InTheZone(FightQuirk):
    def __init__(self) -> None:
        self.name: str = "In The Zone"
        self.description = (
            "Attacks do more damage from their ideal stance, but less damage from a suboptimal "
            "stance "
        )

    def effect(self, attacker: Fighter, target: Fighter, move: BaseAttack) -> float:
        if attacker.stance == move.ideal_stance:
            return 1.2
        else:
            return 0.8


in_the_zone = InTheZone()
