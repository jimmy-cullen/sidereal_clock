import ephem, datetime, math, time
#import matplotlib.pyplot as plt
#import numpy as np


# Define some values
observer_lat  = '52:14:10'
observer_long = '-02:18:26'

midnight_today = datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time())


#Create an Observer with JBO Coordinates and today's date
jb = ephem.Observer()
jb.lat  = observer_lat
jb.long = observer_long
jb.date = midnight_today

#print "LST at midnight UT: " + str(jb.sidereal_time())

while True:
    jb.date = ephem.now()
    #print(type(jb))
    print ("UTC:" + '\t\t' + str(time.strftime('%H:%M:%S',time.gmtime())))
    print ("Sidereal time:" + '\t' + str(jb.sidereal_time()))
    #print (time.time().strftime('%H%M%S'))
    time.sleep(1)

