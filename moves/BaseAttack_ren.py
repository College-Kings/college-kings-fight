from dataclasses import dataclass
from typing import ClassVar, Optional

from game.fight.FightStance_ren import FightStance

"""renpy
init -20 python:
"""


@dataclass
class BaseAttack:
    DAMAGE_DICT: ClassVar[dict[FightStance, int]] = {
        FightStance.AGGRESSIVE: 5,
        FightStance.DEFENSIVE: -5,
        FightStance.FORWARD: 0,
        FightStance.SOLID: 0,
    }

    name: str
    ideal_stance: Optional[FightStance]
