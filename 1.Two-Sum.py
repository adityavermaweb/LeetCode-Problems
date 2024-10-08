# Give an array of integers 'nums' and an integer 'target', return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Ex:1 Input:nums = [2, 7, 11, 15], target = 9
#      Output:[0, 1]
#      Explanation: Because nums[0] + nums[1] == 9, we return[0, 1].

# Ex:2 Input:nums = [3, 2, 4], target = 6
#      Output: [1, 2]
# Ex:3 Input:nums = [3, 3] , target = 6
#      Output:[0, 1]    



# solution:-

nums = [2, 7, 11, 15]
target = 9
def twoSum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        if target - num in hash_map:
            return[hash_map[target-num],i]
        hash_map[num]=i
    return[]