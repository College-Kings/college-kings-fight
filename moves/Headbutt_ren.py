from game.fight.Fight_ren import Fight
from game.fight.Fighter_ren import Fighter
from game.fight.moves.SpecialMove_ren import SpecialMove
from game.fight.FightStance_ren import FightStance
from game.fight.moves.Turtle_ren import Turtle

"""renpy
init python:
"""


class Headbutt(SpecialMove):
    def __init__(self, images: dict[str, str]) -> None:
        super().__init__("Headbutt", ideal_stance=FightStance.AGGRESSIVE)
        self.images: dict[str, str] = images

        self.description: str = 'If you used "Turtle" last turn, deal +30% more Damage'
        self.damage = 2
        self.stamina_cost = 2
        self.end_stance = FightStance.SOLID
        self.effect = 'If you used "Turtle" last turn, deal +30% more Damage'

    def is_sensitive(self, fight: Fight, target: Fighter, attacker: Fighter) -> bool:
        return fight.stats[target.name]["guards_broken"] >= 3

    def check_level_1_stance_bonus(
        self, fight: Fight, target: Fighter, attacker: Fighter
    ) -> bool:
        return isinstance(fight.move_list[-2][attacker.name][-1], Turtle)

    def check_level_2_stance_bonus(
        self, fight: Fight, target: Fighter, attacker: Fighter
    ) -> bool:
        return target.guard == 0

    def check_level_3_stance_bonus(
        self, fight: Fight, target: Fighter, attacker: Fighter
    ) -> bool:
        return not fight.move_list[-1][attacker.name]
