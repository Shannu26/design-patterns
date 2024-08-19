# Let's consider an example of a computer parts inventory where we want to 
# perform various operations like displaying information and calculating the total price.

from abc import ABC, abstractmethod

# Visitor Interface
class ComputerPartVisitor(ABC):
	@abstractmethod
	def visit_keyboard(self, keyboard: 'Keyboard'):
		pass

	@abstractmethod
	def visit_monitor(self, monitor: 'Monitor'):
		pass

	@abstractmethod
	def visit_mouse(self, mouse: 'Mouse'):
		pass

	@abstractmethod
	def visit_computer(self, computer: 'Computer'):
		pass

# Concrete Visitors
class ComputerPartDisplayVisitor(ComputerPartVisitor):
	def visit_keyboard(self, keyboard: 'Keyboard'):
		print("Displaying Keyboard.")

	def visit_monitor(self, monitor: 'Monitor'):
		print("Displaying Monitor.")

	def visit_mouse(self, mouse: 'Mouse'):
		print("Displaying Mouse.")

	def visit_computer(self, computer: 'Computer'):
		print("Displaying Computer.")

# Element Interface
class ComputerPart(ABC):
	@abstractmethod
	def accept(self, visitor: ComputerPartVisitor):
		pass

# Concrete Elements
class Keyboard(ComputerPart):
	def accept(self, visitor: ComputerPartVisitor):
		visitor.visit_keyboard(self)

class Monitor(ComputerPart):
	def accept(self, visitor: ComputerPartVisitor):
		visitor.visit_monitor(self)

class Mouse(ComputerPart):
	def accept(self, visitor: ComputerPartVisitor):
		visitor.visit_mouse(self)

class Computer(ComputerPart):
	def __init__(self):
		self.parts = [Keyboard(), Monitor(), Mouse()]

	def accept(self, visitor: ComputerPartVisitor):
		for part in self.parts:
			part.accept(visitor)
		visitor.visit_computer(self)

# Client Code
if __name__ == "__main__":
	computer = Computer()
	display_visitor = ComputerPartDisplayVisitor()
	computer.accept(display_visitor)