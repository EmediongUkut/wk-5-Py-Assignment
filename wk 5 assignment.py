# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self._power = power  # Encapsulated (protected)
        self.city = city

    def introduce(self):
        return f"I am {self.name}, protector of {self.city}!"

    def use_power(self):
        return f"{self.name} uses {self._power}!"

    def get_power(self):
        return self._power  # Getter for encapsulated power

    def set_power(self, new_power):
        self._power = new_power  # Setter for encapsulated power


# Inherited class
class FlyingHero(Superhero):
    def use_power(self):
        return f"{self.name} flies through the skies to save {self.city}!"


# Inherited class
class TechHero(Superhero):
    def use_power(self):
        return f"{self.name} deploys advanced tech gadgets to fight crime in {self.city}!"
































