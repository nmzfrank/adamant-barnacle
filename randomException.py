class randomException(Exception):
	pass

class rangeException(randomException):
	def __init__(self, expression, message):
		self.expression = expression
		self.message = message