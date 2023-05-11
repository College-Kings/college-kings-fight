from dataclasses import dataclass
from game.fight.FightStance_ren import FightStance

"""renpy
init python:
"""


@dataclass
class Kick:
    images: dict[str, str]

    name: str = "Kick"
    ideal_stance: FightStance = FightStance.SOLID
    description: str = "A devastating attack to your opponent's body."
    damage: int = 4
    stamina_cost: int = 5
    end_stance: FightStance = FightStance.FORWARD
    effect: str = "+20% Damage if used with exactly 5 Stamina left"

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Kick):
            return NotImplemented

        return self.images == __value.images
