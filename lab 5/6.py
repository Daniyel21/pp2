import re 

data = "abbbbc acc abb ab bababa"

print("Task 6")
matches=re.sub("[., ]",':',data)
print(matches)
