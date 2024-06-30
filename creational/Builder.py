from abc import ABC, abstractmethod

# Product
class House:
    def __init__(self):
        self.walls = None
        self.doors = None
        self.windows = None

    def __str__(self):
        return f"House with {self.walls} walls, {self.doors} doors, and {self.windows} windows."

# Builder Interface
class HouseBuilder(ABC):
    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_doors(self):
        pass

    @abstractmethod
    def build_windows(self):
        pass

    @abstractmethod
    def get_house(self) -> House:
        pass

# Concrete Builders
class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "concrete"

    def build_doors(self):
        self.house.doors = "wooden"

    def build_windows(self):
        self.house.windows = "glass"

    def get_house(self) -> House:
        return self.house

class WoodenHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "wooden"

    def build_doors(self):
        self.house.doors = "metal"

    def build_windows(self):
        self.house.windows = "plastic"

    def get_house(self) -> House:
        return self.house

# Director
class ConstructionDirector:
    def __init__(self, builder: HouseBuilder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_walls()
        self.builder.build_doors()
        self.builder.build_windows()

# Usage
concreteBuider = ConcreteHouseBuilder()
woodenBuilder = WoodenHouseBuilder()
director = ConstructionDirector(woodenBuilder)
director.construct_house()
house = woodenBuilder.get_house()
print(house)