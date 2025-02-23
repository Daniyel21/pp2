import re 

data = "abbbbc acc abb ab bababa"

matches = re.findall("a.*bb+|abbb+", data)
print(matches)
