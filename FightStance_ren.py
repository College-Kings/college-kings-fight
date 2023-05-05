from enum import IntEnum
import enum

"""renpy
init -30 python:
"""


class FightStance(IntEnum):
    AGGRESSIVE = enum.auto()
    FORWARD = enum.auto()
    SOLID = enum.auto()
    DEFENSIVE = enum.auto()

    @classmethod
    def _missing_(cls, value):
        return cls.AGGRESSIVE
