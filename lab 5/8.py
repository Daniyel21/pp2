import re 

data = "abbbAbc acc abKKb ab bababa"

print(re.findall(r"[A-Z][^A-Z]*", data))
