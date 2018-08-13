from collector.CollectAll import CollectAll
from collector.PageParser import Parser
from collector.__Interpreter import Interpreter, Database
from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose
import os

class CLIController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'App that downloads and analyses Lottery Results'
        arguments = [
            (
                ['-a', '--all'],
                dict(action='store', help='This option will add all possible options')
            ),
        ]

    def default(self):
        self.app.log.info('Use the option -h or --help to see commands')

    @expose(help="this command downloads the latest results from the website", aliases=['downloadpages'])
    def download_latest_results(self):
        self.app.log.info('Downloading Latest Results')
        web_collector = CollectAll()
        web_collector.generate_urls()
        web_collector.download_pages()

    @expose(help="This will parse the latest results, then insert it into the database", aliases=['parsepages'])
    def parseresults(self):
        download_dir = 'download/'
        folders = [name for name in os.listdir(download_dir) if os.path.isdir(os.path.join(download_dir, name))]
        parser = Parser()
        if self.app.pargs.all:
            print("Parsing all previous records")
            for f in folders:
                print("Parsing " + f)
                parser.read_games(f)
                parser.add_lotto(False)
                parser.add_euromillions(False)
                parser.add_lotto_54321(False)
                parser.add_daily_millions(False)
        else:
            latest = max(folders)
            self.app.log.info('Parsing latest results')
            parser.read_games(latest)
            self.app.log.info('Results Parsed')
            self.app.log.info('Inserting Results for Lotto')
            parser.add_lotto(False)
            self.app.log.info('Inserting Results for EuroMillions')
            parser.add_euromillions(False)
            self.app.log.info('Inserting Results for Lotto54321')
            parser.add_lotto_54321(False)
            self.app.log.info('Inserting Results for Daily Millions')
            parser.add_daily_millions(False)



class LOTScrapper(CementApp):
    class Meta:
        label = 'LOTScrapper'
        base_controller = 'base'
        handlers = [CLIController]

with LOTScrapper() as app:
    app.run()

#collect = CollectAll()
#collect.generate_urls()

#collect.download_pages()

