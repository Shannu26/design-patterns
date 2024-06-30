from abc import ABC, abstractmethod

# Product Interfaces
class Button(ABC):
	@abstractmethod
	def click(self):
		pass

class TextBox(ABC):
	@abstractmethod
	def display(self):
		pass

# Concrete Products
class DarkButton(Button):
	def click(self):
		return "Dark Button clicked"

class LightButton(Button):
	def click(self):
		return "Light Button clicked"

class DarkTextBox(TextBox):
	def display(self):
		return "Dark TextBox displayed"

class LightTextBox(TextBox):
	def display(self):
		return "Light TextBox displayed"

# Abstract Factory Interface
class UIFactory(ABC):
	@abstractmethod
	def create_button(self) -> Button:
		pass

	@abstractmethod
	def create_textbox(self) -> TextBox:
		pass

# Concrete Factories
class DarkUIFactory(UIFactory):
	def create_button(self) -> Button:
		return DarkButton()

	def create_textbox(self) -> TextBox:
		return DarkTextBox()

class LightUIFactory(UIFactory):
	def create_button(self) -> Button:
		return LightButton()

	def create_textbox(self) -> TextBox:
		return LightTextBox()

# Client Code
def client_code(factory: UIFactory):
	button = factory.create_button()
	textbox = factory.create_textbox()

	print(button.click())
	print(textbox.display())

# Usage
print("Dark Theme:")
client_code(DarkUIFactory())

print("\nLight Theme:")
client_code(LightUIFactory())