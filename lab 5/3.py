import re 

data = "abbbA_Zb a_cc abb a_b bababa"

matches = re.findall("[a-z]_+[a-z]+", data)
print(matches)