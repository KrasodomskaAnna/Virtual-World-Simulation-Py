from organisms.animals.animal import Animal
from utils.utils import *


class Lamp(Animal):
    def __init__(self, game, position, strength=const.LAMP_STRENGTH, initiative=const.LAMP_INITIATIVE, age=0):
        super().__init__(game, position, strength, initiative, age)

    def create_new_one(self, position_for_new):
        return Lamp(self._game, position_for_new, )

    def is_the_same_specie(self, being_in_conflict):
        return isinstance(being_in_conflict, Lamp)

    def get_organism_type(self):
        return "LAMP"

    def get_color(self):
        return "#D9A566"

    def _get_step(self):
        return const.CYBER_LAMP_STEP
