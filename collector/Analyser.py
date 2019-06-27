from collections import Counter
from collector.Database import Database


class Analyser():
    db = Database()

    def __get_results(self, db_table):
        return self.db.query_data(
            "SELECT game_type, game_date, number_1, number_2, number_3, number_4, number_5, number_6, bonus_number FROM " + db_table
        )

    def analyse_lotto(self):
        results = self.__get_results('lotto')
        dates = []
        numbers = []
        bonus_numbers = []
        for r in results:
            dates.append(r[1])
            numbers.append(r[2])
            numbers.append(r[3])
            numbers.append(r[4])
            numbers.append(r[5])
            numbers.append(r[6])
            numbers.append(r[7])
            bonus_numbers.append(r[8])
            #print(r)

        analysis = {
            'Main Numbers': Counter(numbers),
            'Bonus Numbers': Counter(bonus_numbers),
            'Start Date': min(dates),
            'End Date': max(dates)
        }

        return analysis

    def test(self):
        print(self.__get_results('lotto'))