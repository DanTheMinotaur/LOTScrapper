from bs4 import BeautifulSoup


class Parser:

    @staticmethod
    def read_page(page):
        html = BeautifulSoup(open(page).read(), 'html.parser')

        results_sections = html.find_all('section', class_="matching-draw")

        games = []

        for section in results_sections:  #Splits sections

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
