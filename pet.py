class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        if not (0 <= self.hunger <= 10):
            raise ValueError("Hunger must be between 0 and 10")
        if not (0 <= self.energy <= 10):
            raise ValueError("Energy must be between 0 and 10")
        if not (0 <= self.happiness <= 10):
            raise ValueError("Happiness must be between 0 and 10")

    def eat(self):
        self.hunger = max(0, self.hunger - 5)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        self.energy = min(10, self.energy + 5)

    def play(self):
       self.happiness = min(10, self.happiness + 2)
       self.energy = max(0, self.energy - 2)
       self.hunger = min(10, self.hunger + 2)
        

    def train(self, trick):
        self.tricks.append(trick)
        

    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} has not learned any tricks yet.")
        else:
            print(f"{self.name} can do the following tricks: {', '.join(self.tricks)}")
       

    def get_status(self):
        print(f"{self.name}'s status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")