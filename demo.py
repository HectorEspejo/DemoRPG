print("Write your name: ")
name = input(">")
class Character:
    #name and skills
    def __init__(self, name, hp, lvl, exp, money, strength, energy):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self.exp = exp
        self.money = money
        self.strength = strength
        self.energy = energy
    def rest(self):
        if self.energy < 6:
            print(f"{self.name} decides to rest")
            input(">...")
            self.energy = 10
            print(f"Energy is restored!")
            input(">...")
    def die(self):
        if self.hp == 0:
            print(f"{name} has died")
    def attacked_debug(self):                   #Kill yourself
        print("Debug: healthpoints goes to 0")
        self.hp = 0
    def debug_health(self):                     #For testing the adding of health
        self.hp = self.hp + 100
    def city(self):                             #No sirve para nada
        print("City")
    def explore(self):
        print("Where do you wish to travel:")
        print("[A]Rudbury town")
        print("[B]Mount Reborn")
        print("[C]Royal harbour")
        travel_option = input(">")
        if travel_option == "A":
            print(f"Welcome to Rudbury Town, {self.name}")
            input()
            print("Here's what you can do:")
            input()
            while True:
                print("[A]Go to the bar")
                print("[B]Go to the king's court")
                print("[C]Go to the store")
                print("[D]Exit")
                rubury_option = input(">")
                if rubury_option == "C":
                    print(f"{self.name} enters a store full of antiquities and unuseful stuff")
                    input()
                    print("SHOPKEEPER: Hello, fellow traveler! What can I do for you?")
                    input()
                    print("[A]Buy")
                    print("[B]Tell me a joke")
                    shop_option = input(">")
                    if shop_option == "A":
                        while True:
                            print("These are my goods:")
                            input()
                            print("(A) Sword -> 100 R: Adds 4 to strength")
                            input()
                            print("What do you wish to buy?")
                            buy_option = input(">")
                            if buy_option == "A":
                                if self.money >= 100:
                                    self.money = self.money - 100
                                    print("You've purchased a sword!")
                                    self.strength = self.strength + 4
                                    input()
                                    print(f"{self.name} returns to the main square")
                                    input()
                                    break
                                if self.money < 100:
                                    print("SHOPKEEPER: Nothing in life is free, pal")
                                    input()
                                    print(f"{self.name} returns to the main square")
                                    input()
                                    break
                            if buy_option == "C":
                                print("No problem!")
                if rubury_option == "D":
                    print(f"{self.name} gets out from there")
                    break


class Enemy_1:
    def __init__(self, name = "pirate"):
        self.name = name

p = Character(name, 100, 1, 0, 100, 3, 5)

while p.hp > 0:
    print("Choose an option:")
    command = input(">")
    if command == "attacked_debug":
        p.attacked_debug()
        print(f"Debug: You have {p.hp}")
    if command == "help":
        print("explore, rest, status")
        input("...")
    if command == "status":
        print(f"Name: {p.name}")
        print(f"Healthpoints: {p.hp}")
        print(f"Money: {p.money}")
        print(f"Strength: {p.strength}")
        print(f"Energy: {p.energy}")
        input("...")
    if command == "debug_health":
        p.debug_health()
        print(f"Now you have {p.hp}")
    if command == "rest":
        p.rest()
    if command == "tiogilito":                          #Add 1000 money
        print("Voi'lá!")
        print("+1000 added to your money. Don't be a huge spender")
        input()
        p.money = p.money + 1000
    if command == "explore":
        p.explore()
