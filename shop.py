class Character (object):
  hp = 100
  sp = 3
  money = 500
  inventory = []
  
class Shop (object):
  money = 5000
  def buy(p):
    while True:
      shoplist = ["[A] Sword", "[B]Potion", "[C] Exit"]
      print("Select the item you wanna buy: ")
      print(shoplist)
      shopselection = input(">Select: ")
      if shopselection == "A":
        print("You've chosen the Sword")
        p.money = p.money - 100
        p.sp = p.sp + 2
        input("...")
        print("You lost 100 L and you gained 2 Strength")
        input("...")
        Shop.money = Shop.money + 100
        print("Shop money: ", Shop.money)
        shoplist.pop(0)
        input("...")
        if shopselection == "C":
          break
      
      

    
  
  
  
p = Character

store = Shop

while p.hp > 0:
  command = input(">")
  if command == "status":
    print(f"HP: ", p.hp)
    print(f"Strength: ", p.sp)
    print(f"Money: ", p.money)
    print("Inventory: ", p.inventory)
  
  if command == "shop":
   Shop.buy(p)
