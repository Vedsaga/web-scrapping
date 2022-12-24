# import beautifulSoup from 'bs4'
import re

from web_scrapping.locators.transistor_count_table_locators import TransistorCountTableLocators


class TransistorCountTableParser:
    """
    A class to parse the transistor count table.
    """

    def __init__(self, soup):
        self.parent = soup

    # Function to parse the table header
    @property
    def heading(self):
        locator = TransistorCountTableLocators.GPU_TABLE_HEADING
        headings = [each_heading.get_text().strip() for each_heading in self.parent.select(locator, limit=3)]
        return headings

    # Function to parse the table rows
    @property
    def rows(self):
        locator = TransistorCountTableLocators.EACH_ROW
        all_rows = self.parent.select(locator)
        new_list = []
        # regex to match the new format
        regex = re.compile(r'^[-,µ ?+a-zA-Z0-9]+')
        for each_row in all_rows:
            for each in each_row.select(TransistorCountTableLocators.EACH_CELL_DETAIL, limit=3):
                without_regex = each.get_text().strip()
                post_regex = regex.findall(without_regex)
                if len(post_regex) != 0:
                    new_list.append(post_regex[0])
                else:
                    new_list.append("?")
        return new_list
