from classes import Dog, Cat, Hamster, Horse, Camel, Donkey

dogs = []
cats = []
hamsters = []
horses = []
camels = []
donkeys = []


def main_menu():
    while True:
        print("Выберите действие:")
        print("1. Добавить животное")
        print("2. Получить информацию о животном")
        print("3. Обучить животное новой команде")
        print("4. Выйти из программы")
        choice = int(input())
        print()

        if 1 <= choice <= 3:
            animal_type = animal_type_menu()
            if animal_type == 7:
                continue
            if choice == 1:
                add_animal(animal_type)
            elif 2 <= choice <= 3:
                animal_id, animals = animal_menu(animal_type)
                if animal_id == 0:
                    continue
                if choice == 2:
                    print_info(animals[animal_id - 1])
                if choice == 3:
                    add_commands(animal_id, animals)
        elif choice == 4:
            exit()
        else:
            print("Выберите один из пунктов меню")



def animal_type_menu():
    while True:
        print("Выберите с какими животными вы собираетесь работать:")
        print("1. Собаки")
        print("2. Кошки")
        print("3. Хомяки")
        print("4. Лошади")
        print("5. Лошади")
        print("6. Лошади")
        print("7. Вернуться в главное меню")
        choice = int(input())
        print()

        if 1 <= choice <= 7:
            return choice
        else:
            print("Выберите один из пунктов меню")


def animal_menu(animal_type):
    count = int()
    animals = list()

    if animal_type == 1:
        count, animals = Dog.count, dogs
    elif animal_type == 2:
        count, animals = Cat.count, cats
    elif animal_type == 3:
        count, animals = Hamster.count, hamsters
    elif animal_type == 4:
        count, animals = Horse.count, horses
    elif animal_type == 5:
        count, animals = Camel.count, camels
    elif animal_type == 6:
        count, animals = Donkey.count, donkeys

    if count == 0:
        print("Животных такого типа в питомнике нет, возвращаемся в главное меню\n")
        return 0, object()
    else:
        print(f"Животных такого вида в питомнике - {count}. Какое именно вам нужно?")

        for animal in animals:
            print(f"id: {animal.id} имя: {animal.name}")

        while True:
            animal_id = int(input("Введите id животного или 0, чтобы вернуться в главное меню:"))
            print()
            if animal_id == 0:
                return animal_id, object()
            if animal_id <= count:
                return animal_id, animals
            else:
                print("Выберите одного из животных по его id или вернитесь в главное меню - 0")


def add_animal(animal_type):
    name = input("Введите имя:")
    birth_day = input("Введите дату рождения:")
    commands = input("Введите список команд через пробел без запятых:").split()
    print()

    if animal_type == 1:
        dogs.append(Dog("dog", name, birth_day, commands))
    if animal_type == 2:
        cats.append(Cat("cat", name, birth_day, commands))
    if animal_type == 3:
        hamsters.append(Hamster("hamster", name, birth_day, commands))
    if animal_type == 4:
        horses.append(Horse("horse", name, birth_day, commands))
    if animal_type == 5:
        camels.append(Camel("camel", name, birth_day, commands))
    if animal_type == 6:
        donkeys.append(Donkey("donkey", name, birth_day, commands))


def print_info(animal):
    print(f"id: {animal.id}")
    print(f"animal type: {animal.animal_type}")
    print(f"birth day: {animal.birth_day}")
    print(f"commands: {animal.commands}")
    print()


def add_commands(animal_id, animals):
    animals[animal_id - 1].commands += input("Введите новые команды для животного через пробел, без запятых").split()


main_menu()