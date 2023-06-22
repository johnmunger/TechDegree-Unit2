from constants import TEAMS, PLAYERS
from league import League

def openingMenuText():
    menuText=[
    "---- Menu ----\n",
    "Here are your choices:\n",
    "   A) Display Basketball Team Stats",
    "   B) Quit\n"
    ]
    for i in range(len(menuText)):
        print(menuText[i])

def printStats(team):
    statsHeader = ['#########################',
                f'        {team.getName()}       ',
                '#########################']
    for i in range(len(statsHeader)):
        print(statsHeader[i])
    team.displayTeamStats(team.leagueAverageHeight)

def ifOptionAPrintTeamSelection(league):
    options = "ABC"
    for i in range(len(options)):
        print(f"{options[i]}. {league.teams[i].getName()}\n")

def menuUI(league):
    openingMenuText()
    while True:
        try:
            action = input('Please select an option:')
            if action.upper() not in ['A','B']: #I originally used 'AB', but that apparently include '' so hitting enter didn't raise an exception
                raise ValueError("Please enter either A or B")
            if (action.upper() == 'B'):
                return False
            break
        except ValueError as e:
            print(e)

    ifOptionAPrintTeamSelection(league)
    
    while True:
        try:
            selection = input('Please select a team: ')#get team name option
            teams = league.getTeams()
            if selection.upper() not in ['A','B','C']:#same as above
                raise ValueError("Invalid Selection. Please select A, B, or C.") #raising error if invalid option is selected
            team = teams[(lambda x: ord(x.upper()) - ord('A'))(selection)]#this saves declaring a dictionary to simply map user's string input to index integer
            printStats(team)
            break # break the loop once valid input is given.
        except ValueError as e:
            print(e)
    return True

def main():
    active = True
    theWholeLeague = League()
    theWholeLeague.importLeague(PLAYERS)
    theWholeLeague.getLeague().setTeamStats()
    theWholeLeague.getLeague().setLeagueAverageHeight(theWholeLeague.getLeague().getTeamStats()['Average Height'])
    theWholeLeague.draftTeams(TEAMS)
    while active:
        active = menuUI(theWholeLeague)

if __name__ == "__main__":
    main()