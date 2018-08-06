from collector.Database import Database
from collector.PageParser import Parser

"""
test_db = Database()

test_db.query_data("SELECT * FROM lotto;")
"""

test_par = Parser

#test_par.read_page('download/2018.06.02/lotto.html')
#test_par.read_page('download/2018.06.02/daily-million.html')
#test_par.read_page('download/2018.06.02/euromillions.html')
print(test_par.read_page('download/2018.06.02/lotto54321.html'))