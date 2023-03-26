from difflib import SequenceMatcher

str1 = "MermaidMan and Barnacleboy"
str2 = "Home Sweet Pineapple"

matchtest = SequenceMatcher(None, str1, str2).ratio()

print(matchtest)