from organisms.plants.plant import Plant
from utils.utils import *


class Nightshade(Plant):
    def __init__(self, game, position, strength=const.NIGHTSHADE_STRENGTH, initiative=const.PLANT_INITIATIVE, age=0):
        super().__init__(game, position, strength, initiative, age)

    def collision_answer(self, being_in_conflict):
        if being_in_conflict is None:
            return
        being_in_conflict.kill()
        self._game.add_message(f"{being_in_conflict.get_organism_type()} is kill by {self.get_organism_type()}\n")

    def create_new_one(self, position_for_new):
        return Nightshade(self._game, position_for_new, )

    def get_organism_type(self):
        return "NIGHTSHADE"

    def get_color(self):
        return "#C88BD9"
