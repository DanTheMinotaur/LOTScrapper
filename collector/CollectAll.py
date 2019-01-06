from string import Template
import urllib.request
import datetime
import os


class CollectAll:

    games = [
        'euromillions',
        'lotto',
        'daily-million',
        'lotto54321',
    ]  # Types of games on site

    urls = dict()  # Holds the urls to the site once generated

    def generate_urls(self):
        self.urls = dict()  # reset urls if being regenerated
        print("Generating URLS")
        for game in self.games:
            self.urls[game] = Template('https://www.lottery.ie/dbg/results/view?game=$game&draws=0').substitute(dict(game=game))

    def get_games(self):
        return self.games

    def set_game(self, game):
        self.games.append(game)

    def download_pages(self):
        print("Downloading Web Pages")
        for page_name, page in self.urls.items():
            self.download_page(page_name, page)

    def download_page(self, page_name, page):
        request = urllib.request.Request(page, headers={'User-Agent': "Magic Browser"})
        response = urllib.request.urlopen(request)

        data = response.read().decode('utf-8')

        dir_name = 'download/' + datetime.date.today().strftime('%Y.%m.%d') + '/'

        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        self.file_writer(data, dir_name + page_name + '.html')

    def file_writer(self, data, file_name):
        file = open(file_name, 'w', encoding='utf-8')

        file.write(data)

        file.close()


