from abc import ABC, abstractmethod

import game as gm
from utils.utils import *


class Organism(ABC):
    def __init__(self, game, position, strength, initiative, age=0):
        assert isinstance(game, gm.Game)
        assert position.x >= 0
        assert position.y >= 0
        self._age = age
        self._is_alive = True
        self._position = position
        self._strength = strength
        self._initiative = initiative
        self._game = game

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self):
        pass

    @abstractmethod
    def collision_answer(self, being_in_conflict):
        pass

    @abstractmethod
    def get_organism_type(self):
        pass

    @abstractmethod
    def get_color(self):
        pass

    @abstractmethod
    def create_new_one(self, position_for_new):
        pass

    def get_is_alive(self):
        return self._is_alive

    def kill(self):
        self._is_alive = False

    def set_strength(self, strength):
        self._strength = strength

    def get_strength(self):
        return self._strength

    def get_initiative(self):
        return self._initiative

    def get_age(self):
        return self._age

    def increase_age(self):
        self._age += 1

    def get_position(self):
        return self._position

    def get_position_notation(self):
        return f"({self._position.x}, {self._position.y})"

    def is_on_board(self, position):
        return self._game.get_width() > position.x >= Const.CORD_ORIGIN and self._game.get_height() > position.y >= Const.CORD_ORIGIN

    def _random_neighbor(self, move_on_empty_field, shift):
        free_positions = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                check = Point(x * shift + self._position.x, y * shift + self._position.y)
                if self.is_on_board(check):
                    if move_on_empty_field:
                        if self._is_free(check):
                            free_positions.append(check)
                    else:
                        free_positions.append(check)
        if len(free_positions) == 0:
            return Point(Const.ERROR, Const.ERROR)
        random_choice = random.randint(0, len(free_positions))
        for freePosition in free_positions:
            if random_choice == 0:
                return freePosition
            else:
                random_choice -= 1
        return Point(Const.ERROR, Const.ERROR)

    def _is_free(self, position):
        for organism in self._game.organisms:
            if position == organism.get_position():
                return False
        for organism in self._game.updated_organisms:
            if position == organism.get_position():
                return False
        return True

    def _collision_with(self):
        for organism in self._game.organisms:
            if organism == self:
                continue
            if self._position == organism.get_position():
                if organism.get_is_alive():
                    return organism
        return None
