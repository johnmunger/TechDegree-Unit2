class Player:
    def __init__(self):
        self.name = ''
        self.guardians = []
        self.experience = False
        self.height = 0

    # Getter for name
    def getName(self):
        return self.name

    # Setter for name
    def setName(self, value):
        self.name = value

    # Getter for guardians
    def getGuardians(self):
        return self.guardians

    # Setter for guardians
    def setGuardians(self, value):
        self.guardians = value

    # Getter for experience
    def getExperience(self):
        return self.experience

    # Setter for experience
    def setExperience(self, value):
        self.experience = value

    # Getter for height
    def getHeight(self):
        return self.height

    # Setter for height
    def setHeight(self, value):
        self.height = value
