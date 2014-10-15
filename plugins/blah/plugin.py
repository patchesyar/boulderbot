from plugins.BasePlugin import BasePlugin
import random
class blahPlugin(BasePlugin):
	def lmgtfyHandler (self, nick, commandArg):
		print('lmgtfy called by '+nick)
		if len(commandArg)==1:
			self.sendMessage('Hey %s, you gotta give me something to google!'%nick)
		else:
			googleargs=''
			for i in range(1,len(commandArg)):
				googleargs+=commandArg[i]
				if i!=len(commandArg)-1:
					googleargs+='+'
			self.sendMessage('www.google.com/#q='+googleargs)
	def __init__(self, twitchy):
		super(blahPlugin, self).__init__(twitchy)

		self.registerCommand('lmgtfy', self.lmgtfyHandler)
