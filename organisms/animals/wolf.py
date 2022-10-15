from organisms.animals.animal import Animal
from utils.utils import *


class Wolf(Animal):
    def __init__(self, game, position, strength=const.WOLF_STRENGTH, initiative=const.WOLF_INITIATIVE, age=0):
        super().__init__(game, position, strength, initiative, age)

    def create_new_one(self, position_for_new):
        return Wolf(self._game, position_for_new, )

    def is_the_same_specie(self, being_in_conflict):
        return isinstance(being_in_conflict, Wolf)

    def get_organism_type(self):
        return "WOLF"

    def get_color(self):
        return "#595959"

    def _get_step(self):
        return const.WOLF_STEP
