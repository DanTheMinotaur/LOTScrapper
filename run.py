from collector.CollectAll import CollectAll
from collector.Interpreter import Interpreter


#collect = CollectAll()

#collect.generate_urls()
#collect.download_page('https://www.lottery.ie/dbg/results/view?game=lotto&draws=0', 'test')

#collect.download_pages()

#collect.file_writer('Hello', 'hello.html')

inter = Interpreter()
inter.read_page('download/2018.06.01/lotto.html')