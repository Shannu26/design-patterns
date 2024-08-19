# Subsystem Classes containing various 
# components of Home Theater
class Amplifier:
	def on(self):
		print("Amplifier is on")

	def off(self):
		print("Amplifier is off")

class DVDPlayer:
	def on(self):
		print("DVD Player is on")

	def play(self, movie):
		print(f"Playing {movie}")

	def stop(self):
		print("DVD Player stopped")

	def off(self):
		print("DVD Player is off")

class Projector:
	def on(self):
		print("Projector is on")

	def off(self):
		print("Projector is off")

class TheaterLights:
	def dim(self, level):
		print(f"Theater lights dimmed to {level}%")
		
# Facade Class with a simple interface
class HomeTheaterFacade:
	def __init__(self, amp: Amplifier, dvd: DVDPlayer, projector: Projector, lights: TheaterLights):
		self.amp = amp
		self.dvd = dvd
		self.projector = projector
		self.lights = lights

	def watch_movie(self, movie: str):
		print("Get ready to watch a movie...")
		self.lights.dim(10)
		self.projector.on()
		self.amp.on()
		self.dvd.on()
		self.dvd.play(movie)

	def end_movie(self):
		print("Shutting movie theater down...")
		self.lights.dim(100)
		self.projector.off()
		self.dvd.stop()
		self.dvd.off()
		self.amp.off()

# Client Code
if __name__ == "__main__":
	# Subsystem components
	amp = Amplifier()
	dvd = DVDPlayer()
	projector = Projector()
	lights = TheaterLights()

	# Facade
	home_theater = HomeTheaterFacade(amp, dvd, projector, lights)

	# Using the facade to watch a movie
	home_theater.watch_movie("Inception")

	# Using the facade to end the movie
	home_theater.end_movie()