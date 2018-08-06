from bs4 import BeautifulSoup


class Parser:

    def __init__(self):
        self.games = [
            'daily-million',
            'euromillions',
            'lotto',
            'lotto54321'
        ]
        self.game_results = dict()

    """
        Method generaets all data by date and sets game_results with each results.
    """
    def read_games(self, date):
        for game in self.games:
            self.game_results[game] = self.read_page('download/' + date + '/' + game + '.html')

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

            data['date'] = section.find('h4').get_text()

            winning_results = section.find_all('div', class_="winning-results")

            winning_numbers = []

            for results in winning_results:
                inputs = results.find_all('input')

                game_results = []

                for number in inputs:
                    game_results.append(number.get('value'))

                winning_numbers.append(game_results)

            data['results'] = winning_numbers

            games.append(data)

        return games
