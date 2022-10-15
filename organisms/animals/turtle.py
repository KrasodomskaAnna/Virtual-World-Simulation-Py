from organisms.animals.animal import Animal
from utils.utils import *


class Turtle(Animal):
    def __init__(self, game, position, strength=const.TURTLE_STRENGTH, initiative=const.TURTLE_INITIATIVE, age=0):
        super().__init__(game, position, strength, initiative, age)

    def action(self):
        if not random_choice_probability(const.PROBABILITY_TURTLE_MOVE):
            return
        self._move()

    def collision_answer(self, being_in_conflict):
        if being_in_conflict is None:
            return
        if being_in_conflict.get_strength() < const.STRENGTH_REPEL_ATTACK_TURTLE:
            if not isinstance(being_in_conflict, Animal):
                return
            being_in_conflict.come_back()
            self._game.add_message(
                f"{being_in_conflict.get_organism_type()} attack is repel by {self.get_organism_type()} and must back off to the previous position \n")
        else:
            self.kill()
            self._game.add_message(f"{self.get_organism_type()} is kill by {being_in_conflict.get_organism_type()}\n")

    def create_new_one(self, position_for_new):
        return Turtle(self._game, position_for_new, )

    def is_the_same_specie(self, being_in_conflict):
        return isinstance(being_in_conflict, Turtle)

    def get_organism_type(self):
        return "TURTLE"

    def get_color(self):
        return "#5317A6"

    def _get_step(self):
        return const.TURTLE_STEP
