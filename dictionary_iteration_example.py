#!/usr/bin/python3

guts = {
    "Name":"Guts",
    "Personality":"gruff",
    "Weapon":"Dragon Slayer",
    "Armor":"Berserker Armor"
}

# Add loop to print each dictionary key and key value as shown in the Python Scripting Topic

for key in guts.keys():
    print(key + ": " + guts[key])
