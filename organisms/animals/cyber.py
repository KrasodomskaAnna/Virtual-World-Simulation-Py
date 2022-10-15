import math
from math import fabs

from coordinates import Coordinate

import organisms.plants.sosnowsky_hogweed as sos_hog
from organisms.animals.animal import Animal
from utils.utils import *


class Cyber(Animal):
    def __init__(self, game, position, strength=const.CYBER_LAMP_STRENGTH, initiative=const.CYBER_LAMP_INITIATIVE,
                 age=0):
        super().__init__(game, position, strength, initiative, age)

    def action(self):
        nearest_sosnowsky = None
        for organism in self._game.organisms:
            if isinstance(organism, sos_hog.Sosnowsky_hogweed):
                if nearest_sosnowsky is None:
                    nearest_sosnowsky = organism
                elif self.__is_further(nearest_sosnowsky, organism):
                    nearest_sosnowsky = organism
        if nearest_sosnowsky is None:
            self._move()
        else:
            self.__move_to(nearest_sosnowsky.get_position())

    def __move_to(self, point):
        x_dist = fabs(self.get_position().x - point.x)
        y_dist = fabs(self.get_position().y - point.y)
        if x_dist >= y_dist:
            change_xy = 0
        else:
            change_xy = 1

        change_direct_x = -1
        if point.x * self.get_position().x >= 0:  # if point is on the same half of coordinate system
            change_direct_x = (1 if point.x > self.get_position().x else -1)
        elif point.x >= 0:
            change_direct_x = 1

        change_direct_y = -1
        if point.y * self.get_position().y >= 0:  # if point is on the same half of coordinate system
            change_direct_y = (1 if point.y > self.get_position().y else -1)
        elif point.y >= 0:
            change_direct_y = 1

        new_pos_x = self.get_position().x
        new_pos_y = self.get_position().y
        if x_dist >= y_dist:
            change_direct_y = 0
        else:
            change_direct_x = 0
        new_pos_x += change_direct_x
        new_pos_y += change_direct_y
        self._move_to_position(Coordinate(x=new_pos_x, y=new_pos_y))

    def __is_further(self, first, second):
        if self.__get_distance(first) > self.__get_distance(second):
            return True
        else:
            return False

    def __get_distance(self, other):
        x = other.get_position().x
        y = other.get_position().y
        x_dist = fabs(self.get_position().x - x)
        y_dist = fabs(self.get_position().y - y)
        return math.sqrt(pow(x_dist, 2) + pow(y_dist, 2))

    def create_new_one(self, position_for_new):
        return Cyber(self._game, position_for_new, )

    def is_the_same_specie(self, being_in_conflict):
        return isinstance(being_in_conflict, Cyber)

    def get_organism_type(self):
        return "CYBER"

    def get_color(self):
        return "#A68863"

    def _get_step(self):
        return Const.LAMP_STEP
