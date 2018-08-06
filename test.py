from collector.Database import Database
from collector.PageParser import Parser

"""
test_db = Database()

test_db.query_data("SELECT * FROM lotto;")
"""

test_par = Parser()

#test_par.read_page('download/2018.08.06/lotto.html')
#test_par.read_page('download/2018.08.06/daily-million.html')
#test_par.read_page('download/2018.08.06/euromillions.html')
#print(test_par.read_page('download/2018.08.06/lotto54321.html'))

test_par.read_games('2018.08.06')

