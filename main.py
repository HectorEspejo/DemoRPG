print("Welcome to the demo")
input(">(Press enter)")
print("First, let's start by choosing your class:")
print("Warrior or Wizard?")
class_selection = input(">")
if class_selection == "Warrior":
    class Warrior:
        def __init__(self, name, lvl, hp, strength, energy):
            self.name = name
            self.lvl = lvl
            self.hp = hp
            self.strength = strength
            self.energy = energy
            name = 000
            lvl = 1
            hp = 100
            strength = 3
            energy = 10
    print("Type your name:")
    name = input(">")
    player = Warrior(name, 1, 100, 3, 10)
    print(f"Welcome, {player.name}.")
    input(">Press enter...")
    print("You're now on lvl 1")
    input(">")
    print(f"You're health points are {player.hp}")
    input(">")
    print(f"You have {player.strength} points of strength")
    input(">")
    print(f"You have {player.energy} points of energy")
    #TBC

if class_selection == "Wizard":
    class Wizard:
        def __init__(self, name, lvl, hp, strength, energy):
            self.name = name
            self.lvl = lvl
            self.hp = hp
            self.strength = strength
            self.energy = energy
            #lvl=1
            hp = 110
            strength = 2
            energy = 15

    print("Write down your name")
    name = input(">")
    player = Wizard(name, 1, 110, 2, 15)
    print(f"Welcome, {player.name}")
    input(">")
    print(f"Your health points are {player.hp}")
    input(">")
    print(f"You have {player.strength} strength points")
    input(">")
    print(f"You have {player.energy} energy points")
    input(">")
    #TBC