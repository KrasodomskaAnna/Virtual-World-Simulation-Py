from organisms.animals.animal import Animal
from organisms.plants.plant import Plant
from utils.utils import *


class Guarana(Plant):
    def __init__(self, game, position, strength=const.PLANT_STRENGTH, initiative=const.PLANT_INITIATIVE, age=0):
        super().__init__(game, position, strength, initiative, age)

    def collision_answer(self, being_in_conflict):
        if being_in_conflict is None:
            return
        if isinstance(being_in_conflict, Animal):
            return
        being_in_conflict.set_strength(being_in_conflict.get_strength() + const.GUARANA_INCREASE_STRENGTH_WHO_EAT)
        self._game.add_message(
            f"{self.get_organism_type()} increased strength of {being_in_conflict.get_organism_type()} so it's now {being_in_conflict.get_strength()}\n")
        self.kill()

    def create_new_one(self, position_for_new):
        return Guarana(self._game, position_for_new, )

    def get_organism_type(self):
        return "GUARANA"

    def get_color(self):
        return "#022026"
