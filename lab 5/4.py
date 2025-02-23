import re 

data = "abbbbc acAc abb ab bNababa"

print('Task 4')
matches = re.findall(r"[A-Z][a-z]+", data)
print(matches)