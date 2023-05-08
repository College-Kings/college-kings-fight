from dataclasses import dataclass, field
from typing import ClassVar

from game.fight.FightStance_ren import FightStance
from game.fight.moves.types_ren import FightMove
from game.characters.PlayableCharacters_ren import PlayableCharacter
from game.characters.NonPlayableCharacter_ren import NonPlayableCharacter

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

    player: PlayableCharacter
    opponent: NonPlayableCharacter
    end_label: str

    move_list: list[dict[str, list[FightMove]]] = field(default_factory=list)

    def __post__init__(self) -> None:
        self.stats: dict[str, dict[str, int]] = {
            self.player.name: {
                "guards_broken": 0,
                "damage_dealt": 0,
                "damage_blocked": 0,
                "damage_taken": 0,
            },
            self.opponent.name: {
                "guards_broken": 0,
                "damage_dealt": 0,
                "damage_blocked": 0,
                "damage_taken": 0,
            },
        }
