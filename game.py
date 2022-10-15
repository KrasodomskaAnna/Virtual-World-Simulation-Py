


class Game:
    def __init__(self, graphics):
        self.organisms = []
        self.updated_organisms = []
        self.__width = 0
        self.__height = 0
        self.__alzurShield = 0  # Alzur Shield -> if is 0 it can be use, if is + for this number of turns will be active, if is - for this number of turns can't be use
        self.__turnsNumber = 0
        self.__messages = None
        self.__warnings = None
        self.__input = "-"
        self.graphics = graphics

    def next_turn(self):
        self.__messages = ""
        self.__warnings = ""
        self.organisms.sort(key=lambda x: (x.get_initiative(), x.get_age()))

        for organism in self.organisms:
            if not organism.get_is_alive():
                return
            organism.action()
            organism.collision()

        for organism in self.organisms:
            if organism.get_is_alive():
                organism.increase_age()
                self.updated_organisms.append(organism)

        self.organisms.clear()
        self.organisms.extend(self.updated_organisms)
        self.updated_organisms.clear()

        if len(self.organisms) == 1:
            self.end_game("You stay alone")

        from utils.utils import const
        if self.__alzurShield == 1:
            self.__alzurShield = -const.ALZUR_SHIELD_LOCK
        elif self.__alzurShield < 0:
            self.__alzurShield += 1
        elif self.__alzurShield > 0:
            self.__alzurShield -= 1
        self.__turnsNumber += 1

    def is_alzur_shield_active(self):
        return self.__alzurShield > 0

    def activate_azur_shield(self):
        if self.__alzurShield != 0:
            return False
        from utils.utils import const
        self.__alzurShield = const.ALZUR_SHIELD_DURATION_SET
        return True

    def end_game(self, report):
        # graphics1.endGame(report)
        self.graphics.add_end_game_window(report)

    def change_graphics(self, new_graphics):
        self.graphics = new_graphics

    def get_input(self):
        return self.__input

    def set_input(self, input):
        self.__input = input

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_azur_shield(self):
        return self.__alzurShield

    def set_azur_shield(self, value):
        self.__alzurShield = value

    def set_bg_dimensions(self, width, height):
        self.__width = width
        self.__height = height
        # graphics1.setBoardDimensions(width, height)

    def get_turns_number(self):
        return self.__turnsNumber

    def set_turns_number(self, turns_number):
        self.__turnsNumber = turns_number

    def get_messages(self):
        return self.__messages

    def get_warnings(self):
        return self.__warnings

    def add_message(self, message):
        self.__messages += message

    def add_warning(self, warning):
        self.__warnings += warning
