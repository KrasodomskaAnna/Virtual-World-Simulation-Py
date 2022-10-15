from organisms.plants.plant import Plant
from utils.utils import *


class Grass(Plant):
    def __init__(self, game, position, strength=Const.PLANT_STRENGTH, initiative=Const.PLANT_INITIATIVE, age=0):
        super().__init__(game, position, strength, initiative, age)

    def create_new_one(self, position_for_new):
        return Grass(self._game, position_for_new, )

    def get_organism_type(self):
        return "GRASS"

    def get_color(self):
        return "#BFB854"
