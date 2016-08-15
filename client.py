import network
import sys
import androidhelper

droid=androidhelper.Android()
string="f"
last=string
#run=True
def heard(phrase):
  print("User:" + phrase)

if (len(sys.argv) >= 2):
  network.call(sys.argv[1], whenHearCall=heard)
else:  
  network.wait(whenHearCall=heard)

droid.startSensingTimed(2,500)
while network.isConnected():
  #phrase= input()
  x=droid.sensorsReadAccelerometer().result[0]
  y=droid.sensorsReadAccelerometer().result[1]
  z=droid.sensorsReadAccelerometer().result[2]
  
  magnitude=6.5
  if(x<-magnitude):
    string="w"
    if(last!=string):
      last="w"
      network.say("w")

  elif(x>magnitude):
    string="s"
    if(last!=string):
      last="s"
      network.say("s")

  elif(y<-magnitude):
    string="a"
    if(last!=string):
      last="a"
      network.say("a")
  elif(y>magnitude):
    string="d"
    if(last!=string):
      last="d"
      network.say("d")
  else:
    string="f"
    if(last!=string):
      last="f"
      network.say("f")
  #if(phrase=="stop"):
    #run=False
    #network.say("f")
  
      
droid.stopSensing()