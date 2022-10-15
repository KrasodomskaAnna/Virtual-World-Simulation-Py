from organisms.plants.plant import Plant
from utils.utils import *


class Dandelion(Plant):
    def __init__(self, game, position, strength=const.PLANT_STRENGTH, initiative=const.PLANT_INITIATIVE, age=0):
        super().__init__(game, position, strength, initiative, age)

    def action(self):
        for i in range(0, const.TRY_DANDELION_TO_SOW_NUMBER):
            self.sow()

    def create_new_one(self, position_for_new):
        return Dandelion(self._game, position_for_new, )

    def get_organism_type(self):
        return "DANDELION"

    def get_color(self):
        return "#F2B05E"
