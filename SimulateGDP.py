import random
# Python port of economic engine from Energy Finance Simulation (Wildcatter)
# Version 0.1 (alpha)
# Released by Matthew Blazewicz on February 15, 2021 under Apache License http://opensource.org/licenses/Apache-2.0

class economy():
    def __init__(self):
        #each increment of economyStateRemain is the equivalent of 1 quarter
        economyStateRemain = 0  #economyStateRemain = remaining time for current economic state
        economyStateLength = 16  #initial duration for current economic state
        economyState = "Bull Market"  #economyState = "Depression", "Bear Market", "Bull Market", "Boomtime"
        globalGDP = 87751541  #GDP starting point in $MM, see reference https://databank.worldbank.org/data/download/GDP.pdf
        globalGDP_Growthrate = 0.0221  #initial annual growth rate
        
        def simulate_GDP():
            if economyStateRemain == 0:
                rn1 = random.randint(1,100)
                if rn1 < 10:
                    economyState = "Depression"
                elif rn1 < 50:
                    economyState = "Bear Market"
                elif rn1 < 90:
                    economyState = "Bull Market"
                elif rn1 <= 100:
                    economyState = "Boomtime"
                economyStateLength = random.randint(4,16)
                economyStateRemain = economyStateLength
            if economyState == "Depression":
                rn2 = random.randint(1,100)
                globalGDP_Growthrate = (0 - (random.randint(1,100)/100))
            elif economyState == "Bear Market":
                rn2 = random.randint(1,100)
                globalGDP_Growthrate = (0 + (random.randint(1,100)/100))
            elif economyState == "Bull Market":
                rn2 = random.randint(1,100)
                globalGDP_Growthrate = (1 + (random.randint(1,100)/100))
            elif economyState == "Boomtime":
                rn = random.random.randint(1,100)
                globalGDP_Growthrate = (2 + (random.randint(1,100)/100))
            globalGDP = globalGDP + globalGDP * globalGDP_Growthrate / 4 / 100 #divided by 4 to account for each call simulating 1 quarter
            economyStateRemain -= 1
