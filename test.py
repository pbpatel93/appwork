import urllib.request
content = urllib.request.urlopen('https://en.wikipedia.org/wiki/Comet')

read_content = content.read()