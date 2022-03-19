import pd_text as text
import random
import pd_sequence as sequence
import pd_stats as stats


def r_location_empty():
    return list(text.LOCATION_EMPTY)[random.randint(0, len(text.LOCATION_EMPTY) - 1)]


def r_dungeon_easy():
    return list(text.LOCATION_DUNGEON_EASY)[random.randint(0, len(text.LOCATION_DUNGEON_EASY) - 1)]


def r_dungeon_middle():
    return list(text.LOCATION_DUNGEON_MIDDLE)[random.randint(0, len(text.LOCATION_DUNGEON_MIDDLE) - 1)]


def r_dungeon_hard():
    return list(text.LOCATION_DUNGEON_HARD)[random.randint(0, len(text.LOCATION_DUNGEON_HARD) - 1)]


def pron_gender(gender, index):
    if gender == "M":
        return text.GENDER_M[index]
    elif gender == "F":
        return text.GENDER_F[index]
    elif gender == "N":
        return text.GENDER_N[index]


def dungeon_adjective(level):
    if level == 100:
        return text.LOCATION_DUNGEON_ADJECTIVE[100]
    for e in list(text.LOCATION_DUNGEON_ADJECTIVE):
        if e <= level <= e + 9:
            return text.LOCATION_DUNGEON_ADJECTIVE[e]


def adjective_gender(word, gender):
    if gender == "M":
        return word + "er"
    elif gender == "F":
        return word + "e"
    elif gender == "N":
        return word + "es"


def r_dungeon_tuple(level):
    adj = dungeon_adjective(level)
    if level < 31:
        noun = r_dungeon_easy()
        gen = text.LOCATION_DUNGEON_EASY[noun]
    elif level >= 81:
        noun = r_dungeon_hard()
        gen = text.LOCATION_DUNGEON_HARD[noun]
    else:
        noun = r_dungeon_middle()
        gen = text.LOCATION_DUNGEON_MIDDLE[noun]
    return adjective_gender(adj, gen), noun


def dungeon_gender(name):
    if name in text.LOCATION_DUNGEON_EASY:
        return text.LOCATION_DUNGEON_EASY[name]
    elif name in text.LOCATION_DUNGEON_MIDDLE:
        return text.LOCATION_DUNGEON_MIDDLE[name]
    elif name in text.LOCATION_DUNGEON_HARD:
        return text.LOCATION_DUNGEON_HARD[name]


def error(msg):
    return sequence.ANSI_RED + "\n[Fehler] {}".format(msg) + sequence.ANSI_RESET


def bold(msg):
    return sequence.ANSI_BOLD + msg + sequence.ANSI_RESET


def attention(msg):
    return sequence.ANSI_YELLOW + "\n[Achtung] {}".format(msg) + sequence.ANSI_RESET


def high(msg):
    return sequence.ANSI_BLUE + "{}".format(msg) + sequence.ANSI_RESET


def tut(msg, player):
    if player.help_mode:
        print("\n" + sequence.ANSI_MAGENTA + "[Hilfe] {}".format(msg).replace("\n", "\n        ") + sequence.ANSI_RESET)
        return True
    else:
        return False


def game(msg):
    return "\n" + "[Spiel] {}".format(msg).replace("\n", "\n        ")


def dungeon_find(name):
    return text.MOVE[random.randint(1, len(text.MOVE)) - 1] + text.SCOUT[random.randint(1, len(text.SCOUT)) - 1] + name


def dungeon_find_trap(name):
    return text.MOVE[random.randint(1, len(text.MOVE)) - 1] + \
           text.TRAP_ACTIVATE[random.randint(1, len(text.TRAP_ACTIVATE)) - 1].format(name)


def dungeon_mobs(mobs):
    return_string = ""
    for i, e in enumerate(mobs):
        return_string += pron_gender(e.gender, 3) + " " + sequence.ANSI_BLUE + e.typ + sequence.ANSI_RESET
        if i == len(mobs) - 2:
            return_string += " und "
        elif i <= len(mobs) - 3:
            return_string += ", "
    return return_string


def gen_mob(dungeon_level):
    in_level = {}
    for e in list(stats.MOB_BASE_STATS):
        if dungeon_level in stats.MOB_BASE_STATS[e]["level-range"]:
            in_level[e] = stats.MOB_BASE_STATS[e]
    rand = list(in_level)[random.randint(1, len(in_level)) - 1]
    return_list = in_level[rand]
    return_list["typ"] = rand
    return return_list
