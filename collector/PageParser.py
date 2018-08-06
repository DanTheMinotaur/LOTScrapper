from bs4 import BeautifulSoup
from datetime import datetime, date
from collector.Database import Database

class Parser:

    def __init__(self):
        self.games = [
            'daily-million',
            'euromillions',
            'lotto',
            'lotto54321'
        ]
        self.game_results = dict()
        self.db = Database()

    def add_lotto(self):
        data_to_insert = []
        for game in self.game_results['lotto']:
            for i, result in enumerate(game['results']):
                game_data = []
                if i == 0:
                    game_type = "Lotto"
                if i == 1:
                    game_type = "Lotto Plus 1"
                if i == 2:
                    game_type = "Lotto Plus 2"
                game_data.append(game_type)
                game_data.append(game['date'])
                game_data = game_data + result

                data_to_insert.append(tuple(game_data))

        print("Inserting Lotto Results to DB")
        self.db.alter_data(
            "INSERT INTO lottery.lotto(game_type, game_date, number_1, number_2, number_3, number_4, number_5, number_6, bonus_number)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", data_to_insert
        )


    """
        Method generates all data by date and sets game_results with each results.
    """
    def read_games(self, game_date):
        for game in self.games:
            self.game_results[game] = self.read_page('download/' + game_date + '/' + game + '.html')

    """
        Method reads a single page and converts the results into dictionary.
    """
    @staticmethod
    def read_page(page):
        html = BeautifulSoup(open(page).read(), 'html.parser')

        results_sections = html.find_all('section', class_="matching-draw")

        games = []

        for section in results_sections:

            data = dict()

            game_date = section.find('h4').get_text()

            if len(game_date) > 18:
                game_date = datetime.strptime(game_date[4:], '%d %B %Y, %H:%M%p')
            else:
                game_date = datetime.strptime(game_date[4:], '%d %B %Y').date()

            data['date'] = game_date

            winning_results = section.find_all('div', class_="winning-results")

            winning_numbers = []

            for results in winning_results:
                inputs = results.find_all('input')

                game_results = []

                for number in inputs:
                    game_results.append(int(number.get('value')))

                winning_numbers.append(game_results)

            data['results'] = winning_numbers

            games.append(data)

        return games
