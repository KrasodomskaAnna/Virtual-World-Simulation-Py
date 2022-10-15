from abc import ABC, abstractmethod

from organisms.animals.animal import Animal
from organisms.organism import Organism
from utils.utils import *


class Plant(Organism, ABC):
    def __init__(self, game, position, strength, initiative=Const.PLANT_INITIATIVE, age=0):
        super().__init__(game, position, strength, initiative, age)

    def collision_answer(self, being_in_conflict):
        if being_in_conflict is None:
            return
        self.kill()
        if isinstance(being_in_conflict, Animal):
            self._game.add_message(
                f"{being_in_conflict.get_organism_type()} change position to {self.get_position_notation()} so eat {self.get_organism_type()}\n")

    def action(self):
        self.sow()

    def collision(self):
        self.collision_answer(self._collision_with())

    def sow(self):
        if not random_choice_probability(Const.PROBABILITY_SOW):
            return
        position_for_new = self._random_neighbor(True, Const.NEIGHBOUR_SHIFT)
        if position_for_new == Point(Const.ERROR, Const.ERROR):
            return
        self._game.add_message(f"{self.get_organism_type()} sow a new plant!\n")
        self._game.updated_organisms.append(self.create_new_one(position_for_new))

    @abstractmethod
    def create_new_one(self, position_for_new):
        pass
