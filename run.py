from collector.CollectAll import CollectAll
from collector.Interpreter import Interpreter, Database


collect = CollectAll()
collect.generate_urls()

collect.download_pages()

