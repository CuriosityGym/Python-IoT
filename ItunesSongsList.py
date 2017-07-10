import re
songsFile=open("songs.txt","r")
songs=songsFile.read()
songsMatch=re.findall(r"\w+,\d+:\d+,\d+", songs)

#print(songsMatch)
songsData=[]
for song in songsMatch:
    songsData.append(song.split(","))

#print(songsData)

hListenedName=""
hListenedTime=0

totalTime=0
for songData in songsData:
    durationSplit=songData[1].split(":")
    duration=int(durationSplit[0])*60 +int(durationSplit[1])
    played=int(songData[2])
    if(played>hListenedTime):
        hListenedTime=played
        hListenedName=songData[0]
    totalTime=totalTime+duration*played
    #totalTimeHours=totalTime/3600
    #totalTimeMinutes=
    
#print(totalTime)

m, s = divmod(totalTime, 60)
h, m = divmod(m, 60)
print ("Your Songs Collection is %d:%02d:%02d Long" % (h, m, s))
print("You have Listened to " + hListenedName + " " + str(hListenedTime) + " times" )    
    
