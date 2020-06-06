
#This script that advertises a bluetooth low energy beacon for 15 seconds 
#penetaration example right here
#class libary using bluetooth in time


import time #<--- First part class moudle it manuiplues time 

from bluetooth.ble import BeaconService #<----  3rd party module

#create an instance of object from the 3rd party class

service - BeaconService() # service minus 3rd party module 



service.start_advertising("11111111-2222-3333-4444-555555555555",1,1,1,200)#<-- when call this accept UUIDs.# port, port, channel

time.sleep(15) #<--- low energy beacon for 15 seconds

service.stop_advertising()# <--- stop the bluetooth connection 

print("Done.") #<---  this is going to pop up on the screen saying done 
