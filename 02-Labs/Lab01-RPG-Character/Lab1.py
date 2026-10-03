class Player:
    def __init__(self, name, level, hp, weapon, armor, guild):
        self.name = name
        self.level = level
        self.hp = hp
        self.weapon = weapon
        self.armor = armor
        self.guild = guild

    def print_info(self):
        print(f"Name : {self.name} \n"
              f"Level : {self.level} \n"
              f"HP : {self.hp} \n" 
              f"Weapon : {self.weapon.name} (Damage : {self.weapon.damage}) (Broken : {self.weapon.broken})\n" 
              f"Armor : {self.armor.name} (Defense : {self.armor.defense}) (Broken : {self.armor.broken})\n"
              f"Guild : {self.guild.name} (Leader : {self.guild.leader.name})")
        
    def attack(self):
        pass
    def walk(self):
        pass
    def jump(self):
        pass
    def eat(self):
        pass

class Weapon:
    def __init__(self, name, damage, broken):
        self.name = name
        self.damage = damage
        self.broken = broken
    def crash(self):
        pass
    def upgrade(self):
        pass

class Armor:
    def __init__(self, name, defense, broken):
        self.name = name
        self.defense = defense
        self.broken = broken
    def crash(self):
        pass
    def upgrade(self):
        pass

class Guild:
    def __init__(self, name):
        self.name = name
        self.leader = None
        self.member = []
    
    def print_info(self):
        for member in self.member:
            print(f"Player : {member.name}")
        print(f"Leader : {self.leader.name}")
    def rename(self):
        pass
    def delete(self):
        pass

sword = Weapon("Sword", 10 ,100)
bow = Weapon("Bow", 8 ,50)

shirt = Armor("Shirt", 0 ,49)
pant = Armor("Pant",0 ,52)

hero_guild = Guild("Hero")
dragon_guild = Guild("dragon")

player1 = Player("Knight_1", 1, 10, Weapon, Armor, Guild)
player1.weapon = sword
player1.armor = shirt
player1.guild = hero_guild

player2 = Player("Knight_2", 2, 20, Weapon, Armor, Guild)
player2.weapon = bow
player2.armor = pant
player2.guild = hero_guild

player3 = Player("Knight_3", 99, 999, Weapon("Hand",99,99), Armor("Full Diamond",99,99), Guild)
player3.guild = dragon_guild

hero_guild.leader = player2
hero_guild.member.append(player1)
hero_guild.member.append(player2)

dragon_guild.leader = player1
dragon_guild.member.append(player3)
print("\n===Hero===")
hero_guild.print_info()
print("\n===Dragon===")
dragon_guild.print_info()
print("===Player 1===")
player1.print_info()
print("\n===Player 2===")
player2.print_info()
print("\n===Player 3===")
player3.print_info()
