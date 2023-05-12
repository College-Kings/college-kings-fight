from game.fight.Fighter_ren import Fighter
from game.fight.moves.types_ren import BaseAttack
from game.fight.quirks.FightQuirk_ren import FightQuirk

"""renpy
init 10 python:
"""


class TheGreatEqualizer(FightQuirk):
    def __init__(self) -> None:
        self.name: str = "The Great Equalizer"
        self.description = (
            "Compared to the Opponent, deal more damage when you have less Health, but less "
            "damage when you have more "
        )

    def effect(self, attacker: Fighter, target: Fighter, move: BaseAttack) -> float:
        if target.current_health > attacker.current_health:
            return 0.8
        elif target.current_health < attacker.current_health:
            return 1.2
        else:
            return 1.0


the_great_equalizer = TheGreatEqualizer()
