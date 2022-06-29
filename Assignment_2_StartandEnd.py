Regex_Pattern = r"^[0-9]{1}[a-zA-Z0-9]{4}\.{1}$"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())