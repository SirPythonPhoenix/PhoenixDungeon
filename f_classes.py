import f_textgenerator as gen
from f_textgenerator import error, attention, tut, high, bold
import random
import pd_stats as stats
import pd_sequence as sequence
import pd_text as text


class Player:

    def __init__(self, name, location, **kwargs):
        self.help_mode = True
        self.name = name
        if "level" in list(kwargs):
            self.level = int(kwargs["level"])
        else:
            self.level = 1
        self.calc_stats()

        self.location = location
        self.gold = 0
        self.health = stats.PLAYER_BASE_STATS["health"]
        self.inventory = {}
        self.bleed = {
            "damage": 0,
            "left": 0,
        }
        self.poison = {
            "damage": 0,
            "left": 0,
        }

        self.xp = 0
        self.equipped = {
            "weapon": None,
            "helmet": None,
            "chest": None,
            "legs": None,
            "boots": None,
        }
        self.inventory = []

    def calc_stats(self):
        self.max_health = stats.PLAYER_BASE_STATS["health"]
        self.armor = stats.PLAYER_BASE_STATS["armor"]
        self.dodge = stats.PLAYER_BASE_STATS["dodge"]
        self.dmg = stats.PLAYER_BASE_STATS["dmg"]
        self.acc = stats.PLAYER_BASE_STATS["acc"]
        self.crit = stats.PLAYER_BASE_STATS["crit"]
        self.ls = stats.PLAYER_BASE_STATS["ls"]

        for i in range(1, int(self.level)):
            self.max_health += round(stats.PLAYER_BASE_STAT_INCREASE["health"] * i/2)
            self.dmg += round(stats.PLAYER_BASE_STAT_INCREASE["dmg"] * i/16)
            self.acc += round(stats.PLAYER_BASE_STAT_INCREASE["acc"])
            self.dodge += round(stats.PLAYER_BASE_STAT_INCREASE["dodge"])
            self.crit += round(stats.PLAYER_BASE_STAT_INCREASE["crit"])

    def trap(self, trap):
        pass

    def attack(self, cmd, mobs):
        mob_list = []
        for e in mobs:
            mob_list.append(e.typ)
        if cmd == ".attack":
            cmd = ".attack " + mob_list[0]
        if len(cmd.split(" ")) == 2 and cmd.split(" ")[1] in mob_list:
            mob = mobs[mob_list.index(cmd.split(" ")[1])]
            if random.randint(1, 100) in range(1, self.acc - mob.dodge + 1):
                damage = self.dmg - mob.armor
                mob.health -= damage
                if mob.health <= 0:
                    left_message = gen.pron_gender(mob.gender, 0) + ' ' + sequence.ANSI_BLUE + mob.typ + sequence.ANSI_RESET + ' wurde ' + text.DEATH[random.randint(1, len(text.DEATH)) - 1] + '.'
                else:
                    left_message = gen.pron_gender(mob.gender, 0) + ' ' + sequence.ANSI_BLUE + mob.typ + sequence.ANSI_RESET + ' hat noch ' + str(mob.health) + ' Lebenspunkte.'
                print(gen.game('Du greifst {} an.'.format(
                    gen.pron_gender(mob.gender, 4) + " " +
                    sequence.ANSI_BLUE + mob.typ + sequence.ANSI_RESET) +
                    '\n' + sequence.ANSI_BRIGHT_RED + f' - {damage} health ' +
                    sequence.ANSI_RESET + f'| {left_message}'
                ))
                if mob.health <= 0:
                    mobs.remove(mob)
                    return mobs
            else:
                print(gen.game('Du verfehlst {}.'.format(
                    gen.pron_gender(mob.gender, 4) + " " +
                    sequence.ANSI_BLUE + mob.typ + sequence.ANSI_RESET)))
            for i, e in enumerate(mob_list):
                mob = mobs[i]

                if random.randint(1, 100) in range(1, mob.acc - self.dodge + 1):
                    damage = mob.dmg - self.armor
                    self.health -= damage
                    right_message = "trifft"
                    if self.health <= 0:
                        left_message = 'Du wurdest ' + text.DEATH[random.randint(1, len(text.DEATH)) - 1] + '.'
                    else:
                        left_message = 'Du hast noch ' + str(self.health) + ' Lebenspunkte.'

                else:
                    right_message = "verfehlt"
                print(
                    '\n        ' + gen.pron_gender(mob.gender, 0).capitalize() + ' ' + sequence.ANSI_BLUE + mob.typ + sequence.ANSI_RESET + " greift an und {}.".format(right_message))
                if right_message == "trifft":
                    print('        ' + sequence.ANSI_BRIGHT_RED + f' - {damage} health ' +
                        sequence.ANSI_RESET + f'| {left_message}')
        else:
            print(error('Mob nicht gefunden.'))
        return mobs
    def in_dungeon(self, locations):
        if locations[self.location].typ == "dungeon":
            return True
        else:
            return False

    def get_location(self, locations):
        return locations[self.location]

class Location:
    def __init__(self, typ="place", **kwargs): #kwargs: level, isnext
        if typ == "place":
            if random.randint(1, 3) == 1:
                typ = "town"
            else:
                typ = "dungeon"
        if "level" in list(kwargs):
            self.level = kwargs["level"]
        self.isnext = []
        for i in range(0, random.randint(1, 2)):
            self.isnext.append(None)
        if "isnext" in list(kwargs):
            self.isnext[0] = kwargs["isnext"]
        self.typ = typ
        if self.typ == "dungeon":
            self.etage = 0
        self.gen()

    def gen(self):
        if self.typ == "dungeon":
            self.etage += 1
            self.adjective, self.name = gen.r_dungeon_tuple(self.level)

            self.fullname = self.adjective + " " + self.name
            self.events = []
            self.event_attr = {}
            self.mobs = []

            for i in range(0, random.randint(4, 10)):
                r = random.randint(0, 100)
                if r in range(0, 60):
                    self.events.append("fight")
                elif r in range(60, 75):
                    self.events.append("trap")
                elif r in range(75, 85):
                    self.events.append("loot")
                elif r in range(85, 95):
                    self.events.append("blocked")
                elif r in range(95, 101):
                    self.events.append("secret")
        elif self.typ == "town":
            pass

        elif self.typ == "way":
            pass

        elif self.typ == "empty":
            self.name = gen.r_location_empty()
            self.fullname = self.name


class Room:

    def __init__(self):
        self.entrance = 0


class Mob:

    def __init__(self, level):
        all = gen.gen_mob(level)

        self.level = level
        self.typ = all["typ"]
        self.max_health = all["health"]
        self.armor = all["armor"]
        self.dodge = all["dodge"]
        self.dmg = all["dmg"]
        self.acc = all["acc"]
        self.crit = all["crit"]
        self.ls = all["ls"]
        self.xp = all["xp"]
        self.gender = all["gender"]

        self.health = self.max_health

    def attack(self):
        pass

    def defend(self, entity):
        pass


class Item:

    def __init__(self):
        self.tier = 0
        self.typ = 0
        self.consumable = 0
        self.material = 0
