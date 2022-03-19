import shutil
import os
import time
import asyncio
import keyboard
import threading

clear = lambda: os.system('cls')

os.system("")

inpt = "START_VALUE"

def move(x, y):
    print("\033[%d;%dH" % (y, x))

def inp():
    global inpt
    while True:
        inpt = input("")

def main():
    global inpt
    input_loop = threading.Thread(target=inp)
    input_loop.start()
    while True:
        if inpt != "":
            columns, lines = shutil.get_terminal_size()
            clear()
            print("""
    ╔════════════════════════════╗    ╔════════════════════════════╗    ╔════════════════════════════╗
    ║ Helm:                      ║    ║                            ║    ║                            ║
    ║ Harnisch:                  ║    ║                            ║    ║                            ║
    ║ Harnisch:                  ║    ║                            ║    ║                            ║
    ║ Beinschutz:                ║    ║                            ║    ║                            ║
    ║ Schuhe:                    ║    ║                            ║    ║                            ║
    ║ Rucksack:                  ║    ║                            ║    ║                            ║
    ║ Waffe:                     ║    ║                            ║    ║                            ║
    ║ Sekundär:                  ║    ║                            ║    ║                            ║
    ╚════════════════════════════╝    ╚════════════════════════════╝    ╚════════════════════════════╝

    ╔""" + "═" * (columns - 10)  + """╗
    ║ """ + " " * (columns - 12)  + """ ║
    ║ """ + " " * (columns - 12)  + """ ║
    ║ """ + " " * (columns - 12)  + """ ║
    ║ """ + " " * (columns - 12)  + """ ║
    ║ """ + " " * (columns - 12)  + """ ║
    ║ """ + " " * (columns - 12)  + """ ║
    ║ """ + inpt + " " * (columns - 12 - len(inpt))  + """ ║
    ╚""" + "═" * (columns - 10)  + """╝


  ═>""",
            end=""
            )
            inpt = ""



main()
