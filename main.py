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

