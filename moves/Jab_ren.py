from dataclasses import dataclass
from game.fight.FightStance_ren import FightStance

"""renpy
init python:
"""


@dataclass
class Jab:
    images: dict[str, str]

    name: str = "Jab"
    ideal_stance: FightStance = FightStance.AGGRESSIVE
    description: str = "Attack with a quick jab straight to the chin."
    damage: int = 2
    stamina_cost: int = 3
    end_stance: FightStance = FightStance.FORWARD
    effect: str = "Next Attack this turn ignores guard"

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Jab):
            return NotImplemented

        return self.images == __value.images
