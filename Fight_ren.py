from dataclasses import dataclass, field
from typing import ClassVar, Optional

from game.fight.FightStance_ren import FightStance
from game.fight.Fighter_ren import Fighter
from game.fight.moves.types_ren import FightMove

"""renpy
init python:
"""


@dataclass
class Fight:
    DAMAGE_DICT: ClassVar[dict[FightStance, int]] = {
        FightStance.AGGRESSIVE: 5,
        FightStance.DEFENSIVE: -5,
        FightStance.FORWARD: 0,
        FightStance.SOLID: 0,
    }

    end_label: str
    player: Optional["Fighter"] = None
    opponent: Optional["Fighter"] = None

    move_list: list[dict["Fighter", list["FightMove"]]] = field(default_factory=list)
    stats: dict["Fighter", dict[str, int]] = field(default_factory=dict)

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, type(self)):
            return NotImplemented

        return (
            self.player == __value.player
            and self.opponent == __value.opponent
            and self.end_label == __value.end_label
        )
