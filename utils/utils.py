import random


def random_choice_probability(probability):
    return random.randint(0, 100) <= probability * 100


def random_position(width, height):
    x = random.randint(0, width)
    y = random.randint(0, height)
    return Point(x, y)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def assign(self, other):
        self.x = other.x
        self.y = other.y


class Const:
    DEFAULT_ORGANISM_TRAIT = -1
    NEIGHBOUR_SHIFT = 1
    CORD_ORIGIN = 0
    ERROR = -1

    PROBABILITY_SOW = 1.0 / 2.0
    TRY_DANDELION_TO_SOW_NUMBER = 3
    GUARANA_INCREASE_STRENGTH_WHO_EAT = 3

    PLANT_STRENGTH = 0
    NIGHTSHADE_STRENGTH = 99
    SOSNOWSKY_STRENGTH = 10

    HUMAN_STRENGTH = 5
    WOLF_STRENGTH = 9
    LAMP_STRENGTH = 4
    FOX_STRENGTH = 3
    TURTLE_STRENGTH = 2
    ANTELOPE_STRENGTH = 4
    CYBER_LAMP_STRENGTH = 11

    PLANT_INITIATIVE = 0

    HUMAN_INITIATIVE = 4
    WOLF_INITIATIVE = 5
    LAMP_INITIATIVE = 4
    FOX_INITIATIVE = 7
    TURTLE_INITIATIVE = 1
    ANTELOPE_INITIATIVE = 4
    CYBER_LAMP_INITIATIVE = 4

    HUMAN_STEP = 1
    WOLF_STEP = 1
    LAMP_STEP = 1
    FOX_STEP = 1
    TURTLE_STEP = 1
    ANTELOPE_STEP = 2
    CYBER_LAMP_STEP = 1

    PROBABILITY_TURTLE_MOVE = 3.0 / 4.0
    STRENGTH_REPEL_ATTACK_TURTLE = 5
    PROBABILITY_ANTELOPE_ESCAPE = 1.0 / 2.0

    ALZUR_SHIELD_DURATION = 5
    ALZUR_SHIELD_DURATION_SET = ALZUR_SHIELD_DURATION + 1
    ALZUR_SHIELD_LOCK = 5

    ANTELOPE_PERCENT = 2
    CYBER_LAMP_PERCENT = 2
    FOX_PERCENT = 2
    LAMP_PERCENT = 2
    TURTLE_PERCENT = 2
    WOLF_PERCENT = 2
    DANDELION_PERCENT = 2
    GRASS_PERCENT = 2
    GUARANA_PERCENT = 2
    NIGHTSHADE_PERCENT = 2
    SOSNOWSKY_PERCENT = 2


const = Const()
