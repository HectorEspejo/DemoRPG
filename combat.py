class Character:
    def __init__(self, lvl, exp, health, strength):
        self.lvl = lvl
        self.exp = exp
        self.health = health
        self.strength = strength

    def level_up(self):
        self.exp = self.exp + 100
        if self.exp == 100:
            self.lvl = self.lvl + 1
            self.strength = self.strength + 1
            self.health = self.health + 10
            self.exp = 0
            print(f"You've reached level {self.lvl}!")
            input()
            print(f"You have now {self.health} HP and {self.strength} points")
            input()


class Enemy:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength


p = Character(1, 0, 100, 5)


e = Enemy(10, 1)

print("You have encountered an enemy!")
input()
while p.health > 0:
    print(f"Your HP: {p.health}")
    print(f"Enemy HP: {e.health}")
    input()
    print("What to do?")
    print("attack / escape")
    action = input(">")
    if action == "attack":
        print(f"You make {p.strength} points of damage")
        e.health = e.health - p.strength
        input()
        print(f"Enemy does {e.strength} points of damage to you")
        p.health = p.health - e.strength
        input()
    if e.health == 0:
        print("You've won")
        input()
        print("You gained 50 experience!")
        p.level_up()
        break
    if action == "escape":
        if e.health > 5:
            print("You can't escape!")
            input()
        if e.health < 5:
            print("You escaped!")
            break
