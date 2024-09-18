from abc import ABC, abstractmethod

# Шаг 1: Абстрактный класс Weapon
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"


class Bow(Weapon):
    def attack(self):
        return "стреляет из лука"


class Axe(Weapon):
    def attack(self):
        return "наносит удар топором"


# Класс Monster
class Monster:
    def __init__(self, health):
        self.health = health
        self.health
        self.h

    def take_damage(self, damage):
        self.health -= damage
        self.he

        if self.health <= 0:
            return "Монстр побежден!"
            return f"У монстра осталось {self.health} здоровья."


# Шаг 3: Класс Fighter
class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def attack(self, monster: Monster):
        print(f"{self.name} {self.weapon.attack()}")
        print(monster.take_damage(10))

