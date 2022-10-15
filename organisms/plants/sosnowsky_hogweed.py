import organisms.animals.cyber as cyber
from organisms.animals.animal import Animal
from organisms.plants.plant import Plant
from utils.utils import *


class Sosnowsky_hogweed(Plant):
    def __init__(self, game, position, strength=const.SOSNOWSKY_STRENGTH, initiative=const.PLANT_INITIATIVE, age=0):
        super().__init__(game, position, strength, initiative, age)

    def action(self):
        for organism in self._game.organisms:
            if not self.__can_kill(organism):
                continue
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    if organism.get_position() == Point(x + self._position.x, y + self._position.y):
                        self.__can_kill_and_execute(organism)
        self.sow()

    def collision_answer(self, being_in_conflict):
        if being_in_conflict is None:
            return
        if not self.__can_kill(being_in_conflict):
            self.kill()
            self._game.add_message(
                f"{self.get_organism_type()} from position self.get_position_notation() is kill by {being_in_conflict.get_organism_type()} which change his position with the aim of kill\n")
            return
        being_in_conflict.kill()
        self._game.add_message(f"{being_in_conflict.get_organism_type()} is kill by {self.get_organism_type()}\n")

    def create_new_one(self, position_for_new):
        return Sosnowsky_hogweed(self._game, position_for_new, )

    def get_organism_type(self):
        return "SOSNOWSKY"

    def get_color(self):
        return "#F2F2F2"

    def __can_kill(self, being_in_conflict):
        if isinstance(being_in_conflict, cyber.Cyber):
            return False
        return True

    def __can_kill_and_execute(self, being_in_conflict):
        if not isinstance(being_in_conflict, Animal):
            return
        if not self.__can_kill(being_in_conflict):
            return
        being_in_conflict.kill()
        self._game.add_message(f"{being_in_conflict.get_organism_type()} is kill by {self.get_organism_type()} \n")
