from organisms.animals.animal import Animal
from utils.utils import *


class Human(Animal):

    def __init__(self, game, position, strength=const.HUMAN_STRENGTH, initiative=const.HUMAN_INITIATIVE, age=0):
        super().__init__(game, position, strength, initiative, age)

    def action(self):
        new_position = {
            "UP": Point(self._position.x + 0, self._position.y - const.HUMAN_STEP),
            "DOWN": Point(self._position.x + 0, self._position.y + const.HUMAN_STEP),
            "RIGHT": Point(self._position.x + const.HUMAN_STEP, self._position.y + 0),
            "LEFT": Point(self._position.x - const.HUMAN_STEP, self._position.y + 0),
            "-": Point(const.ERROR, const.ERROR)
        }[self._game.get_input()]
        if new_position is None:
            return
        if new_position == Point(const.ERROR, const.ERROR):
            return
        if self.is_on_board(new_position):
            self._swap_position(new_position)

    def collision(self):
        being_in_conflict = self._collision_with()
        if being_in_conflict is None:
            return
        if not self._game.is_alzur_shield_active() or not isinstance(being_in_conflict, Animal):
            if being_in_conflict.get_strength() <= self._strength:
                being_in_conflict.collision_answer(self)
            else:
                self.kill()
        else:
            being_in_conflict.run_away()
            self._game.add_message(
                f"{self.get_organism_type()} from position {self.get_position_notation()} deter {being_in_conflict.get_organism_type()} which go away to {being_in_conflict.get_position_notation()}\n")

    def collision_answer(self, being_in_conflict):
        if being_in_conflict is None:
            return
        if not self._game.is_alzur_shield_active():
            self.kill()
            return
        if isinstance(being_in_conflict, Animal) is not None:
            being_in_conflict.run_away()

    def create_new_one(self, position_for_new):
        # human can not reproduce
        return None

    def is_the_same_specie(self, being_in_conflict):
        # there is only one human in the world
        return False

    def get_organism_type(self):
        return "HUMAN"

    def kill(self):
        self._is_alive = False
        self._game.end_game("You died")

    def _get_step(self):
        return const.HUMAN_STEP

    def get_color(self):
        return "#9AA3D9"
