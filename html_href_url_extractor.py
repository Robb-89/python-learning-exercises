#!/usr/bin/python3

hrefLine = '<a href="https://www.offensive-security.com/offsec/game-hacking-intro/">Introduction to Game Hacking</a>'

start = "http"
end = ">"

url = hrefLine[hrefLine.index(start):hrefLine.index(end)]
print(url)




