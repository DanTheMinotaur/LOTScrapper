from collector.Database import Database
from collector.PageParser import Parser
from datetime import datetime
"""
test_db = Database()

test_db.query_data("SELECT * FROM lotto;")
"""

test_par = Parser()

#test_db = Database()
test_par.read_games('2018.08.06')
#test_par.test('daily_millions')
#test_par.add_lotto_54321()

#print(test_db.query_data("SELECT game_type, DATE(game_date) FROM daily_millions;"))

#test_par.read_page('download/2018.08.06/lotto.html')
#test_par.read_page('download/2018.08.06/daily-million.html')
#test_par.read_page('download/2018.08.06/euromillions.html')
#print(test_par.read_page('download/2018.08.06/lotto54321.html'))

#print(test_par.game_results)

#print(test_par.read_page('download/2018.08.06/daily-million.html'))

#print(test_par.game_results)
#test_par.read_games('2018.08.06')
test_par.add_lotto(False)
test_par.add_euromillions(False)
test_par.add_daily_millions(False)
test_par.add_lotto_54321(False)

#var = [{'date': datetime.date(2018, 8, 4), 'results': [[3, 4, 5, 19, 26, 43, 24], [4, 17, 24, 35, 36, 40, 13], [4, 9, 25, 32, 35, 43, 19]]}, {'date': datetime.date(2018, 8, 1), 'results': [[3, 27, 38, 40, 43, 46, 12],[4, 5, 29, 34, 39, 46, 28], [6, 20, 24, 29, 31, 44, 28]]}, {'date': datetime.date(2018, 7, 28), 'results': [[7, 23, 27, 28, 37, 44, 5], [4, 9, 11, 18, 25, 42, 29], [1, 4, 23, 28, 40, 43, 12]]}, {'date': datetime.date(2018, 7, 25), 'results': [[3, 16, 21, 29, 36, 47, 35], [5, 8, 17, 29, 31, 41, 44], [3, 5, 22, 25, 27, 41, 26]]}, {'date': datetime.date(2018, 7, 21), 'results': [[2, 6, 11, 13, 20, 30, 38], [7, 20, 27, 29, 43, 44, 16], [2, 5, 11, 12, 38, 44, 39]]}, {'date': datetime.date(2018, 7, 18), 'results': [[2, 8, 25, 33, 39, 42, 43], [6, 15, 21, 22, 34, 47, 1], [8, 12, 22, 23, 24, 26, 27]]}, {'date': datetime.date(2018, 7, 14), 'results': [[5, 16, 37, 43, 44, 46, 7], [11, 13, 21, 24, 35, 41, 31], [4, 12, 15, 27, 31, 46, 26]]}, {'date': datetime.date(2018, 7, 11), 'results': [[2, 14, 21, 39, 42, 45, 28], [19, 26, 31, 36, 38, 40, 24],[7, 9, 13, 25, 41, 43, 38]]}, {'date': datetime.date(2018, 7, 7), 'results': [[3, 11, 24, 26, 29, 47, 13], [15, 19, 21, 23, 24, 32, 26], [6, 10, 27, 28, 37, 47, 25]]}, {'date': datetime.date(2018, 7, 4), 'results': [[6, 25, 29, 33, 42, 46, 5], [18, 22, 35, 38, 41, 45, 23], [6, 7, 23, 32, 36, 40, 2]]}, {'date': datetime.date(2018, 6, 30), 'results': [[19, 22, 24, 30, 38, 45, 46], [4, 11, 17, 18, 22, 37, 5], [6, 13, 21, 25, 29, 47, 34]]}, {'date': datetime.date(2018, 6, 27), 'results': [[9, 18, 20, 27, 38, 39, 29], [11, 18, 25, 26, 39, 46, 6], [15, 27, 30, 31, 36, 39, 42]]}, {'date': datetime.date(2018, 6, 23), 'results': [[4, 6,12, 20, 40, 43, 21], [10, 22, 23, 34, 46, 47, 21], [2, 4, 12, 15, 32, 37, 43]]}, {'date': datetime.date(2018, 6, 20), 'results': [[11, 26, 32, 36, 42, 47, 34], [3, 23, 25, 28, 36, 40, 18], [14, 22, 25, 30, 33, 43, 17]]}, {'date': datetime.date(2018, 6, 16), 'results': [[6, 26, 27, 32, 45, 47, 9], [3, 5, 6, 35, 43, 47, 16], [1, 8, 9, 21, 44, 47, 36]]}, {'date': datetime.date(2018, 6, 13), 'results': [[5, 21, 25, 29, 41, 43, 31], [17, 20, 31, 34, 38, 43, 35], [1, 4, 11, 23, 46, 47, 40]]}, {'date': datetime.date(2018, 6, 9), 'results': [[11, 12, 19, 27, 30, 38, 16], [13, 18, 20, 24, 25, 47, 34], [8, 14, 16, 26, 27, 41, 36]]}, {'date': datetime.date(2018, 6, 6), 'results': [[1, 10, 22, 28, 44, 47, 14], [3, 11, 25, 29, 33, 41, 14], [18, 26, 27, 28, 39, 40, 22]]}, {'date': datetime.date(2018, 6, 2), 'results': [[1, 7, 10, 17, 35, 37, 43], [20, 23, 24, 36, 38, 47, 32], [1, 16, 24, 36, 39, 42, 33]]}, {'date': datetime.date(2018, 5, 30), 'results': [[11, 13, 14, 16, 31, 38, 5], [2, 5, 12, 14, 18, 19, 8], [4, 10, 18, 23, 25, 43, 27]]}, {'date': datetime.date(2018, 5, 26), 'results': [[6, 15, 22, 30, 39, 45, 16], [7, 17, 23, 32, 33, 38, 11], [1, 3, 6, 8, 29, 47, 11]]}, {'date': datetime.date(2018, 5, 23), 'results': [[5, 22, 29, 38, 40, 44, 20], [9, 20, 21, 24, 33, 35, 37], [12, 13, 30, 43, 45, 46, 14]]}, {'date': datetime.date(2018, 5, 19), 'results': [[3, 11, 14, 23, 36, 45, 26], [11, 13, 15, 20, 30, 31, 8], [15, 24, 30, 31, 34, 44, 39]]}, {'date': datetime.date(2018,5, 16), 'results': [[5, 10, 14, 22, 25, 31, 15], [13, 19, 30, 37, 43, 47, 17], [1, 6, 10, 23, 24, 33, 2]]}, {'date': datetime.date(2018, 5, 12), 'results': [[5, 6, 14, 19, 22, 30, 24], [8, 19, 21, 25, 26, 40, 32], [5, 9, 15, 23, 31, 42, 37]]}, {'date': datetime.date(2018, 5, 9), 'results': [[1, 12, 23, 32, 36, 40, 2], [13, 16, 28, 31, 38, 42, 30], [1, 11, 12, 13, 17, 41, 31]]}]