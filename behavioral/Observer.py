from abc import ABC, abstractmethod

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

# Concrete Observer
class NewsChannel(Observer):
    def __init__(self, name: str):
        self.name = name
        self.news = None

    def update(self, message: str):
        self.news = message
        print(f"{self.name} received news: {self.news}")

# Subject
class NewsAgency:
    def __init__(self, name: str):
        self.observers = []
        self.name = name
        self.latest_news = None

    def subscribe(self, observer: Observer):
        self.observers.append(observer)

    def unsubscribe(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.latest_news)

    def add_news(self, news: str):
        self.latest_news = news
        self.notify_observers()

# Usage
if __name__ == "__main__":
    # Create news agencies (publishers)
    agency1 = NewsAgency("Agency 1")
    agency2 = NewsAgency("Agency 2")
    
    # Create news channels (subscribers)
    channel1 = NewsChannel("Channel 1")
    channel2 = NewsChannel("Channel 2")
    
    # Channel 1 subscribes to both agencies
    agency1.subscribe(channel1)
    agency2.subscribe(channel1)
    
    # Channel 2 subscribes only to agency 1
    agency1.subscribe(channel2)
    
    # Add news to agency 1
    agency1.add_news("Breaking News from Agency 1!")
    
    # Add news to agency 2
    agency2.add_news("Latest Update from Agency 2!")
    
    # Channel 1 unsubscribes from agency 1
    agency1.unsubscribe(channel1)
    
    # Add more news to agency 1
    agency1.add_news("Second News from Agency 1!")