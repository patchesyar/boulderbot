from plugins.BasePlugin import BasePlugin
#from Twitchy import modHandlers


class raysfirePlugin(BasePlugin):
        def __init__(self, twitchy):
                super(raysfirePlugin, self).__init__(twitchy)
		
                self.registerCommand('match', self.matchHandler)
                self.registerCommand('shud', self.advertHandler)
                self.registerCommand('pbs', self.bobrossHandler)
                self.registerCommand('stream', self.twitchHandler)
                self.registerCommand('taj', self.tajHandler)
                self.registerCommand('dasani', self.waterHandler)
                self.registerCommand('crackhead', self.ianHandler)
                self.registerCommand('dongers', self.dongerRayser)
                self.registerCommand('raysfire',self.raysfireHandler)

        def raysfireHandler(self, nick, commandArg):
                print("!raysfire called by "+nick)
                self.sendMessage("Some unique stream commands are !dongers, !pbs, !taj, !crackhead, and !stream")

        
        def dongerRayser(self, nick, commandArg):
                print(nick+" has raysed their buckets")
                self.sendMessage("\\\\_/ ヽ༼ຈل͜ຈ༽ﾉ Rays your buckets ヽ༼ຈل͜ຈ༽ﾉ \\\\_/")

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

        def matchHandler(self, nick, commandArg):
                print("!match called by "+nick)
                self.sendMessage('Greetings gamers, hope you’re enjoying the stream of competitive TF2. Rays has chat hidden and likely won’t see what you’re saying until the end of the match.')

        def advertHandler(self, nick, commandArg):
                print("!shud called by "+nick)
                self.sendMessage('Do you want to be as cool as Ian “Crackhead” Rays himself? Install Rayshud and you can at least look the part! rayshud.com')

        def bobrossHandler(self, nick, commandArg):
                print("!pbs called by "+nick)
                self.sendMessage('When the stream is over, destress with some of the finest art on this side of the badlands. Visit tf2bobross’s gallery at http://tf2bobross.deviantart.com/')
        
