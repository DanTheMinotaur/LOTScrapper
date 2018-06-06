from bs4 import BeautifulSoup
from mysql.connector import errorcode
import mysql.connector
from datetime import datetime


class Interpreter:

    results_data = dict()

    def read_pages(self, pages):
        for game, page in pages.items():
            self.read_page(page, game)

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

    def print_results(self):
        print(self.results_data)

    def extract_full_info(self):
        db = Database()
        for game_name, values in self.results_data.items():
            data = []
            print(game_name)
            data.append(game_name)
            for obj in values:
                print(obj['date'][4:])
                date_obj = datetime.strptime(obj['date'][4:], '%d %B %Y')
                print(date_obj.date())
                data.append(str(date_obj.date()))

                for game_result, numbers in obj['game_results'].items():
                    print(game_result + ' - - ' + str(numbers))
                    data.append(game_result)
                    data = data + numbers
                    #break
                print(data)
                #db.insert_result(data)
                break

            break





class Database:

    __db_conn = mysql.connector

    def __init__(self):
        try:
            self.__db_conn = mysql.connector.connect(
                user='LOTScrapper',
                password='LOTScrapper',
                host='localhost',
                database='lottery'
            )
            print('Database Connection Established')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def test(self):

        cursor = self.__db_conn.cursor()

        query = "SELECT * FROM results"

        cursor.execute(query)

        for each in cursor:
            print(each)

        print(cursor)


    def insert_result(self, result):
        print(result)
        query = "INSERT INTO results(competition, game_date, game, number_1, number_2, number_3, number_4, number_5, number_6, bonus_number) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        cursor = self.__db_conn.cursor()

        cursor.execute(query, result)

        self.__db_conn.commit()