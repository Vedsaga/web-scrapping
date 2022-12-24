import requests
from inflect import engine

from functions.useful_function import map_to_value, create_file, dump_json, load_json, substitute_word_from_list
from web_scrapping.pages.all_transistor_count_page import AllTransistorCountPage

page_content = requests.get('https://en.wikipedia.org/wiki/Transistor_count#Memory').content
page = AllTransistorCountPage(page_content=page_content)

tables = page.transistor_count_tables
extracted_data = {}
table_count = 0
for eachTable in tables:
    key_name = "table_{0}".format(engine().number_to_words(table_count))
    each_heading = substitute_word_from_list(list_to_check=eachTable.heading, match_word='Date', substitute_word='Year')
    all_rows = eachTable.rows
    mapped_values = map_to_value(keys=each_heading, values=all_rows)
    extracted_data[key_name] = mapped_values
    table_count += 1

file_path = create_file(dir_name='data', file_name='transistor_count', file_extension='.json')
dump_json(file_path=file_path, data=extracted_data)
loaded_data = load_json(file_path)


