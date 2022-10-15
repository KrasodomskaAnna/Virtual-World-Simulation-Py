import math
import pickle

from utils.utils import *
from utils.create_org import get_new_organism


class Config:
    BOARD_WIDTH = 20
    BOARD_HEIGHT = 10

    NEVER_BEFORE = 0
    HUNDRED_PERCENT = 100
    FIELDS_OCCUPIED_BY_ORGANISMS_PERCENT = 20 / HUNDRED_PERCENT

    def __init__(self, game, graphics):
        self.__game = game
        self.__graphics = graphics
        self.all_percent = 0

    def load_save(self):
        del self.__game
        with open("config/save.txt", "rb") as f:
            self.__game = pickle.load(f)
        self.__game.change_graphics(self.__graphics)
        return self.__game

    def do_save(self):
        graphics = self.__graphics
        self.__game.change_graphics(None)
        with open("config/save.txt", "wb") as f:
            pickle.dump(self.__game, f)
        self.__game.change_graphics(graphics)
        self.__graphics = graphics

    def load_game(self):
        self.__return_to_game_initial_settings()

        self.__game.set_bg_dimensions(self.BOARD_WIDTH, self.BOARD_HEIGHT)
        self.__create_organism("HUMAN", self.__get_random_free_position(), const.DEFAULT_ORGANISM_TRAIT,
                               const.DEFAULT_ORGANISM_TRAIT, self.NEVER_BEFORE)

        # self.__create_new_organisms_type("ANTELOPE", const.ANTELOPE_PERCENT)
        # self.__create_new_organisms_type("CYBER", const.CYBER_LAMP_PERCENT)
        # self.__create_new_organisms_type("FOX", const.FOX_PERCENT)
        self.__create_new_organisms_type("LAMP", const.LAMP_PERCENT)
        # self.__create_new_organisms_type("TURTLE", const.TURTLE_PERCENT)
        # self.__create_new_organisms_type("WOLF", const.WOLF_PERCENT)
        # self.__create_new_organisms_type("DANDELION", const.DANDELION_PERCENT)
        # self.__create_new_organisms_type("GRASS", const.GRASS_PERCENT)
        # self.__create_new_organisms_type("GUARANA", const.GUARANA_PERCENT)
        # self.__create_new_organisms_type("NIGHTSHADE", const.NIGHTSHADE_PERCENT)
        # self.__create_new_organisms_type("SOSNOWSKY", const.SOSNOWSKY_PERCENT)

    def __display_error(self, message):
        raise Exception("Failed to parse the config1 file: " + message)

    def __create_new_organisms_type(self, type, percent):
        self.all_percent += percent
        if self.all_percent > self.HUNDRED_PERCENT:
            self.__display_error("too many Organisms1! Please, repair config1")
        fields_number = self.__game.get_width() * self.__game.get_height()
        fields_for_organism = math.ceil(
            fields_number * self.FIELDS_OCCUPIED_BY_ORGANISMS_PERCENT * percent / self.HUNDRED_PERCENT)
        for i in range(0, fields_for_organism):
            self.__create_organism(type, self.__get_random_free_position(), const.DEFAULT_ORGANISM_TRAIT,
                                   const.DEFAULT_ORGANISM_TRAIT, self.NEVER_BEFORE)

    def __create_organism(self, type, position, strength, initiative, age):
        self.__game.organisms.append(
            get_new_organism(self.__game, type, position, strength, initiative, age))

    def __get_random_free_position(self):
        position = Point(const.ERROR, const.ERROR)
        while position == Point(const.ERROR, const.ERROR):
            random_pos = Point(const.ERROR, const.ERROR)
            random_pos.assign(random_position(self.__game.get_width(), self.__game.get_height()))
            for organism in self.__game.organisms:
                if organism.get_position() == random_pos:
                    break
            position.assign(random_pos)
        return position

    def __return_to_game_initial_settings(self):
        self.__game.set_azur_shield(self.NEVER_BEFORE)
        self.__game.set_turns_number(self.NEVER_BEFORE)
        self.all_percent = 0
        self.__game.organisms.clear()
