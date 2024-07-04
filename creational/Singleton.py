from threading import Lock

class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    A metaclass that controls the creation of the singleton instance. 
    It maintains a dictionary _instances to store the singleton instance. 
    The __call__ method ensures that only one instance of the class is created.
    """
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class SingletonV1(metaclass=SingletonMeta):
    def __init__(self):
        self.value = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

class SingletonV2:
    instance = None

    def __init__(self):
        self.value = None

    @staticmethod
    def getInstance():
        if not SingletonV2.instance:
            SingletonV2.instance = SingletonV2()
        return SingletonV2.instance

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

def testV1():
    s1 = SingletonV1()
    s1.set_value("Singleton Instance 1")
    print(s1.get_value())  # Output: Singleton Instance 1

    s2 = SingletonV1()
    print(s2.get_value())  # Output: Singleton Instance 1

    s2.set_value("Singleton Instance 2")
    print(s1.get_value())  # Output: Singleton Instance 2
    print(s2.get_value())  # Output: Singleton Instance 2

    print(s1 is s2)  # Output: True

def testV2():
    s1 = SingletonV2.getInstance()
    s1.set_value("Singleton Instance 1")
    print(s1.get_value())

    s2 = SingletonV2.getInstance()
    print(s2.get_value())

    s2.set_value("Singleton Instance 2")
    print(s1.get_value())
    print(s2.get_value())

    print(s1 is s2)

# Usage V1
if __name__ == "__main__":
    testV1()
    print()
    testV2()
    