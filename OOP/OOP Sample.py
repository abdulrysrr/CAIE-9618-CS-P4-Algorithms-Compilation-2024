class Animal:
    """Parent class"""
    def __init__(self, name: str, species: str):
        # name: str
        # species: str
        self._name = name
        self._species = species

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_species(self):
        return self._species

    def set_species(self, species):
        self._species = species

    def display(self):
        print(f"Name: {self._name}, Species: {self._species}")


class Cat(Animal):
    """Child class of Animal"""
    def __init__(self, name: str, breed: str):
        # name: str
        # breed: str
        super().__init__(name, "Cat")
        self._breed = breed

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        self._breed = breed

    def display(self):
        super().display()
        print(f"Breed: {self._breed}")


class Dog(Animal):
    """Child class of Animal"""
    def __init__(self, name: str, breed: str):
        # name: str
        # breed: str
        super().__init__(name, "Dog")
        self._breed = breed

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        self._breed = breed

    def display(self):
        super().display()
        print(f"Breed: {self._breed}")


# Example usage
cat = Cat("Whiskers", "Siamese")
dog = Dog("Buddy", "Labrador")

cat.display()
dog.display()
