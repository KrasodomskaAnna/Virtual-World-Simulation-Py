from organisms.animals.animal import Animal
from utils.utils import *


class Fox(Animal):
    def __init__(self, game, position, strength=const.FOX_STRENGTH, initiative=const.FOX_INITIATIVE, age=0):
        super().__init__(game, position, strength, initiative, age)

    def create_new_one(self, position_for_new):
        return Fox(self._game, position_for_new, )

    def is_the_same_specie(self, being_in_conflict):
        return isinstance(being_in_conflict, Fox)

    def get_organism_type(self):
        return "FOX"

    def get_color(self):
        return "#BF6836"

    def _get_step(self):
        return const.FOX_STEP

    def _is_free(self, position):
        for organism in self._game.organisms:
            if position == organism.get_position():
                if organism.get_strength() > self._strength:
                    return False
        for organism in self._game.updated_organisms:
            if position == organism.get_position():
                if organism.get_strength() > self._strength:
                    return False
        return True

    def _position_move(self):
        return self._random_neighbor(True, self._get_step())
