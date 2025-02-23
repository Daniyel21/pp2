import re 

data = "abbb_bc acc abb ab bababa"

matches=re.sub(r"_",'',data)
print(matches)