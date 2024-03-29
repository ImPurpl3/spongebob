import os
import tkinter as tk
import json
import sys

from tkinter.filedialog import askdirectory
from tmdbv3api import TMDb, TV, Season
from difflib import SequenceMatcher

runpath = os.path.dirname(sys.argv[0])    # get path from where script is running
tokenfile = open(f'{runpath}/token.json') # open token json file
tokendata = json.load(tokenfile)          # load token json file

# set the movie database variables
tmdb = TMDb()
tmdb.api_key = tokendata["TOKEN"]
tv = TV()
seas = Season()

# use tkinter to open folder select gui
tk.Tk().withdraw()
path = askdirectory()
pp1 = os.path.basename(path)
seasnum = pp1.replace("Season ", "") # get season number from folder selection

ss = seas.details("387",seasnum) # get tmdb details for that season of spongebob

properEPdict = {} # init the dictionary
for l in ss.episodes: # for each entry in the episodes for that season of bob l'eponge
    epname = l.name          # episode name
    epnum = l.episode_number # episode number
    ssnum = l.season_number  # season number
    renamed = f"SpongeBob SquarePants - s{ssnum:02}e{epnum:02} - {epname}" # text model for renaming
    properEPdict[f"{epname}"] = renamed # in the dictionary for the tmdb side of comparing,
                                        # make entry for episode name and make it equal the proper model for renaming

sortedProperDict = dict(sorted(properEPdict.items())) # sort dict to make it easier to match later

seasStr = f"Season {ssnum}"

epdict = {} # init local side dictionary
for filename in os.listdir(path):    # for each episode in the season:
    f = os.path.join(path, filename) # lose 168 brain cells
    fl = os.path.splitext(filename)  # get file extension
    ff = fl[0]                       # get file name

    if os.path.isfile(f) and seasStr in ff: # lose 24 more brain cells; run through if file and if wrong format is detected
        #print(f"Found Wrong Format! - {ff}")
        epname = ff[35:]  # remove first 35 characters of filename (because they were named "SpongeBob Squarepants - Season x - episodename.avi")
        epfile = f"{path}/{filename}" # setup file name to match episode name
        epdict[f"{epname}"] = epfile  # file name match to episode name

print(epdict)
print(epdict.keys())

for key in sortedProperDict.keys():
    #print(f"On index: {key}")
    maxMatchRatio = 0
    maxMatchKey = ""
    for dbkey in epdict.keys():
        matchRatio = SequenceMatcher(None, key, dbkey).ratio()

        if matchRatio > maxMatchRatio:
            maxMatchRatio = matchRatio
            maxMatchKey = dbkey

    if maxMatchRatio >= 0.75 and maxMatchKey in epdict.keys():
        print(f"New Match! : {key} - {maxMatchKey} @ {maxMatchRatio}")
        pth, filenm = os.path.split(epdict[maxMatchKey]) # split path and file name
        fleext = os.path.splitext(epdict[maxMatchKey])   # file extension
        correctFileName = f"{pth}/{sortedProperDict[key]}{fleext[1]}"
        try:
            os.rename(epdict[maxMatchKey], correctFileName) # rename the matched file
        except OSError:
            correctedFilename = correctFileName.replace("?", "")
            os.rename(epdict[maxMatchKey], correctedFilename) # rename the matched file

        print(f"{epdict[maxMatchKey]} -> {pth}/{sortedProperDict[key]}{fleext[1]}") # print changes