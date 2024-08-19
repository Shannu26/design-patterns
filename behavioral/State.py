# Let's consider an example of a vending machine that has different states such as 
# "Idle", "HasMoney", and "Dispensing".

from abc import ABC, abstractmethod

# State Interface
class State(ABC):
    @abstractmethod
    def insert_money(self):
        pass

    @abstractmethod
    def select_item(self):
        pass

    @abstractmethod
    def dispense_item(self):
        pass

# Concrete State Classes
class IdleState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_money(self):
        print("Money inserted.")
        self.vending_machine.set_state(self.vending_machine.has_money_state)

    def select_item(self):
        print("Insert money first.")

    def dispense_item(self):
        print("Insert money first.")

class HasMoneyState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_money(self):
        print("Money already inserted.")

    def select_item(self):
        print("Item selected.")
        self.vending_machine.set_state(self.vending_machine.dispensing_state)

    def dispense_item(self):
        print("Select an item first.")

class DispensingState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_money(self):
        print("Dispensing in progress. Please wait.")

    def select_item(self):
        print("Dispensing in progress. Please wait.")

    def dispense_item(self):
        print("Dispensing item.")
        self.vending_machine.set_state(self.vending_machine.idle_state)

# Context Class
class VendingMachine:
    def __init__(self):
        self.idle_state = IdleState(self)
        self.has_money_state = HasMoneyState(self)
        self.dispensing_state = DispensingState(self)

        self.state = self.idle_state

    def set_state(self, state):
        self.state = state

    def insert_money(self):
        self.state.insert_money()

    def select_item(self):
        self.state.select_item()

    def dispense_item(self):
        self.state.dispense_item()

# Client Code
if __name__ == "__main__":
    vending_machine = VendingMachine()

    vending_machine.select_item()
    vending_machine.insert_money()
    vending_machine.select_item()
    vending_machine.dispense_item()