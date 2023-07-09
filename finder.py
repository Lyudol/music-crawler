import fetch
import html_to_json
import json
import time
import math
from threading import Thread
#tracks = jsonified["html"][0]["body"][0]["div"][1]["div"][0]["div"][1]["div"][0]["div"][0]["div"][0]["div"][1]["div"][0]["div"][0]["div"][1]["div"][0]["div"][0]["ul"][0]["li"] for all tracks
#tracks[8]["div"][0]["div"][0]["img"][0]["_attributes"]["alt"] for each name

drivers = [fetch.driverfinder1,fetch.driverfinder2,fetch.driverfinder3,fetch.driverfinder4,fetch.driverfinder5]


def opensite(website,drivertouse):
    fetch.openfinderwebsite(website,drivertouse)

def getjson(drivertouse):
    html = fetch.pagesource(drivertouse)
    jsonified = html_to_json.convert(html)

    towrite = jsonified
    f = open("json"+str(drivers.index(drivertouse))+".txt", "w")
    f.write(json.dumps(towrite))
    f.close()

def gettracks(drivertouse):
    with open("json"+str(drivers.index(drivertouse))+".txt", "r") as file:
                jsonified = file.read()
                jsonified = json.loads(jsonified)

    tracks = jsonified["html"][0]["body"][0]["div"][1]["div"][0]["div"][1]["div"][0]["div"][0]["div"][0]["div"][1]["div"][0]["div"][0]["div"][1]["div"][0]["div"][0]["ul"][0]["li"]
    return tracks

def getsong(tracks, tracknumber):
    name = tracks[tracknumber]["div"][0]["div"][0]["img"][0]["_attributes"]["alt"]
    song = "".join(list(name)[:-12])
    return song


def findtoadd(tracks):
    tracknumber = 0
    found = []

    for track in tracks:
            if "div" in track["div"][0]["div"][0].keys():
                    
                    print(getsong(tracks,tracknumber))
                    found.append(getsong(tracks,tracknumber))
                    tracknumber += 1
            else:
                    tracknumber +=1
    return found

def getter(drivertouse):
    for i in range(3):
        fetch.load(drivertouse)        # loads thrice
        
    getjson(drivertouse)               # gets json of page
    tracks = gettracks(drivertouse)    # gets all tracks
    found = findtoadd(tracks) # finds ones that needs lyrics
    return found #returns


def main(drivertouse,terms):
    opensite("https://www.musixmatch.com/search/tracks",drivertouse)
    fetch.clickcookie(drivertouse)
    for term in terms:   # searches each letter
        opensite("https://www.musixmatch.com/search/" + term + "/tracks", drivertouse)
        found = getter(drivertouse)
        file = open('songsfound.txt','a', encoding="utf-8")             # adds lyric to add to file
        for song in found:
            file.write(song+"\n")
        file.close()
          

#n = amount of drivers


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


wordfile = open("words.txt", "r")
data = wordfile.read()
lst = data.split("\n")



chunkedlist = list(chunks(lst,int(math.ceil(len(lst)/len(drivers)))))




Thread(target=main, args=(drivers[0],chunkedlist[0],)).start()
Thread(target=main, args=(drivers[1],chunkedlist[1],)).start()
Thread(target=main, args=(drivers[2],chunkedlist[2],)).start()
Thread(target=main, args=(drivers[3],chunkedlist[3],)).start()
Thread(target=main, args=(drivers[4],chunkedlist[4],)).start()