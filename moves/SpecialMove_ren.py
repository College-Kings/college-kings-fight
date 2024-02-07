from typing import Protocol, runtime_checkable
from abc import abstractmethod

from game.fight.Fight_ren import Fight
from game.fight.Fighter_ren import Fighter

"""renpy
init -10 python:
"""


@runtime_checkable
class SpecialMove(Protocol):
    @abstractmethod
    def is_sensitive(
        self, fight: "Fight", target: "Fighter", attacker: "Fighter"
    ) -> bool: ...

    @abstractmethod
    def check_level_1_stance_bonus(
        self, fight: "Fight", target: "Fighter", attacker: "Fighter"
    ) -> bool: ...

    @abstractmethod
    def check_level_2_stance_bonus(
        self, fight: "Fight", target: "Fighter", attacker: "Fighter"
    ) -> bool: ...

    @abstractmethod
    def check_level_3_stance_bonus(
        self, fight: "Fight", target: "Fighter", attacker: "Fighter"
    ) -> bool: ...
