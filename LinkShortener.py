import pyshorteners

link = input('Enter Long URl : ')
shortener = pyshorteners.Shortener()
shortLink = shortener.tinyurl.short(link)

print(shortLink)