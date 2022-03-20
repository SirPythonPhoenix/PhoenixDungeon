import random

LOCATION_FIELD = [
    "Hain",
    "Horst",
    "Grube",
    "Dickicht",
    "Senke",
    "Lichtung",
    "Grasfläche",
    "Wald",
    "Hügel",
]

LOCATION_DUNGEON_WORD = {
    "Wald": "M",
    "Höhle": "F",
    "Sumpf": "M",
    "Mine": "F",
    "Gewölbe": "N",
    "Forst": "M",
    "Friedhof": "M",
    "Begräbnis": "N",
    "Tümpel": "M",
    "Moor": "N",
    "Kanalisation": "F",
    "Katakomben": "F",
    "Ruine": "F",
    "Grabmal": "N",
    "Gruft": "F",
    "Zitadelle": "F",
    "Grotte": "F",
    "Wrack": "N",
    "Mausoleum": "N",
    "Grabstätte": "F",
    "Festung": "F",
    "Gipfel": "M",
    "Schlucht": "F",
    "Tempel": "M",
    "Verlies": "N",
    "Garnison": "F",
    "Gefängnis": "N",
    "Befestigung": "F",
    "Wall": "M",
}

LOCATION_DUNGEON_ADJECTIVE = [
    "bedrohlich",
    "scheußlich",
    "furchtbar",
    "grauenhaft",
    "fürchterlich",
    "schrecklich",
    "abscheulich",
    "ungeheur",
    "dämonisch",
    "flammend",
    "höllisch",
]

MOBS = [
    'verdammter Bär',
    'dreiköpfiger Wolf',
    'Skelett',
    'Gnom',
    'gefräßige Bestie',
    'fleischiges Scheusal',
    'Kobold',
    'Gespenst',
    'Ghul',
    'Ork',
    'Troll',
    'Vampir',
    'Banshee',
    'Harpyie',
    'Gargoyle',
    'Arachnoide',
]

WEAPONS = [
    'Dussack',
    'Keule',
    'Knüppel',
    'Beil',
    'Spieß',
    'Wurfkeule',
    'Wurfspieß',
    'Hammer',
    'Messer',
    'Bauernsense',
    'Mistgabel',
    'Säbel',
    'Bogen',
    'Dolchstab',
    'Antennendolch',
    'Kriegsgabel',
    'Sturmsense',
    'Streithacke',
    'Holzfäller Axt',
    'Dolch',
    'Wurfspeer',
    'Degen',
    'Hornbogen',
    'Gladius',
    'Kriegshammer',
    'Lanze',
    'Kriegszepter',
    'Mordaxt',
    'Armbrust',
    'Streitkolben',
    'Streithammer',
    'Triangulärer Vollgriffdolch',
    'Fausthammer',
    'Langschwert',
    'Schießeisen',
    'Wurfsterne',
    'Xiphos',
    'Streitaxt',
    'Morgenstern',
    'Griffangelschwert',
    'Griffzungenschwert',
]

def gen_dung_name():
    word = random.choice(list(LOCATION_DUNGEON_WORD))
    if LOCATION_DUNGEON_WORD[word] == "M":
        return f"{random.choice(LOCATION_DUNGEON_ADJECTIVE)}er {word}"
    if LOCATION_DUNGEON_WORD[word] == "F":
        return f"{random.choice(LOCATION_DUNGEON_ADJECTIVE)}e {word}"
    if LOCATION_DUNGEON_WORD[word] == "N":
        return f"{random.choice(LOCATION_DUNGEON_ADJECTIVE)}es {word}"


class Scaling:
    @staticmethod
    def max_health(level):
        return (level + 5) ** 2

    @staticmethod
    def dmg(level):
        return (level + 2) - 1

    @staticmethod
    def exp(level):
        return round(level * 50)

    @staticmethod
    def acc():
        return 80

    @staticmethod
    def monster_health(level):
        return round((level + 5) ** 2 / 7)

    @staticmethod
    def monster_dmg(level):
        return round(level ** 2 / 10)
