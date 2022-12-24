
'''
old_list = ['MP944 (20-bit, 6-chip, 28 chips total)', '74,442 (5,360 excl. ROM & RAM)[14][15]', '1970[12][a]']
new_list = ['MP944', '74,442', '1970']
'''

import re


old_list = ['MP944 (20-bit, 6-chip, 28 chips total)', '74,442 (5,360 excl. ROM & RAM)[14][15]', '1970[12][a]']
# regex to match the new format
regex = re.compile(r'^[a-zA-Z0-9,]+')

for old in old_list:
    new = regex.findall(old)
    print(new)

