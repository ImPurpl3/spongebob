import os
import tkinter as tk
import json

from tkinter.filedialog import askdirectory
from tmdbv3api import TMDb, TV, Season

tokenfile = open('C:/Users/Lenovo/Desktop/Stuff/Coding/spongebob/token.json')
tokendata = json.load(tokenfile)

tmdb = TMDb()
tmdb.api_key = tokendata["TOKEN"]
tv = TV()
seas = Season()

tk.Tk().withdraw()
path = askdirectory()
pp1 = os.path.basename(path)
seasnum = pp1.replace("Season ", "")

ss = seas.details("387",seasnum)

properEPdict = {}
for l in ss.episodes:
    epname = l.name
    epnum = l.episode_number
    ssnum = l.season_number
    renamed = f"SpongeBob SquarePants - s{ssnum:02}e{epnum:02} - {epname}"
    properEPdict[f"{epname}"] = renamed

sortedProperDict = dict(sorted(properEPdict.items()))

epdict = {}
for filename in os.listdir(path):
    f = os.path.join(path, filename)
    fl = os.path.splitext(filename)
    ff = fl[0]
    if os.path.isfile(f):
        epname = ff[35:]
        epfile = f"{path}/{filename}"
        epdict[f"{epname}"] = epfile

for key in sortedProperDict.keys():
    if key in epdict.keys():
        pth, filenm = os.path.split(epdict[key])
        fleext = os.path.splitext(epdict[key])
        os.rename(epdict[key], f"{pth}/{sortedProperDict[key]}{fleext[1]}")
        print(f"{epdict[key]} -> {pth}/{sortedProperDict[key]}{fleext[1]}")