from collector.CollectAll import CollectAll
from collector.Interpreter import Interpreter, Database


collect = CollectAll()
#collect.generate_urls()
#collect.download_page('https://www.lottery.ie/dbg/results/view?game=lotto&draws=0', 'test')

#collect.download_pages()

#collect.file_writer('Hello', 'hello.html')

inter = Interpreter()
#inter.read_page('download/2018.06.01/lotto.html', 'lotto')

games = {
    'euromillions': 'download/2018.06.01/euromillions.html',
    'lotto': 'download/2018.06.01/lotto.html',
    'daily-million': 'download/2018.06.01/daily-million.html',
    'lotto54321': 'download/2018.06.01/lotto54321.html',
}

inter.read_pages(games)


inter.print_results()

inter.extract_full_info()

#db = Database()

#db.insert_result(['euromillions', '2018-06-01', '17', '18', '24', '29', '40', '4', '5'])