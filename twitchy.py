# Boulderbot 1.5
# An IRC bot designed for Twitch.TV streams
# 
# Please see the README for instructions on using Twitchy.
# It is released under the BSD license; the full license
# available in the LICENSE file.

# CONFIGURATION
Twitch_Username = 'Boulderbot'  # Twitch.TV username for the bot, must be a registered username!
Twitch_Password = 'oauth:hsb3gwu5kvwv6oqm6z5aglrsiy51g6m'  # OAuth for above Twitch.TV account, http://www.twitchapps.com/tmi/
Twitch_Channel = 'raysfireispoopy'  # Twitch.TV channel to connect to

#I connect to raysfireispoopy to have a separate channel to test on

# NOW DON'T TOUCH ANYTHING ELSE, UNLESS YOU KNOW WHAT YOU'RE DOING

# If you do want to improve the code, though, feel free.
# I'd like if you then made a pull request on GitHub for everyone to
# benefit from the improved code, but you aren't required to do so.

import socket
import time
import imp
import os
import traceback
import re
import inspect
from threading import Thread
from plugins.BasePlugin import BasePlugin


class Twitchy:
    def __init__(self):
        print("Welcome to Boulderbot version 1.5!")
        self.ircSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ircServ = 'irc.twitch.tv'
        self.ircChan = '#'+ Twitch_Channel.lower()
        
        self.connected = False
        # Plugin system loosely based on blog post by lkjoel
        # http://lkubuntu.wordpress.com/2012/10/02/writing-a-python-plugin-api/
        self._pluginFolder = './plugins/'
        self._mainModule = 'plugin'
        self._plugins = [] #used for cleanup
        
        self.commands = []
        self.triggers = []
        self.joinPartHandlers = []
        self.modHandlers = []
        self.ignoredUsers = []
        self.loadedPluginNames = []
        self.spamMessages = ['codes4free.net', 'g2a.com/r/', 'prizescode.net']
    
    def kill(self): #changes all plugins to None, having no commands or triggers
        for p in self._plugins:
            p._kill()
    
    def sendMessage(self, message): #Sends message to the channel. Bread and butter stuff here
        self.ircSock.send(str('PRIVMSG %s :%s\n' % (self.ircChan, message)).encode('UTF-8'))
    
    def connect(self, port): #connects to IRC channel
        self.ircSock.connect((self.ircServ, port))
        self.ircSock.send(str("Pass " + Twitch_Password + "\r\n").encode('UTF-8'))
        self.ircSock.send(str("NICK " + Twitch_Username + "\r\n").encode('UTF-8'))
        self.ircSock.send(str("JOIN " + self.ircChan + "\r\n").encode('UTF-8'))
    
    def loadPlugins(self): #instantiates all the plugins in the plugin directory
        potentialPlugins = []
        allplugins = os.listdir(self._pluginFolder)
        for i in allplugins:
            location = os.path.join(self._pluginFolder, i)
            if not os.path.isdir(location) or not self._mainModule + ".py" in os.listdir(location):
                continue
            info = imp.find_module(self._mainModule, [location])
            potentialPlugins.append({"name": i, "info": info})
        
        print("Found plugin classes:")
        for i in potentialPlugins:
            try:
                plugin = imp.load_module(self._mainModule, *i["info"])
                pluginClasses = inspect.getmembers(plugin, inspect.isclass)
                for className, classObj in pluginClasses:
                    if className == "BasePlugin" or className in self.loadedPluginNames or not issubclass(classObj, BasePlugin):
                        continue #Exclude BasePlugin & any classes that are not a subclass of it
                    print(className)
                    pluginInstance = classObj(self)
                    self._plugins.append(pluginInstance)
                    self.loadedPluginNames.append(className)
            except Exception as e:
                print("Error loading plugin.")
                print(traceback.format_exc())

    ###The 4 types of functions the bot can look for
    ###Note, when registering in the plugin, self is excluded
    def registerCommand(self, command, pluginFunction): #to trigger, start message with "!<command> <arguments>" 
        self.commands.append( {'regex': command, 'handler':pluginFunction} )
    
    def registerTrigger(self, trigger, pluginFunction): #to trigger, include <trigger> in the message
        self.triggers.append( {'regex': trigger, 'handler':pluginFunction} )
    
    def registerForJoinPartNotifications(self, pluginFunction): #Automatically tracks users joining and leaving
        self.joinPartHandlers.append( pluginFunction )
    
    def registerForModNotifications(self, pluginFunction): #Automaticaly tracks moderators joining and leaving
        self.modHandlers.append( pluginFunction )
    
    def handleIRCMessage(self, ircMessage): #Reads and processes an IRC Message, looking for commands, triggers, etc
        if ircMessage.find(' PRIVMSG '+ self.ircChan +' :') != -1:
            nick = ircMessage.split('!')[0][1:]
            if nick.lower() in self.ignoredUsers: #return None if user is listed as an ignored user
                return
            msg = ircMessage.split(' PRIVMSG '+ self.ircChan +' :')[1]
            
            if re.search('^!ignore', msg, re.IGNORECASE): #return None if user is meant to be ignored, adds them to ignored users
                args = msg.split(" ")
                self.ignoredUsers.append(args[1])
                return
            
            for pluginDict in self.commands:
                if re.search('^!'+pluginDict['regex'], msg, re.IGNORECASE):
                    handler = pluginDict['handler']
                    args = msg.split(" ")
                    handler(nick, args)
            
            for pluginDict in self.triggers:
                if re.search('^'+pluginDict['regex'], msg, re.IGNORECASE):
                    handler = pluginDict['handler']
                    handler(nick, msg)
            
            for spam in self.spamMessages: #Timeout user that spams chat with a user-set spam message
                if re.search(spam, msg, re.IGNORECASE):
                    time.sleep(1) # Instant timeout might not be picked up by twitch web chat
                    self.sendMessage(".timeout " + nick + "\n")
                    print("Timed out " + nick + " for spam: " + spam + ". Message was: " + msg)
        
        elif ircMessage.find('PING ') != -1: #Responds to pings with pongs
            self.ircSock.send(str("PING :pong\n").encode('UTF-8'))
        
        elif ircMessage.find('JOIN ') != -1: #triggers joinpart handler(joining) if user joins
            nick = ircMessage.split('!')[0][1:]
            print(nick +" joined chat")
            for handler in self.joinPartHandlers:
                handler(nick, True)
        
        elif ircMessage.find('PART ') != -1: #triggers joinpart handler(parting if user leaves
            nick = ircMessage.split('!')[0][1:]
            print(nick +" left chat")
            for handler in self.joinPartHandlers:
                handler(nick, False)
        
        elif ircMessage.find('MODE '+ self.ircChan +' +o') != -1: #triggers modHandler(joining) if mod joins
            nick = ircMessage.split(' ')[-1]
            if nick.lower() != Twitch_Username.lower():
                print("Mod joined: "+nick)
                for handler in self.modHandlers:
                    handler(nick, True)
        
        elif ircMessage.find('MODE '+ self.ircChan +' -o') != -1: #triggers modHandler(parting) if mod leaves
            nick = ircMessage.split(' ')[-1]
            if nick.lower() != Twitch_Username.lower():
                print("Mod left: "+nick)
                for handler in self.modHandlers:
                    handler(nick, False)
        
        else: 
            print(ircMessage)
    
    def run(self):#here's where the magic happens
        line_sep_exp = re.compile(b'\r?\n')
        socketBuffer = b''
        while True:
            try:
                self.connected = True
                socketBuffer += self.ircSock.recv(1024)
                
                ircMsgs = line_sep_exp.split(socketBuffer)
                
                socketBuffer = ircMsgs.pop()
                
                # Deal with them
                for ircMsg in ircMsgs:
                    msg = ircMsg.decode('utf-8')
                    Thread(target=self.handleIRCMessage, args=(msg,)).start()
            except:
                raise
                

# 'main'
if __name__ == "__main__":
    while True:
        twitchy = Twitchy()
        try:
            twitchy.loadPlugins()
            twitchy.connect(6667)#connect to the irc server
            twitchy.run()#Make moves, son
        except Exception as e:
            print(traceback.format_exc())
        # If we get here, try to shutdown the bot then restart in 5 seconds
        twitchy.kill()
        time.sleep(5)
