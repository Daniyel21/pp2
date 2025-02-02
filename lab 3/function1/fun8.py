def has_33(nums):
    for i in range(len(nums) - 1): 
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i+2] == 7:
            return True  
    return False  
hit =[]
num =1
print("write your array (write 404 to stop): ")
while num!=404:
    num = int(input())
    if num ==404:
        break
    hit.append(num)
if has_33(hit) == True:
    print("Yes")
else:
    print("No")
