import re 

data = "abbbbc acc abb ab bababa"

print('Task 5')
matches = re.findall(r"a+.b", data)
print(matches)
