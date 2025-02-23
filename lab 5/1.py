import re 

data = "abbbbc acc abb ab bababa"

matches = re.findall("a.*b", data)
print(matches)
