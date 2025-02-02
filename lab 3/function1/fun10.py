def cleaning(arr):
    list2 = []  
    for i in arr:
        if i not in list2:  
            list2.append(i)
    return list2  

print("Write your array (type 'stop' to end input): ")
list1 = []

while True:
    user_input = input()
    if user_input.lower() == "stop": 
        break
    try:
        num = int(user_input)
        list1.append(num)
    except ValueError:
        print("Invalid input, please enter a number or 'stop'.")

list2 = cleaning(list1)
print("List with unique elements:", list2)
