from urllib.request import urlopen
from string import Template

# Lottery link details

games = [
    'euromillions',
    'lotto',
]



urls = []

#urls.append(Template('https://www.lottery.ie/dbg/results/view?game=$game&draws=$max_results').substitute(games[0]))

for game in games:
    print(game)
    urls.append(Template('https://www.lottery.ie/dbg/results/view?game=$game&draws=0').substitute(dict(game=game)))

print(urls)

#link = Template('https://www.lottery.ie/dbg/results/view?game=$game&draws=$max_results').substitute()

#print(link)

#html = urlopen("http://www.stackoverflow.com/").read().decode('utf-8')
#print(html)
