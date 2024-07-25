class Animals:
    count = 0

    def __init__(self, animal_type, name, birth_day, commands):
        self.animal_type = animal_type
        self.name = name
        self.birth_day = birth_day
        self.commands = commands
        Animals.count += 1

    def add_command(self, command):
        self.commands.append(command)



class Pets(Animals):
    pass


class Pack_Animals(Animals):
    pass


class Dog(Pets):
    count = 0

    def __init__(self, animal_type, name, birth_day, commands):
        Pets.__init__(self, animal_type, name, birth_day, commands)
        Dog.count += 1
        self.id = Dog.count


class Cat(Pets):
    count = 0

    def __init__(self, animal_type, name, birth_day, commands):
        Pets.__init__(self, animal_type, name, birth_day, commands)
        Cat.count += 1
        self.id = Cat.count


class Hamster(Pets):
    count = 0

    def __init__(self, animal_type, name, birth_day, commands):
        Pets.__init__(self, animal_type, name, birth_day, commands)
        Hamster.count += 1
        self.id = Hamster.count


class Horse(Pack_Animals):
    count = 0

    def __init__(self, animal_type, name, birth_day, commands):
        Pack_Animals.__init__(self, animal_type, name, birth_day, commands)
        Horse.count += 1
        self.id = Horse.count


class Camel(Pack_Animals):
    count = 0

    def __init__(self, animal_type, name, birth_day, commands):
        Pack_Animals.__init__(self, animal_type, name, birth_day, commands)
        Camel.count += 1
        self.id = Camel.count


class Donkey(Pack_Animals):
    count = 0

    def __init__(self, animal_type, name, birth_day, commands):
        Pack_Animals.__init__(self, animal_type, name, birth_day, commands)
        Donkey.count += 1
        self.id = Donkey.count

#
# animal_1 = Animals("Dog", "Bob", "100", ["gav"])
# print(animal_1.count, animal_1.type, animal_1.name, animal_1.birth_day, animal_1.commands)
#
# animal_2 = Animals("Cat", "Alice", "200", ["meow"])
#
#
# print(animal_2.count, animal_2.type, animal_2.name, animal_2.birth_day, animal_2.commands)
#
# animal_2.add_command("qq")
#
# print(animal_1.type, animal_1.name, animal_1.birth_day, animal_1.commands)
# print(animal_2.type, animal_2.name, animal_2.birth_day, animal_2.commands)
