from game.fight.Fight_ren import Fight
from game.fight.moves.SpecialMove_ren import SpecialMove
from game.fight.FightStance_ren import FightStance
from game.fight.Fighter_ren import Fighter

"""renpy
init python:
"""


class OverhandPunch(SpecialMove):
    def __init__(self, images: dict[str, str]) -> None:
        self.images: dict[str, str] = images

        self.name = "Overhand Punch"
        self.ideal_stance = FightStance.FORWARD
        self.description = "Breaks Guard and deals 100% Damage if it's at 30% or less"
        self.damage = 3
        self.stamina_cost = 3
        self.end_stance = FightStance.AGGRESSIVE
        self.effect = "Breaks Guard and deals 100% Damage if it's at 30% or less"

    def is_sensitive(self, fight: Fight, target: Fighter, attacker: Fighter) -> bool:
        return fight.stats[attacker.name]["guards_broken"] >= 3

    def check_level_1_stance_bonus(
        self, fight: Fight, target: Fighter, attacker: Fighter
    ) -> bool:
        return target.guard <= Fighter.MAX_GUARD * 0.3

    def check_level_2_stance_bonus(
        self, fight: Fight, target: Fighter, attacker: Fighter
    ) -> bool:
        raise NotImplementedError()

    def check_level_3_stance_bonus(
        self, fight: Fight, target: Fighter, attacker: Fighter
    ) -> bool:
        raise NotImplementedError()
