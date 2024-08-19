from abc import ABC, abstractmethod

# Mediator Interface
class ChatRoomMediator(ABC):
    @abstractmethod
    def show_message(self, user, message):
        pass

# Concrete Mediator Classes
class ChatRoom(ChatRoomMediator):
    def show_message(self, user, message):
        print(f"[{user.name}]: {message}")

# Component Classes
class User:
    def __init__(self, name, chat_room):
        self.name = name
        self.chat_room = chat_room

    def send_message(self, message):
        self.chat_room.show_message(self, message)

# Client Code
if __name__ == "__main__":
    chat_room = ChatRoom()

    user1 = User("Alice", chat_room)
    user2 = User("Bob", chat_room)

    user1.send_message("Hello, Bob!")
    user2.send_message("Hi, Alice!")