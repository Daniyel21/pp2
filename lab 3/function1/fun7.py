def has_33(nums):
    print("write your array (write 0 to stop): ")
    for i in range(len(nums) - 1): 
        if nums[i] == 3 and nums[i + 1] == 3:
            return True  
    return False  
hit =[]
num =1
while num!=0:
    num = int(input())
    if num ==0:
        break
    hit.append(num)
if has_33(hit) == True:
    print("Yes")
else:
    print("No")

