from baseball_team import BaseballTeam
from player import Player
from time import sleep
from random import randint

def deliberating(total, width=15):
    for progress in range(1, total + 1):
        sleep(0.1)  # Simulate some work being done
        
        # Calculate the percentage completed
        percentage = int(progress / total * 100)
        
        # Calculate the number of filled and empty slots in the progress bar
        filledWidth = int(width * progress / total)
        emptyWidth = width - filledWidth
        
        # Print the progress bar
        print(f"[{'=' * filledWidth}{' ' * emptyWidth}] {percentage}%", end='\r')
        
    print("\n\n")

def addSuspense(team, player, index):
    print(f"The {team} choose to draft\n\n")
    deliberating(randint(10,45-index*3))
    print(f"{player}!!!\n\n")

class League:
    def __init__(self):
        self.league = BaseballTeam('League')
        self.teams = []

    def getLeague(self):
        return self.league

    def getTeams(self):
        return self.teams

    def importLeague(self, players):
        # Code to import the league data and create BaseballTeam instances
        # For each in players create a player and add it to league

        for player in players:
            # unpack Player
            self.readyPlayer(**player)
            

    def draftTeams(self, teamNames):
        # Code to distribute players fairly based on experience

        experiencedPlayers = []
        inexperiencedPlayers = []
        for player in self.league.getPlayers():
            if player.getExperience() == True:
                experiencedPlayers.append(player)
            else:
                inexperiencedPlayers.append(player)

        for team in teamNames:
            self.teams.append(BaseballTeam(team))

        for i in range(len(experiencedPlayers)):
            playerName = experiencedPlayers[i].getName()
            r = i%3
            team = self.teams[r].getName()
            if(r == 0):
                addSuspense(team, playerName, i)
                self.teams[0].addPlayer(experiencedPlayers[i])
            elif(r == 1):
                addSuspense(team, playerName, i)
                self.teams[1].addPlayer(experiencedPlayers[i])
            else:
                addSuspense(team, playerName, i)
                self.teams[2].addPlayer(experiencedPlayers[i])
        
        for i in range(len(inexperiencedPlayers)):
            playerName = inexperiencedPlayers[i].getName()
            r = i%3
            team = self.teams[r].getName()
            if(i % 3 == 0):
                addSuspense(team, playerName, i)
                self.teams[0].addPlayer(inexperiencedPlayers[i])
            elif(i % 3 == 1):
                addSuspense(team, playerName, i)
                self.teams[1].addPlayer(inexperiencedPlayers[i])
            else:
                addSuspense(team, playerName, i)
                self.teams[2].addPlayer(inexperiencedPlayers[i])

        for team in self.teams:
            team.setTeamStats()

    def teamSelect(self, teamSelection):
        # Code to select and display teams stats
        if(teamSelection.upper()=="A"):
            self.teams
        pass
    
    def readyPlayer(self, name, guardians, experience, height):
        experience = True if experience =='YES' else False
        draftee = Player()
        draftee.setName(name)
        draftee.setGuardians(guardians.split(' and '))
        draftee.setExperience(experience)
        draftee.setHeight(round(int(height[:2]), ))
        self.league.addPlayer(draftee)