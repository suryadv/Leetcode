def search(nums,target):
    if target not in nums:
        return -1
    l = 0
    r = len(nums)-1
    while l<=r:
        mid = (l+r)//2
        if nums[mid]<target:
            l = mid+1
        elif nums[mid]>target:
            r = mid-1
        else:
            return mid


nums = [10,20,30,40]
target = 40
k = search(nums,target)
print(k)
