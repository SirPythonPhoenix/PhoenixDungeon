
def max_health(level):
    return (level + 5)**2


def dmg(level):
    return (level + 2) - 1


def exp(level):
    return round(level * 50)


def acc():
    return 80


def monster_health(level):
    return round((level + 5)**2 / 7)


def monster_dmg(level):
    return round(level**2 / 10)


for i in range(1, 101):

    print(
        "-------------------------------"
        
        "\n\nPLAYER"
        "\nLevel: " + str(i) +
        "\nMax Health: " + str(max_health(i)) +
        "\nBase Damage: " + str(dmg(i)) +
        "\nExperience for next level: " + str(exp(i)) +

        "\n\nWEAPON" +
        "\nAv Damage:"
        
        "\n\nARMOR"
        
        "\n\nMONSTER" +
        "\nAv Monster Health: " + str(monster_health(i)) +
        "\nAv Monster Damage: " + str(monster_dmg(i))
    )
