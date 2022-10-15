from abc import ABC, abstractmethod

from organisms.organism import Organism
from utils.utils import *


class Animal(Organism, ABC):
    def __init__(self, game, position, strength, initiative, age=0):
        super().__init__(game, position, strength, initiative, age)
        self._previous_position = position

    def action(self):
        self._move()

    def collision(self):
        being_in_conflict = self._collision_with()
        if being_in_conflict is None:
            return
        if self.is_the_same_specie(being_in_conflict):
            self._position = self._previous_position
            self._reproduce(being_in_conflict)
            return
        if being_in_conflict.get_strength() <= self._strength:
            being_in_conflict.collision_answer(self)
        else:
            if self._handle_death(being_in_conflict):
                self._game.add_message(
                    f"{self.get_organism_type()} went to position {self.get_position_notation()} so is kill by {being_in_conflict.get_organism_type()}\n")

    def collision_answer(self, being_in_conflict):
        if being_in_conflict is None:
            return
        if self._handle_death(being_in_conflict):
            self._game.add_message(
                f"{self.get_organism_type()} from position {self.get_position_notation()} is kill by {being_in_conflict.get_organism_type()} which change his position with the aim of kill\n")

    def come_back(self):
        self._position = self._previous_position

    def run_away(self):
        self.action()
        self.collision()

    @abstractmethod
    def create_new_one(self, position_for_new):
        pass

    @abstractmethod
    def is_the_same_specie(self, being_in_conflict):
        pass

    def _reproduce(self, animal_reproducing_with):
        position_for_new = self._random_neighbor(True, Const.NEIGHBOUR_SHIFT)
        if position_for_new == Point(const.ERROR, const.ERROR):
            position_for_new = animal_reproducing_with.randomNeighbor(True, const.NEIGHBOUR_SHIFT)
            if position_for_new == Point(const.ERROR, const.ERROR):
                self._game.add_warning(
                    f"Can't reproduce {self.get_organism_type()} on position {self.get_position_notation()}\n")
                return
        self._game.add_message(
            f"{self.get_organism_type()} from position {self.get_position_notation()}change position and met {animal_reproducing_with.get_organism_type()} on position {animal_reproducing_with.get_position_notation()} so they reproduce\n")
        self._game.updated_organisms.append(self.create_new_one(position_for_new))

    def _move(self):
        new_position = self._position_move()
        self._move_to_position(new_position)

    def _move_to_position(self, position):
        if position == Point(Const.ERROR, Const.ERROR):
            return
        if position == self.get_position():
            return
        self._swap_position(position)
        self._game.add_message(
            f"{self.get_organism_type()} move on a new position {self.get_position_notation()}\n")

    def _handle_death(self, being_in_conflict):
        self.kill()
        return True

    def _position_move(self):
        return self._random_neighbor(False, self._get_step())

    def _swap_position(self, new_position):
        self._previous_position = self._position
        self._position = new_position

    @abstractmethod
    def _get_step(self):
        pass
