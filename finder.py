import fetch
import html_to_json
import json
import time
#tracks = jsonified["html"][0]["body"][0]["div"][1]["div"][0]["div"][1]["div"][0]["div"][0]["div"][0]["div"][1]["div"][0]["div"][0]["div"][1]["div"][0]["div"][0]["ul"][0]["li"] for all tracks
#tracks[8]["div"][0]["div"][0]["img"][0]["_attributes"]["alt"] for each name


def opensite(website):
    fetch.openwebsite(website)

def getjson():
    html = fetch.driver.page_source
    jsonified = html_to_json.convert(html)

    towrite = jsonified
    f = open("json.txt", "w")
    f.write(json.dumps(towrite))
    f.close()

def gettracks():
    with open("json.txt", "r") as file:
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

def main():
    for i in range(3):
        fetch.load()        # loads thrice
        time.sleep(2)
    getjson()               # gets json of page
    tracks = gettracks()    # gets all tracks
    found = findtoadd(tracks) # finds ones that needs lyrics
    return found #returns

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  
for letter in alphabet:   # searches each letter
    opensite("https://www.musixmatch.com/search/" + letter + "/tracks")
    found = main()
    file = open('songsfound.txt','a', encoding="utf-8")             # adds lyric to add to file
    for song in found:
        file.write(song+"\n")
    file.close()
          
