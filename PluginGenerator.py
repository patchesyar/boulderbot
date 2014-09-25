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
    file.write("import random\n")#Might not be used but this jankmaster program will work best if I do this
    file.write("class "+np+"Plugin(BasePlugin):\n")
    runMenu(file, np)

def runMenu(file, np):
    keepSwimming=True
    commandTriggers=[] #list of all the command triggers
    externalities=[] #list of external class attributes (for raffles, preds, etc)
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
            newCommands,externals=advMenu(file)
            commandTriggers.extend(newCommands)
            if externals is not None:
                externalities.extend(externals)
            pass
        elif s==3:
            #customProcessor
            pass
        elif s==4:
            keepSwimming=False
        else:
            print("Invalid input. Enter a number in the range of 1-4")
    print(commandTriggers)
    compilePlugin(file, commandTriggers, np, externalities)

######################
### CALL GENERATOR ###
######################
def callGen(file):
    command= input("Input the name of the command trigger: ")
    reply= input("Input the reply: ")
    reply=reply.replace('"', "\\\"")
    reply=reply.replace("'", "\\\'")
    print(command)
    file.write("\tdef %sHandler (self, nick, commandArg):\n" %(command))
    file.write("\t\tprint('!%s called by '+nick)\n" %(command))
    file.write("\t\tself.sendMessage('%s')\n\n" %(reply))
    return(command)

######################
### COMPILE PLUGIN ###
######################
def compilePlugin (file, commandTriggers, np, externalities): #TODO: write in any attributes
    file.write("\tdef __init__(self, twitchy):\n")
    file.write("\t\tsuper("+np+"Plugin, self).__init__(twitchy)\n\n")
    print("writing commands")
    print(commandTriggers)
    for command in commandTriggers:
        print("writing the %s plugin" %command)
        file.write("\t\tself.registerCommand('%s', self.%sHandler)\n" %(command, command))
    for attribute in externalities:
        print("Writing the %s Attribute"%attribute)
        file.write("\t\tself.%s\n"%attribute)


######################
###  ADVANCED MENU ###
######################
def advMenu (file):
    print("Select the premade function to create:")
    print("1. Raffle")
    print("2. Predictions")
    print("3. I changed my mind, return to the main menu!")
    readIn=int(input("=> "))
    newCommands=[]
    externals=[]
    if readIn==1:
        newCommands,externals=raffleGen(file)
    elif readIn==2:
        #newCommands(predGen(file))
        pass
    else:
        pass
    return (newCommands,externals)

########################
### RAFFLE GENERATOR ###
########################
def raffleGen(file):
    #SO MANY VARIABLES
    command=input("What is the name of your raffle trigger? ")
    confirmation=input("Do you want to print a confirmation message on entry? ")
    listUsers=input("Input a command to list entered users: ")
    startRaffle=input("Input a command to start the raffle: ")
    endRaffle=input("Input the command to end the raffle: ")
    name="blah"
    names=[]
    while name is not "":
        name=input("Input the nick of a user that can moderate the raffle or nothing to continue: ")
        if name is not "":
            names.append(name)
    confirmUsersB=False
    if confirmation.lower()=="yes" or confirmation.lower()=="y":
        confirmUsersB=True
    #compile raffle command
    raffleList=("%sList"%command) #List of users entered in raffle
    raffleOn=("%sEnabled"%command) #class attribute that enables/disables raffle
    externals=["raffleOn=False", raffleList+"= []"] #attributes to be added to the class
    newCommands=[command+"Starter", command+"Ender", command+"Lister", command+"Enterer"] #I officially hate Raffles
    ###Raffle Starter###
    file.write("\tdef %sStarter (self, nick, commandArg):\n" % command)
    file.write("\t\tprint('%sStarter called by '+nick)\n" % command)
    for i in range(len(names)):
        if i==0:
            file.write("\t\tif nick == '%s' "%names[i])
        else:
            file.write("or nick == '%s' "%names[i])
    file.write(":\n\t\t\tprint('this raffle is enabled')\n")
    file.write("\t\t\traffleOn=True\n\n")
    ###Raffle Ender###
    file.write("\tdef %sEnder (self, nick, commandArg):\n" % command)
    file.write("\t\tprint('%sEnder called by '+nick)\n" % command)
    for i in range(len(names)):
        if i==0:
            file.write("\t\tif nick == '%s' "%names[i])
        else:
            file.write("or nick == '%s' "%names[i])
    file.write(":\n\t\t\tprint('this raffle is disabled')\n")
    file.write("\t\traffleOn=False\n")#Disable Raffle Entering, choose a winner
    file.write("\t\twinner=random.randint(0,%sList.size)\n"%command)
    file.write("\t\tself.sendMessage(%sList[winner]+' has won the raffle')\n\n"%command)
    ###Raffle Lister###
    file.write("\tdef %sLister (self, nick, commandArg):\n" % command)
    file.write("\t\tprint('%sLister called by '+nick)\n" % command)
    file.write("\t\tself.sendMessage(str(len(%sList))+'people have entered the raffle')\n\n"%command)
    ###Raffle Enterer###
    file.write("\tdef %sEnterer (self, nick, commandArg):\n"%command)
    file.write("\t\tif %sEnabled:\n"%command)
    file.write("\t\t\tmakeEntry=True\n")
    file.write("\t\t\tfor element in %sList:\n"%command)
    file.write("\t\t\t\tif element==nick:\n")
    file.write("\t\t\t\t\tmakeEntry=false\n")
    file.write("\t\t\tif makeEntry:\n")
    file.write("\t\t\t\t%sList.append(nick)\n"%command)
    if confirmUsersB:
        file.write("\t\t\t\tself.sendMessage(nick+'has entered the raffle, type !%s to enter')\n\n"%command)
    return newCommands, externals
        


#main
makePlugin()
