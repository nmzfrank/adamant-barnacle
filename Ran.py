

class randomException(Exception):
	pass

class rangeException(randomException):
	def __init__(self, expression, message):
		self.expression = expression
		self.message = message

class randomGenerator(object):
	"""docstring for randomGenerator"""
	def __init__(self, seed, round, param = 3.7):
		super(randomGenerator, self).__init__()
		self.param = param
		self.seed = float(seed)
		self.round = int(round)
		self.num = int(self.seed * 1000000)
		if(self.seed <= 0 or self.seed >= 1):
			raise rangeException('seed','0-1')
		if(self.round < 0):
			raise rangeException('round','0-')
		

	def __iteration(self):
		self.num = int(self.param * self.num * ( 1000000 - self.num ) / 1000000)

	def generate(self, length):
		self.length = int(length)
		if(self.length <= 0):
			raise rangeException('length','1-')
		self.genList = []
		for i in range(self.round):
			self.__iteration()
		for i in range(self.length):
			self.__iteration()
			self.genList.append(self.num % 10)
		return self.genList


class encode():
	def __init__(self, content, rG):
		self.content = content 
		self.rG = rG
		self.length = len(self.content)

	def transform(self):
		self.cipherText = ''
		self.transitionList = self.rG.generate(self.length)
		for index in range(self.length):
			self.cipherText += chr(ord(self.content[index]) + self.transitionList[index])
		return self.cipherText

class decode():
	def __init__(self, content, rG):
		self.content = content
		self.rG = rG
		self.length = len(self.content)

	def transform(self):
		self.plainText = ''
		self.transitionList = self.rG.generate(self.length)
		for index in range(self.length):
			self.plainText += chr(ord(self.content[index]) - self.transitionList[index])
		return self.plainText


def test():
	rg1 = randomGenerator(0.8, 1000)
	rg2 = randomGenerator(0.8, 1000)
	e = encode('hello world', rg1)
	cipherText = e.transform()
	plainText = decode("yqo{dujpe", rg2).transform()
	print cipherText
	print plainText


if __name__ == '__main__':
	test()