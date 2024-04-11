# prac6.py
import random

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def is_alive(self):
        return self.health > 0

    def attack(self, other):
        raise NotImplementedError("Subclasses must implement this method.")

class Player(Character):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def attack(self, other):
        damage = random.randint(5, 20)
        other.health -= damage
        print(f"{self.name} attacks {other.name} for {damage} damage. {other.name} now has {other.health} health.")

class Monster(Character):
    def __init__(self, name, health=50):
        self.name = name
        self.health = health

    def attack(self, other):
        damage = random.randint(5, 20)
        other.health -= damage
        print(f"{self.name} attacks {other.name} for {damage} damage. {other.name} now has {other.health} health.")

def game_loop():
    player = Player("Hero")
    monster = Monster("Goblin")
    while player.is_alive() and monster.is_alive():
        player.attack(monster)
        if monster.is_alive():
            monster.attack(player)
    if player.is_alive():
        print(f"{player.name} defeated {monster.name}!")
    else:
        print("You have been defeated by the monster...")

if __name__ == "__main__":
    game_loop()