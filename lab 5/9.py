import re 

data = "abbbAbcFaKccLabbOabPbababa"

print(re.sub(r'(?<!^)([A-Z])', r' \1', data))