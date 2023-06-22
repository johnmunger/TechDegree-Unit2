# Basketball Team Stats Tool
In this project you will be writing a program that reads from the "constants" data (`PLAYERS` and `TEAMS`) in `constants.py`. This data will need to be translated into a new collection of your choosing and the fields need to be changed to something that makes more sense for Python to do its comparisons.


**NOTE**: Python has no concept of actual constants like some other languages out there. But it is a convention in Python to treat ALL CAPS variables as if they are in-fact constants.


**Steps to get started:**

1. Create a new empty script file called `app.py` or `application.py`

2. Inside this new file, you will want a Dunder Main statement:
   For a refresh on Dunder Main:
   https://teamtreehouse.com/library/understanding-dunder-main-main

3. Any print statements or function calls you will want to be inside Dunder Main or inside a main function call which is nested inside Dunder Main.
   If you need a refresh, check out the supplied Project 1 files/workspace for an example.
   


If you get stuck, try to work through the problem. Sometimes it helps to try to write/draw out your steps on paper in the order your program should run in and solve each step 1 at a time. If you are still stuck be sure to reach out in the Python Techdegree #unit-02 Slack channel.

## Initial Solution Design

* clean the data
* Store it somewhere
* Distribute the players fairly(determined by experience)
* Make a UI
   - A - Display Team Stats
   - B - Quit

   *if Display Team Stats*
   - A - Panthers
   - B - Bandits
   - C - Warriors

## Control Structure

I basically followed my initial solution design, this didn't feel amenable to same kind of analysis as problem one since the the application state is so simple.  We are either displaying data or we are not.  The rest is just data organization.  I abstracted out the parts that I could to keep the code more readable. If you start at main read down you naturally can read the structure.


### Pre User Input
* Create League
* Import Players into the League
* Calculate stats from the League
* Drafts the Leagues Teams
* Then starts the MenuUI

MenuUI Function is called until it returns false, which results in exiting the program

### Menu UI

Menu UI has two sequential while loops - one for each in input statement.  The program executes until false is returned by menuUI function in the first while loop

## Classes
Starting with the most basic constituents elements and working our way up.

### Player
We start with the player. The play has all the attributes outlined in our CONSTANT arrays.
* name
* guardians
* experience
* height

This class is straight forward object with getter/setters

### BasketballTeam
It keeps track of the team level info
* name
* players
* teamStats dict

Getter/Setter functions

### League
The two members here are the results of the clean and import of the data in constants.py
* league - a team with all the players in the league
* teams - a list of team names

I added add suspense and deliberating to try to make this seem more fun


