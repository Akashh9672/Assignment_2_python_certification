Regex_Pattern = r'^[a-z]{1}[1-9]{1}[^a-z]{1}[^A-Z]{1}[A-Z]{1}'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())