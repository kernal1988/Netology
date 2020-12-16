allweigft = []

class Animal():
    def __init__(self, name, weight, voice):
        self.name = name
        self.weight = weight
        self.voice = voice
        allweigft.append(weight)

class Birds(Animal):
    bird_type = ''
    def pick(self):
        return f'У {self.bird_type} {self.name} собрали яйца и услышали {self.voice}!'

class Chicken(Birds):
    bird_type = 'курицы'

class Duck(Birds):
    bird_type = 'утки'

class Goose(Birds):
    bird_type = 'гуся'

class Animals(Animal):
    animals_type = ''
    def pick(self):
        return f'{self.animals_type} {self.name} подоили и услышали {self.voice}!'

class Cow(Animals):
    animals_type = 'Корову'

class Sheep(Animals):
    animals_type = 'Овцу'

class Goat(Animals):
    animals_type = 'Козу'

if __name__ == "__main__":
    first_goose = Goose("Серый", 7, "Га-Га-Га")
    print(first_goose.pick())
    second_goose = Goose("Белый", 7, "Га-Га-Га")
    print(second_goose.pick())
    first_cow = Cow("Манька", 300, "Мууу")
    print(first_cow.pick())
    first_sheep = Sheep("Барашек", 50, "Бее")
    print(first_sheep.pick())
    second_sheep = Sheep("Кудрявый", 50, "Бее")
    print(second_sheep.pick())
    first_chicken = Chicken("Ко-Ко", 5, "Ко-Ко")
    print(first_chicken.pick())
    second_chicken = Chicken("Кукареку", 5, "Ко-Ко")
    print(second_chicken.pick())
    first_duck = Duck("Кряква", 4, "Кря")
    print(first_duck.pick())
    first_goat = Goat("Рога", 5, "Бее")
    print(first_goat.pick())
    second_goat= Goat("Копыта", 5, "Бее")
    print(second_goat.pick())
print ('=====')
print("Все животные на ферме весят: ", sum(allweigft))
print("Самое тяжелое животное:", max(allweigft))