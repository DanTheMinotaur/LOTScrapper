from bs4 import BeautifulSoup

class Interpreter:

    test = 'download/2018.06.01/lotto.html'

    def read_page(self, page):
        html = BeautifulSoup(open(page).read(), 'html.parser')

        results_sections = html.find_all('section', class_="matching-draw")

        for result in results_sections:
            print(result.prettify())


