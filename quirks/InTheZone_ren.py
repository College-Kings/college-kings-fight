import re
from game.fight.Fighter_ren import Fighter
from game.fight.moves.BaseAttack_ren import BaseAttack
from game.fight.quirks.FightQuirk_ren import FightQuirk

"""renpy
init python:
"""


class InTheZone(FightQuirk):
    def __init__(self) -> None:
        self.name: str = re.sub("[A-Z]", " ", self.__class__.__name__).strip()
        self.description = (
            "Attacks do more damage from their ideal stance, but less damage from a suboptimal "
            "stance "
        )

    def effect(self, attacker: Fighter, target: Fighter, move: BaseAttack) -> float:
        if attacker.stance == move.ideal_stance:
            return 1.2
        else:
            return 0.8
