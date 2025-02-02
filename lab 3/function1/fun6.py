def rev():
    print("input your strings (write 0 to end): ")
    list1 = []

    stri = str(input())
    list1 = stri.split()
    list1.reverse()
    print(list1)

rev()