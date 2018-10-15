nums = [3,2,4]
target = 6
for i,v in enumerate(nums):
            for x in range(i+1, len(nums)):
                if v + nums[x] == target:
                    print( [i, x])
