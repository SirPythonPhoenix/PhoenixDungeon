import pd_text as text
from f_textgenerator import error, attention, tut, high, bold
import pd_sequence as sequence
import f_textgenerator as gen
import f_classes as classes
import pd_stats as stats
import random
import time

inpt = []

def main():
    def greetings():
        print('© Phoenix 2022' + text.DUNGEON_DES_PHOENIX + "\n")
        print('\n\n[Spiel] Dieses Spiel ist zu 100% print-input based und in Python geschrieben.\n'
              '        Das bedeutet im Grunde, dass Text die einzige Eingabe- und Ausgabemöglichkeit in diesem Spiel ist.\n'
              '        Um etwas abzusenden, gebe einfach einen Text ein und drücke dann Enter.\n'
              '        Alle Befehle in diesem Spiel fangen mit einem "." an.\n'
              '        Falls du dir mal nicht sicher bist, kannst du dir alle verfügbaren Befehle mit ".help" anzeigen lassen.\n'
              '        Um fortzufahren und dabei ein neues Spiel zu erstellen, gebe bitte deinen Nickname ein.\n'
              '        Falls du bereits ein Spiel hast, lade es mit dem Befehl ".loadgame"'
              )
        return input("\n[Du] ")

    inpt.append(greetings())

    while True:
        for e in list(text.WELCOME):
            if e in inpt[-1].lower():
                print(text.WELCOME[e])
        if not inpt[-1].startswith('.') and not inpt[-1] == "":
            newgame(inpt[-1])
        elif inpt[-1].startswith('.exit'):
            exit('\n[Spiel] Spiel wird beendet.')
            input()
        elif inpt[-1].startswith(".loadgame"):
            loadgame()
        else:
            print(sequence.ANSI_RED + '\n[Spiel] Unbekannter Befehl.' + sequence.ANSI_RESET)
        inpt.append(input("\n[Du] "))

def newgame(name):
    print(sequence.ANSI_GREEN + '\n[Spiel] Du hast deinen Namen gewählt.'
                                 '\n        Neues Spiel wird erstellt.' + sequence.ANSI_RESET)
    locations = []
    locations.append(classes.Location("empty", isnext=1))
    player = classes.Player(name, 0)
    locations.append(classes.Location("dungeon", level=player.level, isnext=0))
    print("\n[Spiel] " + text.BEGINNING_INTRO[random.randint(1, len(text.BEGINNING_INTRO)) - 1].format(
        gen.pron_gender(text.LOCATION_EMPTY[locations[0].name], 2),
        locations[0].fullname))
    print('        ' + text.BEGINNING_NAME[random.randint(1, len(text.BEGINNING_NAME)) - 1])
    print('        ' + text.LOOKOUT[random.randint(1, len(text.LOOKOUT)) - 1] +
        gen.pron_gender(gen.dungeon_gender(locations[1].name), 1) + ' ' +
        locations[1].fullname + '.')
    print('        ' + text.ENTER.format(locations[1].fullname))
    print('        ' + 'Dann benutze den Befehl ".enter {}"'.format(locations[1].fullname))
    game(locations, player)


def loadgame():
    print(sequence.ANSI_YELLOW + '\n[Spiel] Spiel wird geladen.\nDieser Befehl ist aktuell noch nicht verfügbar.' + sequence.ANSI_RESET)

def game(locations, player):

    def break_down():
        if player.in_dungeon(locations) and player.get_location(locations).events[0] == "blocked":
            health_reduction = random.randint(
                round(stats.PLAYER_BASE_STAT_INCREASE["health"] * player.level - 1/2),
                round(stats.PLAYER_BASE_STAT_INCREASE["health"] * player.level/2),
            )
            player.health -= health_reduction
            print("\n[Spiel] Blockade wurde entfernt.\n"
                  "        Du hast {} Lebenspunkte verloren.".format(health_reduction))
            locations[player.location].events[0] = "clear"
            tut('Benutze ".walk" um dich zum nächsten Raum zu begeben.', player)
        else:
            print(error("Hier gibt es keine Blockade, die du entfernen könntest."))

    def enter():
        if len(inpt[-1].split(" ")) <= 1:
            print(text.ERROR_MISSING_ARGS)
        elif len(inpt[-1].split(" ")) == 2:
            if player.in_dungeon(locations):
                if player.get_location(locations).events[0] == "secret":
                    r = random.randint(0, 100)
                    print("\n[Spiel] Du betrittst {} {}".format(
                        gen.pron_gender(player.get_location(locations).event_attr["gender"], 0),
                        player.get_location(locations).event_attr["name"]
                    ))
                    if r in range(0, 30):
                        locations[player.location].events[0] = "fight"
                    elif r in range(30, 101):
                        locations[player.location].events[0] = "loot"
                    dungeon_event(player.location, player.get_location(locations))
                    return
                else:
                    print(attention("Dieser Befehl kann im Dungeon nicht benutzt werden.\n"
                                    '          Benutze ".flee" um aus dem Dungeon zu flüchten.\n'
                                    '          Du wirst dabei allerdings alle gesammelten Gegenstände verlieren.'))
                    return
            for i, e in enumerate(locations):
                if e.typ == "empty" and e.name == inpt[-1].split(" ")[1]:
                    if player.location in e.isnext:
                        player.location = i
                        print("\n[Spiel] Du begibst dich zu {}".format(e.name))
                        return
                    else:
                        print(error("Ort kann aus aktueller Position nicht betreten werden."))
                        return
            print(error("Ort nicht gefunden."))
        elif len(inpt[-1].split(" ")) == 3:
            for i, e in enumerate(locations):
                if e.typ == "dungeon" and e.adjective == inpt[-1].split(" ")[1] and e.name == inpt[-1].split(" ")[2]:
                    if player.location in e.isnext:
                        player.location = i
                        print("\n[Spiel] Du betrittst den Dungeon {}{}{}.".format(sequence.ANSI_BLUE, e.fullname, sequence.ANSI_RESET))
                        dungeon_event(i, e)
                        return
            print(error("Ort nicht gefunden."))
        else:
            print(text.ERROR_ARGUMENT)

    def died():
        if player.health <= 0:
            print('\n' + text.DIED)
            input("\n")
            exit()

    def loot():
        if locations[player.location].events[0] == 'loot':
            found = ""
            gold_add = random.randint(0, 34) + random.randint(0, 34) + random.randint(0, 34)
            player.gold += gold_add
            found += f'\n- {gold_add} Gold'
            print(game('Du öffnest {} und findest:' + found))
        else:
            print(error('There is nothing to loot here.'))

    def attack():
        if len(locations[player.location].mobs) != 0:
            locations[player.location].mobs = player.attack(inpt[-1], locations[player.location].mobs)
            died()
            if len(locations[player.location].mobs) == 0:
                locations[player.location].events[0] = "clear"
                print('        Du hast alle mobs eliminiert.')
                tut('Du kannst nun ".loot" benutzen um Gegenstände der mobs zu looten.\n' # loot muss noch gemacht werden
                    'Du kannst auch ".walk" benutzen um dich weiter zu begeben.', player)
        else:
            print(error('Es gibt aktuell nichts anzugreifen.'))

    def walk():
        if not(len(locations[player.location].events) == 0) and player.in_dungeon(locations) and (
                player.get_location(locations).events[0] == "clear" or
                player.get_location(locations).events[0] == "loot" or
                player.get_location(locations).events[0] == "secret"
        ):
            locations[player.location].events = locations[player.location].events[1:]
            dungeon_event(player.location, player.get_location(locations))
        else:
            print(error("Befehl kann im moment in verwendet werden."))
        if player.in_dungeon(locations) and len(player.get_location(locations).events) == 0:
            print(game('Du betrittst du nächste Etage des Dungeons.'))

    def execute(action):
        exec(action)

    def dungeon_event(i, e):
        if player.bleed["left"] >= 1:
            player.bleed["left"] -= 1
            insert = f'Du blutest und du erhällst {player.bleed["damage"]} Schaden.\n' \
                     f'        Restliche Dauer: {player.bleed["left"]}\n' \
                     f'        '
            player.health -= player.bleed["damage"]
        elif player.poison["left"] >= 1:
            player.poison["left"] -= 1
            insert = f'Das Gift macht sich bemerkbar und du erhällst {player.poison["damage"]} Schaden.\n' \
                     f'        Restliche Dauer: {player.poison["left"]}\n' \
                     f'        '
            player.health -= player.poison["damage"]
        else:
            insert = ''
        died()
        if e.events[0] == "fight":
            if len(locations[player.location].mobs) == 0:
                for i in range(0, random.randint(1, 2)):
                    locations[player.location].mobs.append(classes.Mob(e.level + e.etage - 1))
            print('\n[Spiel] ' + insert + gen.dungeon_find("{}.").format(gen.dungeon_mobs(locations[player.location].mobs)))
            tut('Benutze ".attack" um anzugreifen.', player)
        if e.events[0] == "trap":
            word = list(text.TRAP)[random.randint(1, len(text.TRAP)) - 1]
            locations[i].event_attr["name"] = word
            locations[i].event_attr["gender"] = text.TRAP[word]["gender"]
            print(
                '\n[Spiel] ' + insert +
                gen.dungeon_find_trap(
                    gen.pron_gender(text.TRAP[word]["gender"], 3) +
                    " " + sequence.ANSI_BLUE + word + sequence.ANSI_RESET))
            if text.TRAP[word]["type"] == "bleed":
                player.bleed["damage"] = text.TRAP[word]["dmg"]
                player.bleed["left"] = random.randint(1, 5)
                print('        Du erhällst Blutung für die Dauer {}.'.format(player.bleed["left"]))
            if text.TRAP[word]["type"] == "poison":
                player.poison["damage"] = text.TRAP[word]["dmg"]
                player.poison["left"] = random.randint(1, 5)
                print('        Du erhällst Gift für die Dauer {}.'.format(player.poison["left"]))
            if text.TRAP[word]["type"] == "damage":
                player.health -= text.TRAP[word]["dmg"]
                print('        Du erhällst {} Direktschaden.'.format(text.TRAP[word]["dmg"]))
            e.events[0] = "clear"
            tut('Du kannst ".walk" benutzen, um weiter zu gehen.', player)
        if e.events[0] == "loot":
            word = list(text.LOOT)[random.randint(1, len(text.LOOT)) - 1]
            print(
                '\n[Spiel] ' + insert + gen.dungeon_find(
                    gen.pron_gender(text.LOOT[word], 3) + ' ' +
                    sequence.ANSI_BLUE + word + sequence.ANSI_RESET + '.'
                )
            )
            tut('Du kannst ".loot" benutzen um zu looten.', player)
        if e.events[0] == "blocked":
            word = list(text.BLOCK)[random.randint(1, len(text.BLOCK)) - 1]
            locations[i].event_attr["name"] = word
            locations[i].event_attr["gender"] = text.BLOCK[word]
            print('\n[Spiel] ' + insert + gen.dungeon_find(gen.pron_gender(text.BLOCK[word], 3) + " " + high(word) + "."))
            tut('Benutze ".break" um die Blockade zu entfernen.\n'
                'Dies kostet dich Lebenspunkte.', player)
        if e.events[0] == "secret":
            word = list(text.SECRET)[random.randint(1, len(text.SECRET)) - 1]
            locations[i].event_attr["name"] = word
            locations[i].event_attr["gender"] = text.SECRET[word]
            print('\n[Spiel] ' + insert + gen.dungeon_find(gen.pron_gender(text.SECRET[word], 3) + " " + sequence.ANSI_BLUE + word + sequence.ANSI_RESET))
            tut('Benutze ".enter {}" um dich in den Geheimraum zu begeben.\n'.format(word) +
                'Du kannst dich alternativ mit ".walk" in den nächsten Raum begeben.', player)
        died()

    def location():
        if len(inpt[-1].split(" ")) >= 2:
            print(text.ERROR_ARGUMENT)
        else:
            print('\n[Spiel] Position: {}'.format(
                locations[player.location].fullname
            ))

    def f_player():
        if inpt[-1] == ".player":
            inpt[-1] = ".player " + player.name
        if len(inpt[-1].split(" ")) >= 3:
            print(text.ERROR_ARGUMENT)
        elif len(inpt[-1].split(" ")) == 2:
            if inpt[-1].split(" ")[1] == player.name:
                print(
                    gen.game(bold('BASE') +
                    '\nName: ' + player.name +
                    '\nLevel: ' + str(player.level) +
                    '\nxp: ' + str(player.xp) +
                    '\nOrt: ' + locations[player.location].fullname +
                    '\nCurrent Health: ' + str(player.health) +
                    bold('\n\nSTATS') +
                    '\nMax Health: ' + str(player.max_health) +
                    '\nArmor: ' + str(player.armor) +
                    '\nDodge: ' + str(player.dodge) +
                    '\nBase Damage: ' + str(player.dmg) +
                    '\nTotal Damage: ' +
                    '\nAccuracy: ' + str(player.acc) +
                    '\nCrit Chance: ' + str(player.crit) +
                    '\nLife Steal: ' + str(player.ls) +
                    bold('\n\nAUSRÜSTUNG') +
                    bold('\n\nINVENTAR'))
                )
        else:
            print(error("Spieler nicht gefunden."))

    def flee():
        if player.in_dungeon(locations):
            word = locations[player.location].fullname
            player.location = player.get_location(locations).isnext[0]
            print("\n[Spiel] Du flüchtest aus dem Dungeon {} und begibst dich zu {}.".format(
                word,
                player.get_location(locations).fullname)
            )

    inpt = []
    while True:
        inpt.append(input(f"\n[{player.name}] "))
        if inpt[-1] == "." and len(inpt) >= 2:
            inpt = inpt[:-1]
            print(' ' * (len(player.name) + 3) + inpt[-1])
        if not inpt[-1].startswith("."):
            pass
        elif inpt[-1].startswith(".enter"):
            enter()
        elif inpt[-1].startswith(".loc"):
            location()
        elif inpt[-1].startswith(".player"):
            f_player()
        elif inpt[-1].startswith(".break"):
            break_down()
        elif inpt[-1].startswith(".flee"):
            flee()
        elif inpt[-1].startswith(".exec"):
            exec(" ".join(inpt[-1].split(" ")[1:]))
        elif inpt[-1].startswith(".walk"):
            walk()
        elif inpt[-1].startswith(".attack"):
            attack()
        elif inpt[-1].startswith(".loot"):
            loot()
        elif inpt[-1].startswith(".exit"):
            exit('\n[Spiel] Spiel wird beendet.')
        else:
            print(text.ERROR_NOT_AVAILABLE)


