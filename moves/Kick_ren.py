from dataclasses import dataclass
from game.fight.moves.BaseAttack_ren import BaseAttack
from game.fight.FightStance_ren import FightStance

"""renpy
init python:
"""


@dataclass
class Kick(BaseAttack):
    images: dict[str, str]

    description: str = "A devastating attack to your opponent's body."
    damage: int = 4
    stamina_cost: int = 5
    end_stance: FightStance = FightStance.FORWARD
    effect: str = "+20% Damage if used with exactly 5 Stamina left"

    def __post_init__(self) -> None:
        super().__init__("Kick", ideal_stance=FightStance.SOLID)
