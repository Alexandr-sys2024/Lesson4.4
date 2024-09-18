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

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return "Монстр побежден!"
        else:
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


# Реализация пошагового боя
def battle():
    # Создаем бойца с мечом
    fighter = Fighter("Боец", Sword())

    # Создаем монстра с 30 единицами здоровья
    monster = Monster(30)

    # Пошаговая смена оружия и атаки
    while monster.health > 0:
        print("\n1. Меч")
        print("\n2. Лук")
        print("\n3. Топор")
        choice = input("Выберите оружие для атаки (1, 2, 3): ")

        # Смена оружия в зависимости от выбора пользователя
        if choice == '1':
            fighter.change_weapon(Sword())
        elif choice == '2':
            fighter.change_weapon(Bow())
        elif choice == '3':
            fighter.change_weapon(Axe())
        else:
            print("Неверный выбор! Попробуйте снова.")
            continue

        # Атака монстра выбранным оружием
        fighter.attack(monster)

    print("Бой завершен, монстр побежден!")


if __name__ == "__main__":
    battle()






