

class randomCreater(object):
	"""docstring for randomCreater"""
	def __init__(self, seed, param):
		self.seed = int(seed * 1000000)
		self.param = param


	def core(self, pre, length):
		resultList = []
		for i in range(int(pre)):
			self.seed = self.param * self.seed * (1000000 - self.seed) / 1000000
		for i in range(int(length)):
			self.seed = self.param * self.seed * (1000000 - self.seed) / 1000000
			resultList.append(self.seed) 



	def list(self, length=10, pre=1000):
		randomList = self.core(pre,length)
		
		