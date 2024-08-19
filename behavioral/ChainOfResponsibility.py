# Let's consider an example of a logging system where we have different levels of 
# logging such as Info, Debug, and Error. Each logging level will handle the 
# request if it meets the criteria, otherwise, it will pass it to the next handler in the chain.

# Handler Interface
from abc import ABC, abstractmethod

class Handler(ABC):
	@abstractmethod
	def set_next(self, handler):
		pass

	@abstractmethod
	def handle(self, request):
		pass

# Base Handler
class BaseHandler(Handler):
	_next_handler = None

	def set_next(self, handler):
		self._next_handler = handler
		return handler

	def handle(self, request):
		if self._next_handler:
			return self._next_handler.handle(request)
		return None

# Conrete Handlers
class InfoHandler(BaseHandler):
	def handle(self, request):
		if request == "INFO":
			return f"InfoHandler: Handling {request}"
		else:
			return super().handle(request)

class DebugHandler(BaseHandler):
	def handle(self, request):
		if request == "DEBUG":
			return f"DebugHandler: Handling {request}"
		else:
			return super().handle(request)

class ErrorHandler(BaseHandler):
	def handle(self, request):
		if request == "ERROR":
			return f"ErrorHandler: Handling {request}"
		else:
			return super().handle(request)

# Client Code
if __name__ == "__main__":
	info_handler = InfoHandler()
	debug_handler = DebugHandler()
	error_handler = ErrorHandler()

	info_handler.set_next(debug_handler).set_next(error_handler)

	requests = ["INFO", "DEBUG", "ERROR", "UNKNOWN"]

	for req in requests:
		result = info_handler.handle(req)
		if result:
			print(result)
		else:
			print(f"{req} was not handled.")