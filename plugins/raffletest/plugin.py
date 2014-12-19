from plugins.BasePlugin import BasePlugin
import random
class raffletestPlugin(BasePlugin):
	def startraffle1Handler (self, nick, commandArg):
		print('startraffle1 called by '+nick)
		if nick == 'tomdiamond' :
			print('this raffle is enabled')
		self.sendMessage('A raffle has started! Type !raffle1 to enter')
		self.raffle1Enabled=True

	def endraffle1Handler (self, nick, commandArg):
		print('endraffle1 called by '+nick)
		if nick == 'tomdiamond' :
			print('this raffle is disabled')
		self.raffle1Enabled=False
		winner=random.randint(0,len(self.raffle1List))
		self.sendMessage(self.raffle1List[winner]+' has won the raffle')

	def listuser1Handler (self, nick, commandArg):
		print('listuser1 called by '+nick)
		self.sendMessage(str(len(raffle1List))+'people have entered the raffle')

	def raffle1Handler (self, nick, commandArg):
		if self.raffle1Enabled:
			makeEntry=True
			for element in self.raffle1List:
				if element==nick:
					makeEntry=false
			if makeEntry:
				self.raffle1List.append(nick)
				self.sendMessage(nick+' has entered the raffle, type !raffle1 to enter')

	def startraffle2Handler (self, nick, commandArg):
		print('startraffle2 called by '+nick)
		if nick == 'tomiamond' :
			print('this raffle is enabled')
		self.sendMessage('A raffle has started! Type !raffle2 to enter')
		self.raffle2Enabled=True

	def endraffle2Handler (self, nick, commandArg):
		print('endraffle2 called by '+nick)
		if nick == 'tomiamond' :
			print('this raffle is disabled')
		self.raffle2Enabled=False
		winner=random.randint(0,len(self.raffle2List))
		self.sendMessage(self.raffle2List[winner]+' has won the raffle')

	def listuser2Handler (self, nick, commandArg):
		print('listuser2 called by '+nick)
		self.sendMessage(str(len(raffle2List))+'people have entered the raffle')

	def raffle2Handler (self, nick, commandArg):
		if self.raffle2Enabled:
			makeEntry=True
			for element in self.raffle2List:
				if element==nick:
					makeEntry=false
			if makeEntry:
				self.raffle2List.append(nick)
				self.sendMessage(nick+' has entered the raffle, type !raffle2 to enter')

	def __init__(self, twitchy):
		super(raffletestPlugin, self).__init__(twitchy)

		self.registerCommand('startraffle1', self.startraffle1Handler)
		self.registerCommand('endraffle1', self.endraffle1Handler)
		self.registerCommand('listuser1', self.listuser1Handler)
		self.registerCommand('raffle1', self.raffle1Handler)
		self.registerCommand('startraffle2', self.startraffle2Handler)
		self.registerCommand('endraffle2', self.endraffle2Handler)
		self.registerCommand('listuser2', self.listuser2Handler)
		self.registerCommand('raffle2', self.raffle2Handler)
		self.raffle1Enabled=False
		self.raffle1List= []
		self.raffle2Enabled=False
		self.raffle2List= []
