from abc import ABC, abstractmethod

# Service Interface
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# Service Class
class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._load_image_from_disk()

    def _load_image_from_disk(self):
        print(f"Loading image from disk: {self.filename}")

    def display(self):
        print(f"Displaying image: {self.filename}")

# Proxy Class
class ProxyImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

# Client Code
if __name__ == "__main__":
    image1 = ProxyImage("photo1.jpg")
    image2 = ProxyImage("photo2.jpg")

    # Image will be loaded from disk
    image1.display()

    # Image will be displayed directly without loading from disk again
    image1.display()

    # Image will be loaded from disk
    image2.display()

    # Image will be displayed directly without loading from disk again
    image2.display()