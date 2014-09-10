from plugins.BasePlugin import BasePlugin

songlist=[]
    


class PyHeroPlugin(BasePlugin):
        def __init__(self, twitchy):
                super(PyHeroPlugin, self).__init__(twitchy)

                self.registerCommand('herorequest', self.pusher)
                self.registerCommand('pop', self.popper)

        def pusher(self, nick, commandArg):
            global songlist
            if len(commandArg)==1:
                self.sendMessage("Don't forget to add the song request!")
            else:
                newword=""
                for i in range(1, len(commandArg)):
                        if i==len(commandArg):
                                newword+=(commandArg[i])
                        else:
                                newword+=(commandArg[i]+" ")
                if newword in songlist:
                    self.sendMessage(newword+" has already been requested")

                isin=False
                for line in open("songlist.txt"):
                        if request==line:
                                isin=True
                
                if isin:
                    songlist.append(newword)
                    self.sendMessage(nick+" has requested "+ newword)
                    print(songlist)
                else:
                    self.sendMessage(newword+"is not a valid request. Check your spelling or contact tomdiamond if this is wrong")

        def popper(self, nick, commandArg):
            global songlist
            if nick=="tomdiamond" or nick=="raysfire":
                print(nick+" has popped")
                if songlist==[]:
                    self.sendMessage("There are no pending requests")
                else:
                    strin=songlist[0]
                    if len(songlist)!=1:
                        songlist=songlist[1:]
                    if len(songlist)==1:
                        songlist=[]
                    self.sendMessage("The next request is "+strin)
                    print(songlist)
