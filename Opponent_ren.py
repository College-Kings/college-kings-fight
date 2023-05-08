from game.fight.FightStance_ren import FightStance
from game.fight.Fighter_ren import Fighter
from game.fight.moves.Turtle_ren import Turtle
from game.fight.moves.types_ren import FightMove
from game.fight.Fight_ren import Fight

turtle: Turtle

"""renpy
init python:
"""


class Opponent(Fighter):
    def __init__(
        self,
        name: str,
        stance: FightStance,
        health: int = 20,
        stamina: int = 8,
        attack_multiplier: int = 1,
    ) -> None:
        super().__init__(name, stance, health, stamina, attack_multiplier)

        self.stance_images: dict[FightStance, str] = {}

    @property
    def stance_image(self) -> str:
        return self.stance_images[self.stance]

    def get_primed_multiplier(self, fight: Fight, move: FightMove) -> float:
        try:
            if fight.move_list[-1][fight.player.name].count(move) != 2:
                return 1.0

            if self.health / float(self.max_health) <= 0.25:
                return 0.7
            elif 0.25 < self.health / float(self.max_health) <= 0.5:
                return 0.4
            else:
                return 0.1

        except IndexError:
            return 1.0

    def get_reckless_multiplier(self, fight: Fight) -> float:
        try:
            if (
                fight.move_list[-5][fight.player.name][-1] != turtle
                and fight.move_list[-3][fight.player.name][-1] != turtle
            ):
                return 1.0

            if self.health / float(self.max_health) <= 0.25:
                return 1.9
            elif 0.25 < self.health / float(self.max_health) <= 0.5:
                return 1.6
            else:
                return 1.3

        except IndexError:
            return 1.0

    def get_calculating_multiplier(self, fight: Fight) -> float:
        try:
            if fight.move_list[-4][self.name] != fight.move_list[-2][self.name]:
                return 0

            if (
                fight.opponent.fighter.health / float(fight.opponent.fighter.max_health)
                <= 0.25
            ):
                return 0.9
            elif (
                0.25
                < fight.opponent.fighter.health
                / float(fight.opponent.fighter.max_health)
                <= 0.5
            ):
                return 0.6
            else:
                return 0.3

        except IndexError:
            return 0
