from constants import TEAMS, PLAYERS
from league import League
def menuUI(league):
    menuText=[
        "---- Menu ----\n\n",
        "Here are your choices:\n",
        "   A) Display Team Stats",
        "   B) Quit",
        "Enter an Option:"
        ]
    for i in range(4):
        print(menuText[i])
    action = input(menuText[4])
    if (action == 'B'):
        return False
    else:
        for i in range(len(league.teams)):
            j = i+1
            print(f"{j}. {league.teams[i].getName()}\n\n")
        selection = int(input('Please select an index:  '))
        teams = league.getTeams()
        teams[selection-1].displayTeamStats()
        return True

def main():
    active = True
    league = League()
    league.importLeague(PLAYERS)
    league.draftTeams(TEAMS)
    while active:
        active = menuUI(league)

if __name__ == "__main__":
    main()