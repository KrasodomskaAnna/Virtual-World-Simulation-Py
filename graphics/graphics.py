import tkinter
import tkinter.font as font
from tkinter import *

from PIL import ImageTk, Image

from config.config import Config
from game import Game
from utils.create_org import get_new_organism
from utils.utils import *


class Graphics:
    BOARD_DIMENTIONS = "800x450"
    MESSAGES_DIMENTIONS = "200x150"
    PHOTO_WIDTH = 476
    PHOTO_HEIGHT = 320
    UNIVERSAL_PADDING = 5
    BOARD_COLOR = "#2A3340"

    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__game = Game(self)
        self.__load_game()
        self.__window = Tk()
        self.__window.title("Animal World 188863")
        self.__window.geometry(self.BOARD_DIMENTIONS)
        self.__window.configure(background="#2A3340")
        self.__window.resizable(0, 0)
        self.__text_font = font.Font(family="Helvetica", size=10, weight="bold")
        self.__stringvar = None
        self.__frame = None
        self.__buttons = []
        self.__add_game_panel()
        self.__window.bind("<KeyPress>", self.on_pressed)
        self.__window.mainloop()

    def __load_save(self):
        config = Config(self.__game, self)
        self.__game = config.load_save()
        del config

    def __save_game(self):
        config = Config(self.__game, self)
        config.do_save()
        del config

    def __load_game(self):
        config = Config(self.__game, self)
        config.load_game()
        # self.update_board
        del config

    def __add_game_panel(self):
        self.__window.columnconfigure(0, weight=10)
        self.__window.columnconfigure(1, weight=2)
        self.__window.columnconfigure(2, weight=2)

        self.__window.rowconfigure(0, weight=2)
        self.__window.rowconfigure(1, weight=1)
        self.__window.rowconfigure(2, weight=1)
        self.__window.rowconfigure(3, weight=1)
        self.__window.rowconfigure(4, weight=1)
        self.__window.rowconfigure(5, weight=1)

        # board
        self.__frame = LabelFrame(self.__window, background="#2A3340")
        width = int(58 / self.__game.get_width())
        height = int(21 / self.__game.get_height())
        for self.__y in range(0, self.__game.get_height()):
            for self.__x in range(0, self.__game.get_width()):
                button = Button(self.__frame, bg="#733F2D", fg="#ffffff", font=self.__text_font, width=width,
                                height=height, command=self.__add_adding_organism_panel)
                self.__buttons.append(button)
                button.grid(column=self.__x, row=self.__y, rowspan=1, columnspan=1)
        self.__frame.grid(column=0, row=0, rowspan=6, sticky="news")

        # buttons
        title_font = font.Font(family="Chiller", size=30, weight="bold")
        label = Label(self.__window, text="ANIMAL WORLD", bg="#2A3340", fg="#ffffff", font=title_font)
        label.grid(column=1, row=0, columnspan=2, sticky="news", padx=self.UNIVERSAL_PADDING,
                   pady=self.UNIVERSAL_PADDING)

        label = Button(self.__window, text="LOAD CONFIG", bg="#733F2D", fg="#ffffff", font=self.__text_font,
                       command=self.__load_game)
        label.grid(column=1, row=1, sticky="news", padx=self.UNIVERSAL_PADDING, pady=self.UNIVERSAL_PADDING)

        label = Button(self.__window, text="LOAD SAVE", bg="#BF4F45", fg="#ffffff", font=self.__text_font,
                       command=self.__load_save)
        label.grid(column=2, row=1, sticky="news", padx=self.UNIVERSAL_PADDING, pady=self.UNIVERSAL_PADDING)

        label = Button(self.__window, text="SAVE GAME", bg="#BF4F45", fg="#ffffff", font=self.__text_font,
                       command=self.__save_game)
        label.grid(column=1, row=2, sticky="news", padx=self.UNIVERSAL_PADDING, pady=self.UNIVERSAL_PADDING)

        label = Button(self.__window, text="AZUR SHIELD", bg="#733F2D", fg="#ffffff", font=self.__text_font,
                       command=self.__game.activate_azur_shield)
        label.grid(column=2, row=2, sticky="news", padx=self.UNIVERSAL_PADDING, pady=self.UNIVERSAL_PADDING)

        label = Button(self.__window, text="NEXT TURN", bg="#733F2D", fg="#ffffff", font=self.__text_font,
                       command=self.__execute_next_turn)
        label.grid(column=1, row=3, sticky="news", padx=self.UNIVERSAL_PADDING, pady=self.UNIVERSAL_PADDING)

        label = Button(self.__window, text="MESSAGES", bg="#BF4F45", fg="#ffffff", font=self.__text_font,
                       command=self.__add_messages_panel)
        label.grid(column=2, row=3, sticky="news", padx=self.UNIVERSAL_PADDING, pady=self.UNIVERSAL_PADDING)

        self.__stringvar = tkinter.StringVar(self.__window, value=self.__game.get_turns_number())
        label = Label(self.__window, textvariable=self.__stringvar, bg="#2A3340", fg="#ffffff", font=self.__text_font)
        label.grid(column=1, row=4, sticky="news", columnspan=2, padx=self.UNIVERSAL_PADDING,
                   pady=self.UNIVERSAL_PADDING)

        label = Label(self.__window, text=f"warnings: \n{self.__game.get_warnings()}", bg="#2A3340", fg="#ffffff",
                      font=self.__text_font)
        label.grid(column=1, row=5, sticky="news", columnspan=2, padx=self.UNIVERSAL_PADDING,
                   pady=self.UNIVERSAL_PADDING)

    def __add_messages_panel(self):
        messages_window = Toplevel(self.__window)
        messages_window.title("Animal World 188863")
        messages_window.geometry(self.MESSAGES_DIMENTIONS)
        messages_window.configure(background="#2A3340")
        self.__window.resizable(0, 0)

        label = Label(messages_window, text=f"messages: \n{self.__game.get_messages()}", bg="#2A3340", fg="#ffffff",
                      font=self.__text_font)
        label.pack()

    def __execute_next_turn(self):
        self.__game.next_turn()
        self.__stringvar.set(f"{self.__game.get_turns_number()}")
        self.__update_board()
        self.__game.set_input("-")

    def __clear_board(self):
        children = self.__frame.winfo_children()
        for button in children:
            button.configure(bg=f"{self.BOARD_COLOR}")

    def __set_color(self, x, y, color):
        idx = y * self.__game.get_width() + x
        if idx >= self.__game.get_width() * self.__game.get_height():
            return
        self.__buttons[idx].configure(bg=color)

    def __update_board(self):
        self.__clear_board()
        for organism in self.__game.organisms:
            self.__set_color(organism.get_position().x, organism.get_position().y, organism.get_color())

    def on_pressed(self, key):
        if key.keysym == "Up":
            self.__game.set_input("UP")
        elif key.keysym == "Down":
            self.__game.set_input("DOWN")
        elif key.keysym == "Right":
            self.__game.set_input("RIGHT")
        elif key.keysym == "Left":
            self.__game.set_input("LEFT")
        self.__execute_next_turn()

    def __add_adding_organism_panel(self):
        self.add_wind = Toplevel(self.__window)
        self.add_wind.title("END")
        self.add_wind.geometry("300x100")
        self.add_wind.configure(background="#2A3340")

        self.__org_table = ["ANTELOPE", "CYBER", "FOX", "LAMP", "TURTLE", "WOLF", "DANDELION", "GRASS",
                            "GUARANA", "NIGHTSHADE", "SOSNOWSKY"]
        self.__i = 0
        self.__org_type = tkinter.StringVar(self.add_wind, value=self.__org_table[self.__i])
        label = Label(self.__window, text=f"type{self.__org_type}", bg="#2A3340", fg="#ffffff", font=self.__text_font)
        label.grid(column=0, row=0, columnspan=2, sticky="news", padx=self.UNIVERSAL_PADDING,
                   pady=self.UNIVERSAL_PADDING)
        label = Button(self.add_wind, text="ACCEPT", bg="#BF4F45", fg="#ffffff", font=self.__text_font,
                       command=self.__append_organism)
        label.grid(column=0, row=1, sticky="news", padx=self.UNIVERSAL_PADDING, pady=self.UNIVERSAL_PADDING)
        label = Button(self.add_wind, text="NEXT", bg="#BF4F45", fg="#ffffff", font=self.__text_font,
                       command=self.__next_organism)
        label.grid(column=1, row=1, sticky="news", padx=self.UNIVERSAL_PADDING, pady=self.UNIVERSAL_PADDING)

    def __next_organism(self):
        self.__i += 1
        if self.__i > 10:
            self.__i = 0
        self.__stringvar.set(self.__org_table[self.__i])

    def __append_organism(self):
        org_type = self.__org_table[self.__i]
        self.__game.updated_organisms.append(
            get_new_organism(self.__game, org_type, Point(self.__x, self.__y), const.DEFAULT_ORGANISM_TRAIT,
                             const.DEFAULT_ORGANISM_TRAIT, 0))

    def add_end_game_window(self, report):
        end_wind = Toplevel(self.__window)
        end_wind.title("END")
        end_wind.geometry("300x100")
        end_wind.configure(background="#2A3340")

        title_font = font.Font(family="Chiller", size=30, weight="bold")
        label = Label(end_wind, text="ANIMAL WORLD", bg="#2A3340", fg="#ffffff", font=title_font)
        label.pack()

        title_font = font.Font(family="Chiller", size=20, weight="bold")
        label = Label(end_wind, text=report, bg="#2A3340", fg="#ffffff", font=title_font)
        label.pack()

        img = Image.open("graphics/pexels-pixabay-247431.jpg")
        img = img.resize((self.PHOTO_WIDTH, self.PHOTO_HEIGHT), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(img)

        lab = tkinter.Label(image=test)
        lab.image = test
        lab.place(x=100, y=100)
