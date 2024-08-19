from abc import ABC, abstractmethod

# Client Interface
class OriginalInterface(ABC):
	@abstractmethod 
	def getInsights(self, dataInXML: str):
		pass

# Service Class
class ThirdPartyLibrary:
	def analyze(self, dataInJSON):
		print(dataInJSON)
		print("Analyzing Data")

# Adapter Class
class XMLToJSONAdapter(OriginalInterface):
	def __init__(self):
		self.adaptee = ThirdPartyLibrary()

	def getInsights(self, dataInXML: str):
		print(dataInXML)
		print("Converted XML to JSON")
		dataInJSON = dataInXML + " in JSON form"
		self.adaptee.analyze(dataInJSON)

# Client Code
if __name__ == "__main__":
	adapter = XMLToJSONAdapter()
	adapter.getInsights("XML Data")