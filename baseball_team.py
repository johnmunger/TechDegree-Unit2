from team_stats import TeamStats

class BaseballTeam:
    leagueAverageHeight = 0
    def __init__(self, name):
        self.name = name
        self.players = []
        self.teamStats = {
            "totalPlayers":0,
            "totalExperienced":0,
            "totalInexperienced":0,
            "averageHeight":0
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
            self.teamStats['totalPlayers'] += 1
            self.teamStats['averageHeight'] += player.getHeight()
            if (player.getExperience()):
                self.teamStats['totalExperienced'] += 1
            else:
                self.teamStats['totalInexperienced'] += 1
            
                
        self.teamStats['averageHeight'] /= self.teamStats['totalPlayers']

    def displayTeamStats(self):
        # Code to display team stats
        for key, value in self.getTeamStats().items():
            print(f'{key}: {value}')
        self.playersOnTeam()
        self.guardiansOnTeam()

    def playersOnTeam(self):
        # Code to retrieve players on a team 
        # 
        printStr = '' 
        for i in range(len(self.players)):
            name = self.players[i].getName()
            lastIndex = len(self.players)-1
            if(i != lastIndex):
                printStr += name + ", "
            else:
                printStr += name  
        print(f"Players: {printStr} \n\n")

    def guardiansOnTeam(self):
        # Code to retrieve guardians on a team
        nameList=[]
        printStr = '' 
        for player in self.players:
            guardians = player.getGuardians()
            for guardian in guardians:
                nameList.append(guardian)
        for i in range(len(nameList)):
            lastIndex = len(nameList)-1
            if(i != lastIndex):
                printStr += nameList[i] + ", "
            else:
                printStr += nameList[i] + "\n\n"

        print(f"Guardians: {printStr} \n\n")