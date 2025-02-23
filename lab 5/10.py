import re 

data = "abbbGbc acc aDbb ab bababa"

matches=re.sub(r"[A-Z]",'_',data)
print(matches)