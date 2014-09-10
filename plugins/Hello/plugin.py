import time #time delays to allow for multi-message commands (!match)
from plugins.BasePlugin import BasePlugin
#from Twitchy import modHandlers

class HelloPlugin(BasePlugin):
        sezcopresent=False      #Sezco hates some of the commands, so when he is present,
                                #I try to deactivate these commands
        def __init__(self, twitchy):
                super(HelloPlugin, self).__init__(twitchy)
		
                self.registerCommand('hello', self.helloHandler) # respond when '!hello' is at beginning of message
                self.registerTrigger('hi there', self.heyHandler) # respond when 'hi' is anywhere in message
                self.registerCommand('kawaii', self.kawaiiHandler)
                self.registerCommand('highfive', self.highfiveHandler)
                self.registerForJoinPartNotifications(self.userJoinPart) # Greet a user, or say goodbye
                self.registerForModNotifications(self.modGivenTaken)
                self.registerCommand('steamtest', self.steamHandler)
                self.registerCommand('transformice', self.mouseHandler)
                self.registerCommand('hotsingles', self.loveHandler)
                self.registerCommand('swag', self.swagHandler)
                self.registerCommand('github', self.gitHandler)
                self.registerCommand('real', self.pogChampion)
                self.registerCommand('kill', self.killer)
                #self.registerCommand('refresh', self.refresher)
                self.registerTrigger('This is our town scrub', self.townHandler)
                self.registerCommand('boulderbot', self.boulderHandler)

        def boulderHandler(self, nick, commandArg):
                print("!boulderbot called by "+nick)
                self.sendMessage("Boulderbot was designed by Tom Dan using Matt Mcnamara's base Twitchy Architecture. Some general commands include !kawaii, !hello, !swag, and many many more. Experiment and ask around about other commands!")

        
        def townHandler(self, nick, commandArg):
                print("This is "+nick+"'s town, scrub")
                self.sendMessage("(ง •̀_•́)ง Yeah, beat it! (ง •̀_•́)ง")

        def refresher(self, nick, commandArg):
                #TODO: find out how in the architecture to "restart" the bot
                self.__init__(self.twitchy)

        def killer(self, nick, commandArg):
                #NOTE: only kills the plugin this command is in,
                #Either use polymorphism to work for all plugins or
                #find a way to apply it at top-level
                self.sendMessage("Goodbye team, my fellow rocks need me elsewhere")
                self._kill()

        def pogChampion(self, nick, commandArg):
                print("PogChamp ROUND 5 HYPE PogChamp")
                self.sendMessage("PogChamp HYPE PogChamp")

        def gitHandler(self, nick, commandArg):
                print("!gitHandler called by "+nick)
                self.sendMessage("*NEW* Boulderbot github: https://github.com/patchesyar/boulderbot")

        def swagHandler(self, nick, commandArg):
                print("!swag called by "+nick)
                self.sendMessage("http://i.imgur.com/c4ErkCB.jpg")

        def loveHandler(self, nick, commandArg):
                print("!hotsingles called by "+nick)
                self.sendMessage("http://i.imgur.com/BpVQZgM.jpg")

        def matchHandler(self, nick, commandArg):
                print("!match called by "+nick)
                self.sendMessage('Greetings gamers, hope you’re enjoying the stream of competitive TF2. We are in a private match and you will not be able to join.')
                time.sleep(2)
                self.sendMessage("If you'd like to join, please wait until we join a public server. Thank you!")

        def mouseHandler(self, nick, commandArg):
                print("!transformice called by "+nick)
                self.sendMessage('This stream is brought to you by www.transformice.com featuring the premier mouse-themed MMO')

        def advertHandler(self, nick, commandArg):
                print("!shud called by "+nick)
                self.sendMessage('Do you want to be as cool as Ian “Crackhead” Rays himself? Install Rayshud and you can at least look the part! rayshud.com')

        def steamHandler(self, nick, commandArg):
                print("!steamtest called by "+nick)
                print(commandArg)
                self.sendMessage("You want the steamid of "+ commandArg[1]+"?")

        def helloHandler(self, nick, commandArg):
                print("!hello called by "+nick)
                print(commandArg)
                if len(commandArg)>=2:
                        newword=""
                        for i in range(1, len(commandArg)):
                                if i==len(commandArg):
                                        newword+=(commandArg[i])
                                else:
                                        newword+=(commandArg[i]+" ")
                        if commandArg[1].lower()=="boulderbot":
                                self.sendMessage("Hello "+nick+"!")
                        else:
                                self.sendMessage("Hello "+newword+"!")
                else:
                        self.sendMessage("Hello "+ nick +"!")

        def kawaiiHandler(self, nick, commandArg):
                print("!kawaii called by "+nick)
                self.sendMessage("You're so cute, "+ nick +"-senpai Keepo")

        def highfiveHandler(self, nick, commandArg):
                print("!highfive called by "+nick)
                print("ognDoAoh / \\ ognChoBro")
                self.sendMessage("Poooound / " +"\\\\"+" DogFace")
	
        def heyHandler(self, nick, fullMsg):
                print("hey there called by " +nick)
                if nick=='tomdiamond':
                        self.sendMessage("Tom, don't let Rays strangle me!")
                else:
                        self.sendMessage("Hi there, "+nick+". I'm TT.")
        
        def userJoinPart(self, nick, isJoining):
                if isJoining:
                        print(nick+" has joined")
                        #self.sendMessage("Welcome "+ nick +"!")
                else:
                        print(nick+" has left")
                        #self.sendMessage("See ya, "+ nick)

        def modGivenTaken(self, nick, modGiven):
                global sezcopresent
                if modGiven:
                        print("Moderator status given to "+ nick)
                        if nick=="Sezco":
                                sezcopresent=True
                                print (str(sezcopresent))
                        #self.sendMessage("Run! "+ nick +" has been given moderator powers!")
                else:
                        print("Moderator status removed from "+ nick)
                        if nick=="Sezco":
                                sezcopresent=False
                                print (str(sezcopresent))
                        #self.sendMessage("Relax, "+ nick +" has lost moderator powers")
