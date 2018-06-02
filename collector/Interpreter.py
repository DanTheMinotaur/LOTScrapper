from bs4 import BeautifulSoup

class Interpreter:

    test = 'download/2018.06.01/lotto.html'

    results_data = dict()

    def read_page(self, page, game_name):
        html = BeautifulSoup(open(page).read(), 'html.parser')

        self.results_data[game_name] = []

        results_sections = html.find_all('section', class_="matching-draw")

        for section in results_sections:  #Splits sections
            data = dict()
            data['date'] = section.find('h4').get_text()

            winning_results = section.find_all('div', class_="winning-results")

            game_count = 1
            game_data = dict()

            for results in winning_results:
                inputs = results.find_all('input')

                game_results = []

                for number in inputs:
                    game_results.append(number.get('value'))

                game_data['game' + str(game_count)] = game_results

                game_count += 1

            data['game_results'] = game_data

            self.results_data[game_name].append(data)

        print(self.results_data)


