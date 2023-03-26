# spongebob
Spongebob Episode Renamer for Plex to ingest

# What it does
* Uses Spongebob Episode file
* Matches file name to The Movie Database's Episode Names
* Renames the file appropiately to Plex's Standards

# Requirements
* TMDb API Key - https://www.themoviedb.org/signup
* More than 4 Functioning Brain Cells
* tmdb3api python lib - https://github.com/AnthonyBloomer/tmdbv3api
* Path to SpongeBob Seasons and Episode File Names must be formated like this (Season Number where there is X, and Episode Name where there is Z)
```
C:/Path/To/TV Shows/SpongeBob SquarePants/Season X/SpongeBob SquarePants - Season X - Z
```

# Things to Note
* This is made so that Plex can look at my SpongeBob Seasons and ingest them properly
* I made this in 1 hour, so if the code is bad and hard to read, thats probably why
* I installed 7 programs before just making my own script because they all sucked (pay wall, couldn't match just from episode name)
* You will have to add your TMDb API Key to the token.json file for stuff to work

# Example Use
If the file name of my SpongeBob Squarepants Season 2 Episode Name "Squidville" is "SpongeBob SquarePants - Season 2 - Squidville.avi",
It will rename the file to "SpongeBob SquarePants - s02e17 - Squidville.avi" so that Plex can read it :)
