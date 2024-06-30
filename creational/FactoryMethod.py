from abc import ABC, abstractmethod

# Product Interface
class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass

# Concrete Products
class Truck(Transport):
    def deliver(self) -> str:
        return "Delivered by Truck"

class Ship(Transport):
    def deliver(self) -> str:
        return "Delivered by Ship"

# Creator
class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self) -> str:
        transport = self.create_transport()
        return transport.deliver()

# Concrete Creators
class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

# Client Code
def client_code(logistics: Logistics):
    print(logistics.plan_delivery())

# Usage
print("Road Logistics:")
client_code(RoadLogistics())

print("\nSea Logistics:")
client_code(SeaLogistics())