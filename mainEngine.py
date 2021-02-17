import random
from SimulateGDP import economy
import SimulateGDP
import threading
import time

### main engine loop ###

def mainEngine():
  worldFin = economy()
  simSpeed = 1 #simulation step speed in seconds
  counter = 60 #number of seconds to run the main engine
  t_end = time.time() + counter #sets a stop time equal to mainEngine initiation time stamp + counter seconds
  
  while time.time() < t_end:
    #function calls to simulate GDP and display a dashboard
    worldFin.simulateGDP()
    displayDashboard(worldFin)
    time.sleep(1)

  # threading.Timer(1,mainEngine).start
  
  
  
 
def displayDashboard(self):
  print(self.economyState + " GDP: " + str(round(self.globalGDP,2)) + " state remain: " + str(self.economyStateRemain))
  
mainEngine()