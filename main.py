class Pet:
    def __init__(self, name, typee, sound):
        self.name = name
        self.type = typee
        self.sound = sound
    
    def play_sound(self):
        print(f"{self.type} named {self.name} says: {self.sound}")

class Human:
    def __init__(self, name, age, pets = None):
        self.name = name
        self.age = age
        self.pets = []

    def get_pet(self, pet):
        if isinstance(pet,Pet):
            print(f"Can't get a pet")
            return
        else:
            print(f"{self.name} has taken {pet}")
            self.pets.append(pet)

    def play_with_pets(self):
        if self.pets:
            print(f"{self.name} is playing with his pets")
            for pet in self.pets:
                pet.play_sound()
        else:
            print(f"{self.name} has no pets to play with")

class House:
    def __init__(self, adress, owner):
        self.adress = adress
        self.owner = owner
        self.people = []

    def move_in(self, human):
        if not isinstance(human,Human):
            print("You can't move in :(")
        else:
            self.people.append(human)
            print("You have been succesfully moved in!")
    
    def who_lives(self):
        if self.people:
            print("Who lives here:")
            for people in self.people:
                print(people.name)
                if people.pets:
                    for pet in people.pets:
                        print(pet.name)

murzik = Pet("Murzik", "Cat", "Meow")
bob = Human("Bob", 24)

bob.play_with_pets()
bob.get_pet(murzik)
bob.play_with_pets()

Dom = House("Bukhar Zhirau 21", "Aleksei")
Dom.who_lives()
Dom.move_in(bob)
Dom.who_lives()