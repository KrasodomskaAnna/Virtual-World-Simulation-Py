from organisms.animals.animal import Animal


class Antelope(Animal):
    from utils.utils import const

    def __init__(self, game, position, strength=const.ANTELOPE_STRENGTH, initiative=const.ANTELOPE_INITIATIVE, age=0):
        super().__init__(game, position, strength, initiative, age)

    def create_new_one(self, position_for_new):
        return Antelope(self._game, position_for_new, )

    def is_the_same_specie(self, being_in_conflict):
        return isinstance(being_in_conflict, Antelope)

    def get_organism_type(self):
        return "ANTELOPE"

    def get_color(self):
        return "#734A32"

    def _get_step(self):
        from utils.utils import const
        return const.ANTELOPE_STEP

    def _handle_death(self, being_in_conflict):
        if not isinstance(being_in_conflict, Animal):
            if self.__escape():
                return False
        self.kill()
        return True

    def __escape(self):
        from utils.utils import const, random_choice_probability, Point
        if not random_choice_probability(const.PROBABILITY_ANTELOPE_ESCAPE):
            return False
        new_position = self._random_neighbor(True, const.NEIGHBOUR_SHIFT)
        if new_position == Point(const.ERROR, const.ERROR):
            return False
        self._swap_position(new_position)
        self._game.add_message(f"{self.get_organism_type()} runAway from attack\n")
        return True
