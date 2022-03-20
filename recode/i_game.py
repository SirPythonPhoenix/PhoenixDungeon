import i_data as data
import shutil
import os
import ctypes
import msvcrt
import subprocess
from ctypes import wintypes
import pd_sequence as color
import time
import random
from pd_sequence import bold, underline, reverse

class Player:
    def __init__(self):
        # player
        self.ausdauer = None
        self.intelligenz = None
        self.aufmerksamkeit = None
        self.handelsfahigkeit = None
        self.xp = None
        self.name = None

        # current
        self.location = None
        self.gold = None
        self.level = None
        self.inventory = None
        self.slots = None
        self.health = None
        self.poison_left = None
        self.bleed_left = None
        self.poison_current_dmg = None
        self.bleed_current_dmg = None
        self.stun_left = None

    def create(self, name):
        self.name = name
        self.ausdauer = 100
        self.intelligenz = 0
        self.aufmerksamkeit = 30
        self.handelsfahigkeit = 0
        self.xp = 0
        self.level = 1

        self.location = 0
        self.inventory = []
        self.slots = {
            "helm": None,
            "harnisch": None,
            "beinschutz": None,
            "schuhe": None,
            "rucksack": None,
            "waffe": None,
            "sekundär": None,
        }

        self.health = self.max_health
        self.poison_left = 0
        self.bleed_left = 0
        self.poison_current_dmg = 0
        self.bleed_current_dmg = 0
        self.stun_left = 0

    @property
    def speed(self):
        stat = 0
        for k, v in self.slots.items():
            if v is not None:
                stat += v.speed
        return stat

    @property
    def max_health(self):
        stat = data.Scaling.max_health(self.level)
        for k, v in self.slots.items():
            if v is not None:
                stat += v.max_health
        return stat

    @property
    def acc(self):
        stat = data.Scaling.acc()
        for k, v in self.slots.items():
            if v is not None:
                stat += v.acc
        return stat
    
    @property
    def regen(self):
        stat = 0
        for k, v in self.slots.items():
            if v is not None:
                stat += v.acc
        return stat
    
    @property
    def prot(self):
        stat = 0
        for k, v in self.slots.items():
            if v is not None:
                stat += v.acc
        return stat
    
    @property
    def dodge(self):
        stat = 0
        for k, v in self.slots.items():
            if v is not None:
                stat += v.acc
        return stat
    
    @property
    def bleed_res(self):
        stat = 0
        for k, v in self.slots.items():
            if v is not None:
                stat += v.acc
        return stat
    
    @property
    def poison_res(self):
        stat = 0
        for k, v in self.slots.items():
            if v is not None:
                stat += v.acc
        return stat
    
    @property
    def stun_res(self):
        stat = 0
        for k, v in self.slots.items():
            if v is not None:
                stat += v.acc
        return stat
    
    @property
    def block_chance(self):
        stat = 0
        for k, v in self.slots.items():
            if v is not None:
                stat += v.acc
        return stat
    
    @property
    def block_red(self):
        stat = 0
        for k, v in self.slots.items():
            if v is not None:
                stat += v.acc
        return stat
    
    @property
    def dmg(self):
        stat = 0
        for k, v in self.slots.items():
            if v is not None:
                stat += v.acc
        return stat
    
    @property
    def crit_dmg(self):
        stat = 0
        for k, v in self.slots.items():
            if v is not None:
                stat += v.acc
        return stat
    
    @property
    def bleed_dmg(self):
        stat = 0
        for k, v in self.slots.items():
            if v is not None:
                stat += v.acc
        return stat
    
    @property
    def poison_dmg(self):
        stat = 0
        for k, v in self.slots.items():
            if v is not None:
                stat += v.acc
        return stat
    
    @property
    def penetration(self):
        stat = 0
        for k, v in self.slots.items():
            if v is not None:
                stat += v.acc
        return stat
    
    @property
    def crit_chance(self):
        stat = 0
        for k, v in self.slots.items():
            if v is not None:
                stat += v.acc
        return stat
    
    @property
    def targets(self):
        stat = 0
        for k, v in self.slots.items():
            if v is not None:
                stat += v.acc
        return stat
    
    @property
    def lifesteal(self):
        stat = 0
        for k, v in self.slots.items():
            if v is not None:
                stat += v.acc
        return stat
    
    @property
    def bleed_chance(self):
        stat = 0
        for k, v in self.slots.items():
            if v is not None:
                stat += v.acc
        return stat
    
    @property
    def poison_chance(self):
        stat = 0
        for k, v in self.slots.items():
            if v is not None:
                stat += v.acc
        return stat
    
    @property
    def stun_chance(self):
        stat = 0
        for k, v in self.slots.items():
            if v is not None:
                stat += v.acc
        return stat


class Mob:
    def __init__(self):
        # current
        self.name = None
        self.health = None
        self.poison_left = None
        self.bleed_left = None
        self.poison_current_dmg = None
        self.bleed_current_dmg = None
        self.stun_left = None

        # defense
        self.max_health = None
        self.regen = None
        self.prot = None
        self.dodge = None
        self.bleed_res = None
        self.poison_res = None
        self.stun_res = None
        self.block_chance = None
        self.block_red = None

        # attacks
        self.dmg = None
        self.crit_dmg = None
        self.bleed_dmg = None
        self.poison_dmg = None
        self.durchbruch = None
        self.crit_chance = None
        self.targets = None
        self.acc = None
        self.lifesteal = None
        self.bleed_chance = None
        self.poison_chance = None
        self.stun_chance = None

    def gen(self):
        self.name = random.choice(data.MOBS)


class Item:
    def __init__(self):
        self.max_health = None
        self.regen = None
        self.prot = None
        self.dodge = None
        self.bleed_res = None
        self.poison_res = None
        self.stun_res = None
        self.block_chance = None
        self.block_red = None

        self.dmg = None
        self.crit_dmg = None
        self.bleed_dmg = None
        self.poison_dmg = None
        self.durchbruch = None
        self.crit_chance = None
        self.targets = None
        self.acc = None
        self.lifesteal = None
        self.bleed_chance = None
        self.poison_chance = None
        self.stun_chance = None


class Location:
    def __init__(self):
        pass


class Field(Location):
    def __init__(self):
        self.neighboring = None
        self.name = None

    def gen(self, neighboring):
        self.neighboring = list([neighboring])
        self.name = random.choice(data.LOCATION_FIELD)


class Town(Location):
    def __init__(self):
        pass

    def gen(self):
        pass


class Dungeon(Location):
    def __init__(self):
        self.neighboring = None
        self.level = None
        self.etagen = None

    def gen(self, level, neighboring):
        self.neighboring = list([neighboring])
        self.level = level
        self.etagen = []
        self.name = data.gen_dung_name()

        factor = round((level + 6)/10)
        etage = []
        if level == 1:
            etage.append({
                "event": "fight",
                "mobs": [

                ]
            })
            etage.append({
                "event": "trap",
                "trap": ""
            })
            etage.append({
                "event": "fight",
                "mobs": [

                ]
            })
        else:
            for i in range(0, random.randint(5, 7*factor)):
                r = random.randint(1, 100)
                if 1 <= r <= 50:
                    etage.append({
                        "event": "fight"
                    })
                if 51 <= r <= 65:
                    etage.append({
                        "event": "trap"
                    })
                if 66 <= r <= 79:
                    etage.append({
                        "event": "loot"
                    })
                if 80 <= r <= 89:
                    etage.append({
                        "event": "blocked"
                    })
                if 90 <= r <= 94:
                    etage.append({
                        "event": "trader"
                    })
                if 95 <= r <= 100:
                    etage.append({
                        "event": "secret"
                    })


class Game:
    def __init__(self):
        self.players = None
        self.locations = None
        self.printed = None
        self.settings = None
        self.mode = None
        self.insert = None

    def maximize(self, lines=None):
        kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
        user32 = ctypes.WinDLL('user32', use_last_error=True)

        SW_MAXIMIZE = 3

        kernel32.GetConsoleWindow.restype = wintypes.HWND
        kernel32.GetLargestConsoleWindowSize.restype = wintypes._COORD
        kernel32.GetLargestConsoleWindowSize.argtypes = (wintypes.HANDLE,)
        user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)

        fd = os.open('CONOUT$', os.O_RDWR)
        try:
            hCon = msvcrt.get_osfhandle(fd)
            max_size = kernel32.GetLargestConsoleWindowSize(hCon)
            if max_size.X == 0 and max_size.Y == 0:
                raise ctypes.WinError(ctypes.get_last_error())
        finally:
            os.close(fd)
        cols = max_size.X
        hWnd = kernel32.GetConsoleWindow()
        if cols and hWnd:
            if lines is None:
                lines = max_size.Y
            else:
                lines = max(min(lines, 9999), max_size.Y)
            subprocess.check_call('mode.com con cols={} lines={}'.format(
                cols, lines))
            user32.ShowWindow(hWnd, SW_MAXIMIZE)
    
    @property
    def p(self):
        return self.settings["prefix"]
    
    def new_game(self, username):
        self.insert = ""
        self.settings = {
            "colored_messages": True,
            "help_messages": True,
            "use_input": True,
            "prefix": ".",
        }
        self.printed = [None for _ in range(0, 11)]
        self.add_player(Player())
        self.player.create(username)
        self.player.location = 0
        self.add_location(Field())
        self.locations[-1].gen(neighboring=1)
        self.add_location(Dungeon())
        self.locations[-1].gen(neighboring=0, level=self.player.level)
        self.out("Spiel", f"Du wachst bei {underline(self.location.name)} auf. "
                          f"Als du dich umschaust, entdeckst du den Dungeon {underline(self.locations[self.location.neighboring[0]].name)}.")
        self.out("Hilfe", f"Du kannst den Befehl '{self.p}enter DUNGEON' benutzen, um den entsprechenden Dungeon zu betreten.", color.ANSI_BRIGHT_MAGENTA)
        self.input_loop()

    def add_player(self, player):
        if self.players is None:
            self.players = []
        self.players.append(player)

    def clear_players(self):
        self.players = None

    def remove_player(self, player):
        self.players.remove(player)

    def input_loop(self):
        while True:
            self.insert = ""
            while True:
                self.frame()
                if self.settings["use_input"] is True:
                    self.insert = input("    => ")
                    break
                else:
                    c = msvcrt.getwch()
                    if c == '\r' or c == '\n':
                        break
                    if c == '\003':
                        raise KeyboardInterrupt
                    if c == '\b':
                        self.insert = self.insert[:-1]
                    else:
                        self.insert += c
            if self.insert.startswith(self.p):
                try:
                    getattr(self, "cmd_" + self.insert.split(" ")[0][1:])(" ".join(self.insert.split(" ")[1:]) if len(self.insert.split(" ")) >= 2 else "")
                except AttributeError:
                    self.out("Fehler", "Dieser Befehl existiert nicht.", color.ANSI_BRIGHT_RED)
            elif self.insert == "":
                pass
            else:
                self.out(self.player.name, self.insert)

    def cmd_test(self, text):
        pass

    def cmd_say(self, text):
        self.out(self.player.name, text)

    def cmd_flag(self, text):
        if len(text.split(" ")) <= 1 or text in ["", " "]:
            self.out("Fehler", "Zu wenig Argumente.", color.ANSI_BRIGHT_RED)
            return
        flag = text.split(" ")[0]
        value = text.split(" ")[1]
        if flag in self.settings:
            if type(self.settings[flag]) is bool:
                if value == "True":
                    value = True
                elif value == "False":
                    value = False
                else:
                    self.out("Fehler", "Operator muss bool sein.", color.ANSI_BRIGHT_RED)
                    return
            self.out("Info", f"Flag {underline(flag)} wird von {underline(str(self.settings[flag]))} auf {underline(str(value))} gesetzt.")
            self.settings[flag] = value
    def test_func(self):
        print("worked")

    @property
    def player(self):
        return self.players[0]

    @property
    def location(self):
        return self.locations[self.player.location]

    def add_location(self, location):
        if self.locations is None:
            self.locations = []
        self.locations.append(location)

    def out(self, author, text, tc=None):
        if tc is None:
            tc = color.ANSI_RESET
        print_ = f"{tc}[{author}] {text}{color.ANSI_RESET}"
        self.printed.pop(0)
        self.printed.append(print_)

    def frame(self):
        if self.players is not None:
            columns, lines = shutil.get_terminal_size()
            os.system('cls')
            print()

            # item display
            items = []
            longest = 0
            for e in list(self.player.slots): # named items
                if self.player.slots[e] is not None:
                    item = f"{str(e).capitalize()}: {self.player.slots[e].fullname}"
                else:
                    item = f"{str(e).capitalize()}: -"
                items.append(item)
                longest = len(item) if len(item) > longest else longest
            items = ["    ║ " + e + " " * (longest - len(e)) + " ║" for i, e in enumerate(items)]
            item_disp = ""
            item_disp += "    ╔" + "═" * (longest + 2) + "╗\n"
            for e in items:
                item_disp += e + "\n"
            item_disp += "    ╚" + "═" * (longest + 2) + "╝\n"
            print(item_disp)

            # printed game text display
            print_pre_disp = []
            for e in self.printed:
                if e is not None:
                    if self.settings["colored_messages"] is False:
                        for code in color.ANSI_ALL:
                            e = e.replace(code, "")
                    e_shortened = e
                    for code in color.ANSI_ALL:
                        e_shortened = e_shortened.replace(code, "")
                    if len(e_shortened) > columns - 12:
                        auth_shortened = e.split(" ")[0]
                        for code in color.ANSI_ALL:
                            auth_shortened = auth_shortened.replace(code, "")
                        auth_len = len(auth_shortened) + 1
                        parts = []
                        e_snippet = e
                        last_color = ""
                        make_pre = False
                        counter = 0
                        while e_snippet != "":
                            in_counter = 0
                            prev_last = last_color
                            while counter < columns - 12 and in_counter < len(e_snippet):
                                if e_snippet[in_counter:(in_counter + 6)].startswith("""\u001b["""):
                                    prev = in_counter
                                    while e_snippet[in_counter] != "m":
                                        in_counter += 1
                                    in_counter += 1 # Fehler bei kleiner Konsole
                                    last_color = e_snippet[prev:in_counter]
                                else:
                                    in_counter += 1
                                    counter += 1
                            add = " " * auth_len if make_pre else ""
                            parts.append(add + prev_last + e_snippet[:in_counter] + color.ANSI_RESET)
                            e_snippet = e_snippet[in_counter:]
                            if e_snippet.startswith(" "):
                                e_snippet = e_snippet[1:]
                            make_pre = True
                            counter = auth_len

                        for p in parts:
                            p_shortened = p
                            for code in color.ANSI_ALL:
                                p_shortened = p_shortened.replace(code, "")
                            print_pre_disp.append(p + " " * (columns - 12 - len(p_shortened)))
                        print_pre_disp.append(" " * (columns - 12))
                    else:
                        print_pre_disp.append(e + " " * (columns - 12 - len(e_shortened)))
                        print_pre_disp.append(" " * (columns - 12))
            print_pre_disp = ["    ║ " + e + " ║" for i, e in enumerate(print_pre_disp)]
            print_disp = ""
            print_disp += "    ╔" + "═" * (columns - 10) + "╗\n"
            for e in print_pre_disp:
                print_disp += e + "\n"
            print_disp += "    ╠" + "═" * (columns - 10) + "╣\n"
            print_disp += "    ║ " + self.insert + " " * (columns - 12 - len(self.insert)) + " ║\n"
            print_disp += "    ╚" + "═" * (columns - 10) + "╝\n"
            print(print_disp, end="")
