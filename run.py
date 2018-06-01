from collector.CollectAll import CollectAll

collect = CollectAll()

collect.generate_urls()
#collect.download_page('https://www.lottery.ie/dbg/results/view?game=lotto&draws=0', 'test')

collect.download_pages()

#collect.file_writer('Hello', 'hello.html')
