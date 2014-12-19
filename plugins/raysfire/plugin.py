from plugins.BasePlugin import BasePlugin
#from Twitchy import modHandlers


class raysfirePlugin(BasePlugin):
        def __init__(self, twitchy):
                super(raysfirePlugin, self).__init__(twitchy)
		
                self.registerCommand('shud', self.advertHandler)
                self.registerCommand('pbs', self.bobrossHandler)
                self.registerCommand('stream', self.twitchHandler)
                self.registerCommand('taj', self.tajHandler)
                self.registerCommand('dasani', self.waterHandler)
                self.registerCommand('crackhead', self.ianHandler)
                self.registerCommand('raysfire',self.raysfireHandler)
                self.registerCommand('raysbeef',self.beefrayser)
                self.registerTrigger('settle it in smash',self.smashSettler)
                self.registerCommand('online', self.onlineHandler)

        def onlineHandler(self, nick, commandArg):
                if nick=='tomdiamond':
                        self.sendMessage("congratulations. You have spammed enough that Tom actually bothered to activate the bot")
                
        def smashSettler(self, nick, commandArg):
                print(nick+"wants to settle it in smash")
                self.sendMessage("http://i.imgur.com/44StnIs.jpg")

        def beefrayser(self, nick, commandArg):
                print(nick+"Has raysed the beef!")
                self.sendMessage("It's time to rays the steaks! \\\\ raysBeef //")

        def raysfireHandler(self, nick, commandArg):
                print("!raysfire called by "+nick)
                self.sendMessage("Some unique stream commands are !dongers, !pbs, !taj, !crackhead, and !stream")

        def ianHandler(self, nick, commandArg):
                print("!crackhead called by "+nick)
                self.sendMessage("http://i.imgur.com/kBVxIyG.png")

        def waterHandler(self, nick, commandArg):
                print("!dasani called by "+nick)
                self.sendMessage("Raysfire is sponsored by Dasani. Dasani: Enhanced with Minerals for a Pure, Fresh Taste™")

        def tajHandler(self, nick, commandArg):
                print('ZIS IS FO YOU')
                self.sendMessage("ZIS IS FO YOU")

        def twitchHandler(self, nick, commandArg):
                print("!stream called by "+nick)
                self.sendMessage('You can watch raysfire stream at twitch.tv/raysfire')

        def advertHandler(self, nick, commandArg):
                print("!shud called by "+nick)
                self.sendMessage('Do you want to be as cool as Ian “Crackhead” Rays himself? Install Rayshud and you can at least look the part! rayshud.com')

        def bobrossHandler(self, nick, commandArg):
                print("!pbs called by "+nick)
                self.sendMessage('When the stream is over, destress with some of the finest art on this side of the badlands. Visit tf2bobross’s gallery at http://tf2bobross.deviantart.com/')
        
