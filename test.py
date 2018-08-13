from collector.Database import Database
from collector.PageParser import Parser
from datetime import datetime

import os
"""
test_db = Database()

test_db.query_data("SELECT * FROM lotto;")
"""

test_par = Parser()

#test_db = Database()
#test_par.read_games('2018.08.06')
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
"""
test_par.add_lotto(False)
test_par.add_euromillions(False)
test_par.add_daily_millions(False)
test_par.add_lotto_54321(False)
"""

print([name for name in os.listdir('download/') if os.path.isdir(os.path.join('download/', name))])