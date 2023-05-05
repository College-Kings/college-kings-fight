from dataclasses import dataclass
from game.fight.moves.BaseAttack_ren import BaseAttack
from game.fight.FightStance_ren import FightStance

"""renpy
init python:
"""


@dataclass
class Jab(BaseAttack):
    images: dict[str, str]

    description: str = "Attack with a quick jab straight to the chin."
    damage: int = 2
    stamina_cost: int = 3
    end_stance: FightStance = FightStance.FORWARD
    effect: str = "Next Attack this turn ignores guard"

    def __post_init__(self) -> None:
        super().__init__("Jab", ideal_stance=FightStance.AGGRESSIVE)
