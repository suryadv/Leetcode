nums = [3,2,3]
target = 6
if len(nums) <= 1:
    print(False)
buff_dict = {}
for i in range(len(nums)):
    if nums[i] in buff_dict:
        print([buff_dict[nums[i]], i])
    else:
        buff_dict[target - nums[i]] = i
