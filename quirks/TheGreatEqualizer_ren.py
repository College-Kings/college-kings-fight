import re

from game.fight.Fighter_ren import Fighter
from game.fight.moves.types_ren import BaseAttack
from game.fight.quirks.FightQuirk_ren import FightQuirk

"""renpy
init python:
"""


class TheGreatEqualizer(FightQuirk):
    def __init__(self) -> None:
        self.name: str = re.sub("[A-Z]", " ", self.__class__.__name__).strip()
        self.description = (
            "Compared to the Opponent, deal more damage when you have less Health, but less "
            "damage when you have more "
        )

    def effect(self, attacker: Fighter, target: Fighter, move: BaseAttack) -> float:
        if target.health > attacker.health:
            return 0.8
        elif target.health < attacker.health:
            return 1.2
        else:
            return 1.0
