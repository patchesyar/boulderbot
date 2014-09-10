"""
pystats plugin for twitchy bot written by John "Tom 'Diamond' Dan" Lavoie
twitchy bot original code by Matthew McNamara <https://github.com/MattMcNam/twitchy>

pystats plugin is used to pull the most recent sizzling stats log file fromsizzlingstats.com. The triggering command
is !stats <str> with <str> being an optional parameter. This parameter is defaulted to the twitch channel username if
it is not stated in the chat command. The bot will find the most recent log for the steamID provided in the command and
post it as a message in chat.


to-do:
add an alt-case for players to redirect twitch usernames to steamurls. text document
add a confirmation notice if the lobby info is more than a day old
"""

import time
from urllib.request import *
from plugins.BasePlugin import BasePlugin


predsOn= False
predslist=[]

class PystatsPlugin(BasePlugin):
    
    def __init__(self, twitchy):
        """
        initializes pystats plugin object with the commands
        """
        super(PystatsPlugin, self).__init__(twitchy)

        #self.registerCommand('stats', self.sizzlerHandler)
        self.registerCommand('stats', self.placeholder)
        self.registerCommand('subtest', self.subtestHandler)
        self.registerCommand('startpred', self.predStart)
        self.registerCommand('stoppred', self.predStop)
        self.registerCommand('pred', self.pred)
        self.registerCommand('checkpred', self.predChecker)
        self.registerCommand('listpred', self.predlist)
        self.registerCommand('pypredhelp', self.predHelper)


##################################
#####       Pypreds         ######
##################################

    def predHelper(self, nick, commandArg):
        global predsOn
        print("predhelper called by "+nick)
        strin=""
        if predsOn:
            strin="Predictions are currently enabled"
        else:
            strin="Predictions are disabled, they should be re-enabled before the next match"
            self.sendMessage("Make a prediction with '!pred x:y' "+strin)
        
        
    def predStart(self, nick, commandArg):
        print("predStart called by "+nick)
        global predsOn
        if nick== 'tomdiamond' or nick== 'raysfire' or nick== 'twilitlord' or nick=='newb':
            print("predictions are enabled")
            predsOn=True

    def predStop(self, nick, commandArg):
        print("predstop called by "+nick)
        global predsOn
        if nick== 'tomdiamond' or nick== 'raysfire' or nick=='twilitlord;' or nick=='newb':
            print("predictions are disabled")
            predsOn=False

    def pred(self, nick, commandArg):
        global predsOn
        global predslist
        makepred=True
        if predsOn:
            print(nick+" has made a prediction")
            if len(commandArg)==2:
                count=0
                for element in predslist:
                    if element[0]== nick:
                        predslist.remove(element)
                    if element[1]== commandArg[1]:
                        self.sendMessage(element[0]+" has already made that prediction, try another one")
                        makepred=False
                if makepred:
                    self.sendMessage(nick+" has made the prediction of "+commandArg[1])
                    predslist.append((nick, commandArg[1]))
            else:
                self.sendMessage("Hey "+nick+", you can make a prediction with '!pred x:y'")
        else:
            self.sendMessage("Predictions are currently disabled, come back when they are re-enabled!")
            
    def predChecker(self, nick, commandArg):
        global predslist
        if nick== 'tomdiamond' or nick== 'raysfire' or nick=='twilitlord' or nick=='newb':
            print(nick+" is checking the preds")
            if len(commandArg)!=2:
                self.sendMessage("Hey "+nick+", remember to add the correct kd too!")
            else:
                chickendinner=False
                for element in predslist:
                    if element[1]== commandArg[1]:
                        self.sendMessage(str(element[0])+" correctly guessed the kd and won the prediction contest!")
                        chickendinner=True
                if not chickendinner:
                    self.sendMessage("Nobody won the prediction contest this time")
                predslist=[]

    def predlist(self, nick, commandArg):
        global predslist
        if len(commandArg)!=2:
            if len(predslist)>10:
                self.sendmessage(str(len(predslist))+" people have entered predictions")
            predmakers=""
            time.sleep(2)
            for element in predslist:
                predmakers+=(element[0]+" ")
            self.sendMessage(predmakers) #returns the list of all the people that made predictions
        else:
            for element in predslist:
                if element[0]==commandArg[1]:
                    self.sendMessage(element[1]) #returns the kd prediction for a certain player

#######################################
#####           Pystats          ######
#######################################

                    

    def subtestHandler(self, nick, commandArg):
        #Simple test function for the substitution.
        #Bounces back a substitute if any
        self.sendMessage("I got "+ findSubstitutes(nick))

    def placeholder(self, nick, commandArg):
        """
        placeholder function: prints messages to console and chat to confirm
        the plugin is loaded and running
        """
        print("!stats attempted by "+nick)
        self.sendMessage("!stats is under construction, thanks for trying!")
    
    def sizzlerHandler(self, nick, commandArg):
        """
        Reply function to '!stats'. prints to console and calls sizzlerGet to
        post link to sizzlingstats.com
        """
        global Twitch_Channel
        print("!stats called by "+nick+". I hope this works...")
        steamID= Twitch_Channel
        if len(commandArg)==2:
            steamID=commandArg[1]
        self.sendMessage(sizzlerGet(steamID))

    def sizzlerGet(steamID):
        """
        given a steam ID in any format, retrieves the latest sizzling stats lobby
        link and returns it
        """
        Steam64=steamidCorrect(str(steamID))
        pagetitle=("http://www.sizzlingstats.com/player/"+Steam64)
        #pagetitle="http://www.fairportrobotics.org"
        print(pagetitle)
        with urlopen(pagetitle) as url:
            s=url.read
        print(s)

    def steamidCorrect(nick):
        """
        pulls the steam64 id from steamidconverter.com/<steamID>
        can accept customURL, steam64, or steamID

        FORMAT EXAMPLES:
        steamID: STEAM_0:1:25030559
        steam64: 76561198010326847
        customURL: patchesyar
        """
        findSubstitutes(nick)
        pagetitle="steamidconverter.com/"+steamID
        print(pagetitle)
        return str(steamID)
        with urlopen(pagetitle) as url:
            s=url.read
        print(s)

    def findSubstitutes(nick):
        for line in open("substitutes.txt"):
            inline=line.split(" ")
            if nick!=inline[0]:
                pass
            else:
                return inline[1]
        return nick
