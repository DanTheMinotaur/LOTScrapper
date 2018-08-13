from bs4 import BeautifulSoup
from datetime import datetime, date
from collector.Database import Database
import datetime

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

    def get_current_db_entries(self, db_table, date=True):
        if date:
            return self.db.query_data("SELECT game_type, DATE(game_date) FROM " + db_table)
        else:
            return self.db.query_data("SELECT game_type, game_date FROM " + db_table)

    def add_lotto_54321(self, single_game=True):
        data_to_insert = []
        current_results = self.get_current_db_entries('lotto_54321')
        for game_counter, game in enumerate(self.game_results['lotto54321']):
            for i, result in enumerate(game['results']):
                game_data = []
                if i == 0:
                    game_data.append("Lotto 54321")
                if i == 1:
                    game_data.append("Lotto 54321 Plus 1")
                if i == 2:
                    game_data.append("Lotto 54321 Plus 2")

                game_data.append(game['date'])

                if tuple(game_data) not in current_results:
                    game_data = game_data + result
                    data_to_insert.append(tuple(game_data))

            if single_game is True:
                break

        if len(data_to_insert) > 0:
            print("Inserting " + str(len(data_to_insert)) + " Lotto54321 Results to DB")
            self.db.alter_data(
                "INSERT INTO lottery.lotto_54321 (game_type, game_date, number_1, number_2, number_3, number_4, number_5, number_6, bonus_number) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", data_to_insert
            )
        else:
            print("No New Results to insert")


    def add_daily_millions(self, single_game=True):
        data_to_insert = []
        current_results = self.get_current_db_entries('daily_millions', False)
        print(current_results)
        for game_counter, game in enumerate(self.game_results['daily-million']):
            for i, result in enumerate(game['results']):
                game_data = []
                if i == 0:
                    game_data.append("Daily Million")
                if i == 1:
                    game_data.append("Daily Million Plus")

                game_data.append(game['date'])

                if tuple(game_data) not in current_results:
                    game_data = game_data + result
                    data_to_insert.append(tuple(game_data))

            if single_game is True:
                break

        if len(data_to_insert) > 0:
            print("Inserting " + str(len(data_to_insert)) + " Daily Millions Results to DB")
            self.db.alter_data(
                "INSERT INTO lottery.daily_millions(game_type, game_date, number_1, number_2, number_3, number_4, number_5, number_6, bonus_number)"
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", data_to_insert
            )
        else:
            print("No New Results to insert")


    def add_euromillions(self, single_game=True):
        eur_mil = []
        eur_mil_plus = []
        current_results = self.get_current_db_entries('euro_millions')
        for game_counter, game in enumerate(self.game_results['euromillions']):
            for i, result in enumerate(game['results']):
                game_data = []
                if i == 0:
                    game_data.append("Euromillions")
                    game_data.append(game['date'])

                    if tuple(game_data) not in current_results:
                        game_data = game_data + result
                        eur_mil.append(tuple(game_data))
                if i == 1:
                    game_data.append("Euromillions Plus")
                    game_data.append(game['date'])

                    if tuple(game_data) not in current_results:
                        game_data = game_data + result
                        eur_mil_plus.append(tuple(game_data))

            if single_game is True:
                break

        if len(eur_mil) > 0:
            print("Inserting " + str(len(eur_mil)) + " Euromillions Results to DB")
            self.db.alter_data(
                "INSERT INTO lottery.euro_millions(game_type, game_date, number_1, number_2, number_3, number_4, number_5, "
                "lucky_star_1, lucky_star_2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", eur_mil
            )
        else:
            print("No New Results to insert")

        if len(eur_mil_plus) > 0:
            print("Inserting " + str(len(eur_mil_plus)) + " Euromillions Plus Results to DB")
            self.db.alter_data(
                "INSERT INTO lottery.euro_millions(game_type, game_date, number_1, number_2, number_3, number_4, number_5) "
                " VALUES (%s, %s, %s, %s, %s, %s, %s);", eur_mil_plus
            )
        else:
            print("No New Results to insert")

    def add_lotto(self, single_game=True):
        data_to_insert = []
        current_results = self.get_current_db_entries('lotto')
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

                if tuple(game_data) not in current_results:
                    game_data = game_data + result
                    data_to_insert.append(tuple(game_data))

            if single_game is True:
                break

        if len(data_to_insert) > 0:
            print("Inserting " + str(len(data_to_insert)) + " Lotto Results to DB")
            self.db.alter_data(
                "INSERT INTO lottery.lotto(game_type, game_date, number_1, number_2, number_3, number_4, number_5, number_6, bonus_number)"
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", data_to_insert
            )
        else:
            print("No New Results to insert")


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
                game_date = datetime.datetime.strptime(game_date[4:], '%d %B %Y, %H:%M%p')
            else:
                game_date = datetime.datetime.strptime(game_date[4:], '%d %B %Y').date()

            #print(game_date)

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
