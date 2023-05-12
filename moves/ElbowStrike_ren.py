from game.fight.moves.SpecialMove_ren import SpecialMove
from game.fight.FightStance_ren import FightStance
from game.fight.Fight_ren import Fight
from game.fight.Fighter_ren import Fighter

"""renpy
init python:
"""


class ElbowStrike(SpecialMove):
    def __init__(self, images: dict[str, str]) -> None:
        self.name: str = "Elbow Strike"
        self.ideal_stance: FightStance = FightStance.SOLID
        self.images: dict[str, str] = images

        self.description: str = ""
        self.damage = 5
        self.stamina_cost = 5
        self.end_stance = FightStance.FORWARD
        self.effect = "50% Damage bypasses Guard"

    def is_sensitive(self, fight: Fight, target: Fighter, attacker: Fighter) -> bool:
        return fight.stats[attacker]["damage_taken"] >= 40

    def check_level_1_stance_bonus(
        self, fight: Fight, target: Fighter, attacker: Fighter
    ) -> bool:
        return True

    def check_level_2_stance_bonus(
        self, fight: Fight, target: Fighter, attacker: Fighter
    ) -> bool:
        return True

    def check_level_3_stance_bonus(
        self, fight: Fight, target: Fighter, attacker: Fighter
    ) -> bool:
        return True
