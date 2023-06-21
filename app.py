from constants import TEAMS, PLAYERS
from league import League
def menuUI(league):
    menuText=[
        "---- Menu ----\n",
        "Here are your choices:\n",
        "   A) Display Basketball Team Stats",
        "   B) Quit\n",
        "Enter an Option:  "
        ]
    for i in range(4):
        print(menuText[i])
    while True:
        try:
            action = input(menuText[4])
            if action.upper() not in ['A','B']:
                raise ValueError("Please enter either A or B")
            if (action.upper() == 'B'):
                return False
            break
        except ValueError as e:
            print(e)
    options = "ABC"
    for i in range(len(options)):
        print(f"{options[i]}. {league.teams[i].getName()}\n")
    while True:
        try:
            selection = input('Please select a team: ')
            selectionsDictionary = {"A":0,"B":1,"C":2}
            teams = league.getTeams()
            if selection.upper() not in ['A','B','C']:
                raise ValueError("Invalid Selection. Please select A, B, or C.") #raising error if invalid option is selected
            team = teams[selectionsDictionary[selection.upper()]]
            statsHeader = ['#########################',
                            f'        {team.getName()}       ',
                            '#########################']
            for i in range(len(statsHeader)):
                print(statsHeader[i])
            team.displayTeamStats()
            break # break the loop once valid input is given.
        except ValueError as e:
            print(e)
    return True

def main():
    active = True
    theWholeLeague = League()
    theWholeLeague.importLeague(PLAYERS)
    theWholeLeague.getLeague().setTeamStats()
    theWholeLeague.getLeague().leagueAverageHeight = theWholeLeague.getLeague().getTeamStats()['Average Height']
    theWholeLeague.draftTeams(TEAMS)
    while active:
        active = menuUI(theWholeLeague)

if __name__ == "__main__":
    main()