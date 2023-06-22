class BasketballTeam:
    leagueAverageHeight = 0
    def __init__(self, name):
        self.name = name
        self.players = []
        self.teamStats = {
            "Total Players":0,
            "Total Experienced":0,
            "Total Inexperienced":0,
            "Average Height":0
            }

    # Getter for players
    def getName(self):
        return self.name
    def getPlayers(self):
        return self.players
    # Setter for players
    def addPlayer(self, value):
        self.players.append(value)

    # Getter for teamStats
    def getTeamStats(self):
        return self.teamStats

    # Setter for teamStats
    def setTeamStats(self):
        for player in self.players:
            self.teamStats['Total Players'] += 1
            self.teamStats['Average Height'] += player.getHeight()
            if (player.getExperience()):
                self.teamStats['Total Experienced'] += 1
            else:
                self.teamStats['Total Inexperienced'] += 1
            
                
        self.teamStats['Average Height'] /= self.teamStats['Total Players']
        self.teamStats['Average Height'] = round(self.teamStats['Average Height'], 1)

    def displayTeamStats(self):
        # Code to display team stats
        for key, value in self.getTeamStats().items():
            print(f'{key}: {value}\n')
        self.playersOnTeam()
        self.guardiansOnTeam()

    def playersOnTeam(self):
        # Code to retrieve players on a team 
        # 
        playersDict= {}
        for i in range(len(self.players)):
            playersDict[self.players[i].getName()] = self.players[i].getHeight()

        sortedData = {k:v for k,v in sorted(playersDict.items(), key=lambda item: item[1])}

        printStr=""
        for tuple in sortedData.items():
            printStr += f"{tuple[0]}, "

        print(f"Players(shortest-tallest): {printStr} \n")

    def guardiansOnTeam(self):
        # Code to retrieve guardians on a team
        nameList=[]
        printStr = "" 
        for player in self.players:
            guardians = player.getGuardians()
            for guardian in guardians:
                nameList.append(guardian)
        for i in range(len(nameList)):
            printStr += f"{nameList[i]}, "

        print(f"Guardians: {printStr} \n")