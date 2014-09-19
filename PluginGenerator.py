#this is a command generator for boulderbot!

import os
import time

def makePlugin():
    np =input ("What is the name of the new plugin? ")
    print(os.listdir())
    time.sleep(1)
    #############################
    #you may need to change this#
    #depending on your file home#
    #############################
    os.chdir("C:\\Python34\\twitchy-master (1)\\Boulderbot master files\\plugins")
    print(os.listdir())
    time.sleep(1)
    os.mkdir(np)
    os.chdir(np)
    print(os.listdir())
    file = open("plugin.py", "w+")
    file.write("from plugins.BasePlugin import BasePlugin\n")
    file.write("class "+np+"Plugin(BasePlugin):\n")
    runMenu(file, np)

def runMenu(file, np):
    keepSwimming=True
    commandTriggers=[]
    while(keepSwimming):
        print("Select a command:")
        print("1. Call/Reply Generator")
        print("2. Advanced Commands")
        print("3. Custom Commands (Requires knowledge of Python)")
        print("4. Quit and compile Plugin")
        s=int(input("=> "))
        if s==1:
            newCommand=callGen(file)
            commandTriggers.append(newCommand)
        elif s==2:
            #advMenu(file)
            pass
        elif s==3:
            #customProcessor
            pass
        elif s==4:
            keepSwimming=False
        else:
            print("Invalid input. Enter a number in the range of 1-4")
    print(commandTriggers)
    compilePlugin(file, commandTriggers, np)
    
def callGen(file):
    command= input("Input the name of the command trigger: ")
    reply= input("Input the reply: ")
    print(command)
    file.write("\tdef %sHandler (self, nick, commandArg)\n" %(command))
    file.write("\t\tprint('!%s called by '+nick)\n" %(command))
    file.write("\t\tself.sendMessage('%s')\n\n" %(reply))
    return(command)

def compilePlugin (file, commandTriggers, np):
    file.write("\tdef __init__(self, twitchy):\n")
    file.write("\t\tsuper("+np+"Plugin, self).__init__(twitchy)\n\n")
    print("writing commands")
    print(commandTriggers)
    for command in commandTriggers:
        print("writing the %s plugin" %command)
        file.write("\t\tself.registerCommand('%s', self.%sHandler)\n" %(command, command))

#main
makePlugin()
