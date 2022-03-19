import pd_sequence as sequence



DUNGEON_DES_PHOENIX = """
██████╗░███████╗██████╗░  ██████╗░██╗░░░██╗███╗░░██╗░██████╗░███████╗░█████╗░███╗░░██╗  ██████╗░███████╗░██████╗
██╔══██╗██╔════╝██╔══██╗  ██╔══██╗██║░░░██║████╗░██║██╔════╝░██╔════╝██╔══██╗████╗░██║  ██╔══██╗██╔════╝██╔════╝
██║░░██║█████╗░░██████╔╝  ██║░░██║██║░░░██║██╔██╗██║██║░░██╗░█████╗░░██║░░██║██╔██╗██║  ██║░░██║█████╗░░╚█████╗░
██║░░██║██╔══╝░░██╔══██╗  ██║░░██║██║░░░██║██║╚████║██║░░╚██╗██╔══╝░░██║░░██║██║╚████║  ██║░░██║██╔══╝░░░╚═══██╗
██████╔╝███████╗██║░░██║  ██████╔╝╚██████╔╝██║░╚███║╚██████╔╝███████╗╚█████╔╝██║░╚███║  ██████╔╝███████╗██████╔╝
╚═════╝░╚══════╝╚═╝░░╚═╝  ╚═════╝░░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚══╝  ╚═════╝░╚══════╝╚═════╝░

██████╗░██╗░░██╗░█████╗░███████╗███╗░░██╗██╗██╗░░██╗
██╔══██╗██║░░██║██╔══██╗██╔════╝████╗░██║██║╚██╗██╔╝
██████╔╝███████║██║░░██║█████╗░░██╔██╗██║██║░╚███╔╝░
██╔═══╝░██╔══██║██║░░██║██╔══╝░░██║╚████║██║░██╔██╗░
██║░░░░░██║░░██║╚█████╔╝███████╗██║░╚███║██║██╔╝╚██╗
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░╚══╝╚═╝╚═╝░░╚═╝"""

DIED = """
██████╗░██╗░░░██╗  ██████╗░██╗░██████╗████████╗
██╔══██╗██║░░░██║  ██╔══██╗██║██╔════╝╚══██╔══╝
██║░░██║██║░░░██║  ██████╦╝██║╚█████╗░░░░██║░░░
██║░░██║██║░░░██║  ██╔══██╗██║░╚═══██╗░░░██║░░░
██████╔╝╚██████╔╝  ██████╦╝██║██████╔╝░░░██║░░░
╚═════╝░░╚═════╝░  ╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░

░██████╗░███████╗░██████╗████████╗░█████╗░██████╗░██████╗░███████╗███╗░░██╗
██╔════╝░██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝████╗░██║
██║░░██╗░█████╗░░╚█████╗░░░░██║░░░██║░░██║██████╔╝██████╦╝█████╗░░██╔██╗██║
██║░░╚██╗██╔══╝░░░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██╔══██╗██╔══╝░░██║╚████║
╚██████╔╝███████╗██████╔╝░░░██║░░░╚█████╔╝██║░░██║██████╦╝███████╗██║░╚███║
░╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚══╝"""

BEGINNING_INTRO = [
    "Du wachst bei {} {} auf.",
    "Du spürst qualvolle Schmerzen. Alles ist schwarz. Plötzlich ist alles weg und du befindest dich bei {} {}.",
    "Alles ist verschwommen. Nach kurzer Zeit kannst du wieder klar sehen. Du befindest dich bei {} {}.",
    "Du siehst Flammen vor dir. Du bist wütend. Plötzlich ist es zu ende und du bebfindest dich bei {} {}."
]

BEGINNING_NAME = [
    "Du kannst dich an nichts erinnern. Du gibst dir selbst einen Namen."
]

LOOKOUT = [
    "Du schaust dich um und entdeckst ",
    "Als du dich umschaust entdeckst du ",
    "Als du einen Blick um dich herum wirfst, entdeckst du ",
    "In deinem Blickfeld befindet sich ",
    "Es scheint als gäbe es hier ",
    "Um dich herum befindet sich ",
    "Du erblickst ",
    "Du entdeckst ",
    "Du findest ",
]

MOVE = [
    "Du gehst weiter und ",
    "Du läufst weiter und ",
    "Du schreitest weiter vor und ",
    "Du gehst um eine Ecke und ",
]

SCOUT = [
    "triffst auf ",
    "entdeckst ",
    "erblickst ",
    "stehst vor ",
    "siehst ",
    "sichtest ",
    "bemerkst ",
]

TRAP_ACTIVATE = [
    "löst {} aus."
]

TRAP = { # darf keine Lehrzeichen enthalten
    "Bärenfalle": {
        "type": "bleed",
        "gender": "F",
        "dmg": 2
    },
    "Giftfalle": {
        "type": "poison",
        "gender": "F",
        "dmg": 3
    },
    "Stachelfalle": {
        "type": "bleed",
        "gender": "F",
        "dmg": 2
    },
    "Fallgrube": {
        "type": "damage",
        "gender": "F",
        "dmg": 10
    },
}

LOOT = {
    "Truhe": "F",
    "Haufen Gegenstände": "M",
    "goldene Kiste": "F",
    "silberne Kiste": "F",
    "edle Truhe": "F",
}

BLOCK ={
    "Blockade": "F",
}

SECRET = { # darf keine Lehrstellen enthalten
    "Geheimtür": "F",
    "Geheimraum": "M",
    "Geheimluke": "F"
}

ENTER = "Möchtest du {} betreten? (dies ist ein Dungeon)"

GENDER_M = ["der", "ein", "einem", "einen", "den"]
GENDER_F = ["die", "eine", "einer", "eine", "die"]
GENDER_N = ["das", "ein", "einem", "ein", "das"]

LOCATION_EMPTY = {
    "Hain": "M",
    "Horst": "M",
    "Grube": "F",
    "Dickicht": "N",
    "Senke": "F",
    "Lichtung": "F",
    "Grasfläche": "F",
    "Wald": "M",
    "Hügel": "M",
}

LOCATION_DUNGEON_EASY = {
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
}

LOCATION_DUNGEON_MIDDLE = {
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
}

LOCATION_DUNGEON_HARD = {
"Festung": "F",
"Gipfel": "M",
"Schlucht": "F",
"Tempel": "M",
"Verlies": "N",
"Garnison": "F",
"Stützpunkt": "M",
"Außenposten": "M",
"Burg": "F",
"Gefängnis": "N",
"Befestigung": "F",
"Wall": "M",
}

LOCATION_DUNGEON_ADJECTIVE = {
    1: "bedrohlich",
    11: "scheußlich",
    21: "furchtbar",
    31: "grauenhaft",
    41: "fürchterlich",
    51: "schrecklich",
    61: "abscheulich",
    71: "ungeheur",
    81: "dämonisch",
    91: "flammend",
    100: "höllisch",
}

ERROR_MISSING_ARGS = sequence.ANSI_RED + "\n[Fehler] Nicht genügend Angaben." + sequence.ANSI_RESET
ERROR_ARGUMENT = sequence.ANSI_RED + "\n[Fehler] Zu viele Angaben." + sequence.ANSI_RESET
ERROR_NOT_AVAILABLE = sequence.ANSI_RED + "\n[Fehler] Unbekannter Befehl." + sequence.ANSI_RESET

WELCOME = {
    "stormstrike": "\n[Emil] Hi Matthias, ich wünsche dir viel Saß beim spielen des Spiels.",
    "roasty": "\n[Emil] Ehrlich, überleg dir mal nen besseren Namen.",
    "senator": "\n[Emil] Ich hätte nie gedacht, dass du jemals dieses Spiel spielst.",
    "kaido": "\n[Emil] Erbarme, der Milchinator ist zurückgekehrt.",

}

DEATH = [
    "abgeschlachtet",
    "vernichtet",
    "getötet",
    "elminiert",
    "beseitigt",
    "exekutiert",
    "hingerichtet",
    "ausgelöscht",
    "erlegt",
    "liquidiert",
    "ausradiert",
    "abgemurkst",
    "kaltgemacht",
    "gekillt",
    "weggepustet",
    "beseitigt"
]
