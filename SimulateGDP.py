import random
# Python port of economic engine from Energy Finance Simulation (Wildcatter)
# Version 0.1 (alpha)
# Released by Matthew Blazewicz on February 15, 2021 under Apache License http://opensource.org/licenses/Apache-2.0

class economy():
    def __init__(self):
        #each increment of economyStateRemain is the equivalent of 1 quarter
        self.economyStateRemain = 15  #economyStateRemain = remaining time for current economic state
        self.economyStateLength = 16  #initial duration for current economic state
        self.economyState = "Bull Market"  #economyState = defines one of four potential economic states
        self.globalGDP = 87751541  #GDP starting point in $MM, see reference https://databank.worldbank.org/data/download/GDP.pdf
        self.globalGDPGrowthRate = 0.0221  #initial annual growth rate
        self.rn1 = random.randint(1,100)
        
    def simulateGDP(self):
        self.globalGDP = self.globalGDP + self.globalGDP * self.globalGDPGrowthRate / 4 / 100 #divided by 4 to account for each call simulating 1 quarter
        self.economyStateRemain = self.economyStateRemain - 1
        
        if self.economyStateRemain == 0:
            self.rn1 = random.randint(1,100)
            if self.rn1 < 10:
                self.economyState = "Depression"
            elif self.rn1 < 50:
                self.economyState = "Bear Market"
            elif self.rn1 < 90:
                self.economyState = "Bull Market"
            elif self.rn1 <= 100:
                self.economyState = "Boomtime"
            self.economyStateLength = random.randint(4,16)
            self.economyStateRemain = self.economyStateLength
        if self.economyState == "Depression":
            self.rn2 = random.randint(1,100)
            self.globalGDPGrowthRate = (0 - (random.randint(1,100)/100))
        elif self.economyState == "Bear Market":
            self.rn2 = random.randint(1,100)
            self.globalGDPGrowthRate = (0 + (random.randint(1,100)/100))
        elif self.economyState == "Bull Market":
            self.rn2 = random.randint(1,100)
            self.globalGDPGrowthRate = (1 + (random.randint(1,100)/100))
        elif self.economyState == "Boomtime":
            self.rn = random.randint(1,100)
            self.globalGDPGrowthRate = (2 + (random.randint(1,100)/100))
        

