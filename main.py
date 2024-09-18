from abc import ABC, abstractmethod

# Шаг 1: Абстрактный класс Weapon
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass