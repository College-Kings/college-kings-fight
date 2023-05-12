from game.fight.Fight_ren import Fight
from game.fight.Fighter_ren import Fighter
from game.fight.moves.SpecialMove_ren import SpecialMove
from game.fight.FightStance_ren import FightStance

"""renpy
init python:
"""


class Uppercut(SpecialMove):
    def __init__(self, images: dict[str, str]) -> None:
        self.images: dict[str, str] = images

        self.name = "Uppercut"
        self.ideal_stance = FightStance.AGGRESSIVE
        self.description = (
            "If Opponent's Health is 20% or less, this attack deals +50% Damage"
        )
        self.damage = 4
        self.stamina_cost = 4
        self.end_stance = FightStance.FORWARD
        self.effect = (
            "If Opponent's Health is 20% or less, this attack deals +50% Damage"
        )

    def is_sensitive(self, fight: Fight, target: Fighter, attacker: Fighter) -> bool:
        return fight.stats[attacker]["damage_dealt"] >= 40

    def check_level_1_stance_bonus(
        self, fight: Fight, target: Fighter, attacker: Fighter
    ) -> bool:
        return target.current_health <= target.max_health * 0.2

    def check_level_2_stance_bonus(
        self, fight: Fight, target: Fighter, attacker: Fighter
    ) -> bool:
        raise NotImplementedError()

    def check_level_3_stance_bonus(
        self, fight: Fight, target: Fighter, attacker: Fighter
    ) -> bool:
        return not fight.move_list[-1][attacker]
