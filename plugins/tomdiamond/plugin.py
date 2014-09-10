from plugins.BasePlugin import BasePlugin


bonkcount=0

class tomdiamondPlugin(BasePlugin):
        def __init__(self, twitchy):
            super(tomdiamondPlugin, self).__init__(twitchy)

            self.registerCommand('hud', self.hudHandler)
            self.registerCommand('varsaa', self.shehnahandler)
            self.registerTrigger('sprotsblades', self.sprotshandler)
            self.registerCommand('steam', self.steamHandler)
            self.registerTrigger('bonk', self.bonkHandler)
            self.registerCommand('tomdiamond', self.tomHandler)

        def tomHandler(self, nick, commandArg):
            print("!tomdiamond called by "+nick)
            self.sendMessage("some of this stream's commands are !steam, !match, !varsaa, !hud, and sprotsblades")

        def bonkHandler(self, nick, commandArg):
            global bonkcount
            print("You been bonked son")
            bonkcount+=1
            self.sendMessage("Tom has bonked! Current bonk count is "+bonkcount+" meaning he has to do "+bonkcount*5+" pushups")
            
        def steamHandler(self, nick, commandArg):
            print("!steam called by "+nick)
            self.sendMessage("Join Tom's stream steam group at steamcommunity.com/groups/tomdiamond or add him at steamcommunity.com/id/patchesyar")

        def hudHandler(self, nick, commandArg):
            print("!hud called by "+nick)
            self.sendMessage("You can download rayshud, the hud Tom uses at rayshud.com")

        def shehnahandler(self, nick, commandArg):
            print("LOL Shana's bad, amirite "+nick)
            self.sendMessage(nick + " thinks varsaa's bad at everything")

        def sprotshandler(self, nick, commandArg):
            print(nick+" loves the sprotsblades")
            self.sendMessage("Welcome to tomdiamond's stream, home of SPROTSBLADES")
