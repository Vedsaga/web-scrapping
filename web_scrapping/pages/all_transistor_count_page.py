from bs4 import BeautifulSoup

from web_scrapping.locators.body_content import BodyContentLocators
from web_scrapping.parsers.transistor_count_table_parser import TransistorCountTableParser


class AllTransistorCountPage:
    # initialization init with BeautifulSoup
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, "html.parser")

    # a property that find all the transistor count table
    @property
    def transistor_count_tables(self):
        tables = self.soup.select(
            BodyContentLocators.TRANSISTOR_COUNT_TABLE_LOCATOR, limit=3,)
        parsed_object: list[TransistorCountTableParser] = []
        for each in tables:
            parsed_object.append(TransistorCountTableParser(each))
        return parsed_object
