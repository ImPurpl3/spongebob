import os
import tkinter as tk
import json

from tkinter.filedialog import askdirectory
from tmdbv3api import TMDb, TV, Season

tokenfile = open('C:/Users/Lenovo/Desktop/Stuff/Coding/renamemathc/token.json')
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

print("Proper Naming:")
for l in ss.episodes:
    epname = l.name
    epnum = l.episode_number
    ssnum = l.season_number
    print(f"SpongeBob SquarePants - s{ssnum:02}e{epnum:02} - {epname}")


for filename in os.listdir(path):
    f = os.path.join(path, filename)
    fl = os.path.splitext(filename)
    ff = fl[0]
    if os.path.isfile(f):
        epname = ff[35:]
