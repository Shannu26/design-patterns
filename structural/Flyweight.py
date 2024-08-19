# Let's consider an example of a text editor where we need to handle the formatting 
# (e.g., font, style, color) of characters. Instead of creating a new object for each 
# character, we can use the flyweight pattern to share the formatting information among multiple characters.

# Flyweight Interface
from abc import ABC, abstractmethod

class Flyweight(ABC):
	@abstractmethod
	def operation(self, extrinsic_state):
		pass

# Concrete Flyweight Class
class ConcreteFlyweight(Flyweight):
	def __init__(self, intrinsic_state):
		self._intrinsic_state = intrinsic_state

	def operation(self, extrinsic_state):
		print(f"Intrinsic State: {self._intrinsic_state}, Extrinsic State: {extrinsic_state}")

# Flyweight Factory Class
class FlyweightFactory:
	_flyweights = {}

	@staticmethod
	def get_flyweight(intrinsic_state):
		if intrinsic_state not in FlyweightFactory._flyweights:
			FlyweightFactory._flyweights[intrinsic_state] = ConcreteFlyweight(intrinsic_state)
		return FlyweightFactory._flyweights[intrinsic_state]

	@staticmethod
	def list_flyweights():
		count = len(FlyweightFactory._flyweights)
		print(f"FlyweightFactory: I have {count} flyweights:")
		print(", ".join(FlyweightFactory._flyweights.keys()))

# Context Class
class CharacterContext:
	def __init__(self, character, font, size, color):
		self.character = character
		self.font = font
		self.size = size
		self.color = color
		self.flyweight = self.create_flyweight()

	def create_flyweight(self):
		key = f"{self.font}-{self.size}-{self.color}"
		return FlyweightFactory.get_flyweight(key)

	def display(self):
		self.flyweight.operation(self.character)

# Client Code
if __name__ == "__main__":
	contexts = [
		CharacterContext('H', 'Arial', 12, 'red'),
		CharacterContext('e', 'Arial', 12, 'red'),
		CharacterContext('l', 'Arial', 12, 'red'),
		CharacterContext('l', 'Arial', 12, 'red'),
		CharacterContext('o', 'Arial', 12, 'red'),
		CharacterContext('W', 'Times', 14, 'blue'),
		CharacterContext('o', 'Times', 14, 'blue'),
		CharacterContext('r', 'Times', 14, 'blue'),
		CharacterContext('l', 'Times', 14, 'blue'),
		CharacterContext('d', 'Times', 14, 'blue'),
    ]

	for context in contexts:
		context.display()

	FlyweightFactory.list_flyweights()