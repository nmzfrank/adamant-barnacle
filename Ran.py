# -*- coding: utf-8 -*-
from randomException import *

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



class Engine():
	def __init__(self, content, type):
		self.rG = randomGenerator(0.7, 1000)
		self.content = content
		if(type == "square"):
			self.engine = squareEngine(self.content,self.rG)
		if(type == "morse"):
			self.engine = morseEngine(self.content)

	def encode(self):
		return self.engine.encode()

	def decode(self):
		return self.engine.decode()

	def setProperty(self, args):
		self.engine.setProperty(args)

	def printHelp(self):
		return self.engine.printHelp()


class squareEngine():
	def __init__(self,content, rG):
		self.content = content
		self.rG = rG
		self.length = len(self.content)

	def encode(self):
		self.cipherText = ''
		self.transitionList = self.rG.generate(self.length)
		for index in range(self.length):
			self.cipherText += chr(ord(self.content[index]) + self.transitionList[index])
		return self.cipherText

	def decode(self):
		self.plainText = ''
		self.transitionList = self.rG.generate(self.length)
		for index in range(self.length):
			self.plainText += chr(ord(self.content[index]) - self.transitionList[index])
		return self.plainText

	def setProperty(self,rG):
		self.rG = rG

	def printHelp(self):
		helpScript = "nothing to say"
		return helpScript


class morseEngine():
	def __init__(self,content):
		self.content = content
		self.seperator = ' '
		self.length = len(self.content)

	def encode(self):
		return self.content

	def decode(self):
		return self.content

	def setProperty(self,seperator):
		self.seperator = seperator

	def printHelp(self):
		helpScript = "nothing to say"
		return helpScript



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