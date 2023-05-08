from dataclasses import dataclass
from game.fight.FightStance_ren import FightStance

"""renpy
init python:
"""


@dataclass
class Hook:
    images: dict[str, str]

    name: str = "Hook"
    ideal_stance: FightStance = FightStance.FORWARD
    description: str = "A devastating attack to your opponent's head."
    damage: int = 3
    stamina_cost: int = 4
    end_stance: FightStance = FightStance.AGGRESSIVE
    effect: str = "Opp has -2 Stamina at the start of their next turn if not blocked [[Once per turn]]"
