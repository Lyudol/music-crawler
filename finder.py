import fetch
import html_to_json
import json
import time
#tracks = jsonified["html"][0]["body"][0]["div"][1]["div"][0]["div"][1]["div"][0]["div"][0]["div"][0]["div"][1]["div"][0]["div"][0]["div"][1]["div"][0]["div"][0]["ul"][0]["li"]
# tracks[8]["div"][0]["div"][0]["img"][0]["_attributes"]["alt"] for each name

fetch.openwebsite("https://www.musixmatch.com/search/a/tracks")

def getjson():
    html = fetch.driver.page_source
    jsonified = html_to_json.convert(html)

    towrite = jsonified
    f = open("testing.txt", "w")
    f.write(json.dumps(towrite))
    f.close()

def gettracks():
    with open("testing.txt", "r") as file:
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

    for track in tracks:
            if "div" in track["div"][0]["div"][0].keys():
                    
                    print(getsong(tracks,tracknumber),tracknumber)
                    tracknumber += 1
            else:
                    tracknumber +=1

def loadmore(amount):
    for i in range(amount):
        fetch.load()
        time.sleep(2)


def main():
       fetch.clickcookie()
       getjson()
       tracks = gettracks()
       findtoadd(tracks)
    

loadmore(3)
main()
