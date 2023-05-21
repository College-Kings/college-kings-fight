from __future__ import annotations
from abc import ABC, abstractmethod

from game.fight.Fight_ren import Fight
from game.fight.Fighter_ren import Fighter

"""renpy
init -10 python:
"""


class SpecialMove(ABC, object):
    @abstractmethod
    def is_sensitive(self, fight: Fight, target: Fighter, attacker: Fighter) -> bool:
        ...

    @abstractmethod
    def check_level_1_stance_bonus(
        self, fight: Fight, target: Fighter, attacker: Fighter
    ) -> bool:
        ...

    @abstractmethod
    def check_level_2_stance_bonus(
        self, fight: Fight, target: Fighter, attacker: Fighter
    ) -> bool:
        ...

    @abstractmethod
    def check_level_3_stance_bonus(
        self, fight: Fight, target: Fighter, attacker: Fighter
    ) -> bool:
        ...
