from dataclasses import dataclass
from game.fight.moves.BaseAttack_ren import BaseAttack
from game.fight.FightStance_ren import FightStance

"""renpy
init python:
"""


@dataclass
class Hook(BaseAttack):
    images: dict[str, str]

    description: str = "A devastating attack to your opponent's head."
    damage: int = 3
    stamina_cost: int = 4
    end_stance: FightStance = FightStance.AGGRESSIVE
    effect: str = "Opp has -2 Stamina at the start of their next turn if not blocked [[Once per turn]]"

    def __post_init__(self) -> None:
        super().__init__("Hook", ideal_stance=FightStance.FORWARD)
