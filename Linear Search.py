def search(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return (i)
    if target not in nums:
        return -1



nums = [10,20,30,40]
target = 3
k = search(nums,target)
print(k)


