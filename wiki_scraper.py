import requests
import logging
from bs4 import BeautifulSoup

logging.basicConfig(filename='wiki_logger', level=logging.DEBUG)




class WikiScraper:

    def __init__(self,link):
        self.link = link


    def _parse_website(self):
        try:
            response = requests.get(self.link)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                return soup
            else:
                logging.info("It has been some problem with request:  " + str(response.status_code))
        except Exception as error:
            logging.info("Exception has occured: " + error)
            
            
        

    def get_title(self):
        soup = self._parse_website()
        try:
            title = soup.title
            return title
        except Exception as error:
            logging.info("Exception has occured: " + str(error))

    def extract_correct_link(self):
        pass

    def find_link(self):
        pass

    def count_iteration(self):
        pass

    def __str__(self):
        return f"{self.link}"


if __name__ == "__main__":
    scraper = WikiScraper('https://en.wikipedia.org/wiki/Flight')
    title = scraper.get_title()
    print(title)
    print(scraper)