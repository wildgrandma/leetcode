# i/p: [2,7,11,15] and target=9
# return list elements that on summation equate to the target 
# op: [2,7]
nums = [2,7,11,15]
target = 9

class Sol:
    def twosum(nums: list[int],target: int) -> list[int]:
        seen = {}
        for i, value in enumerate(nums): #1
           remaining = target - nums[i] #2
           
           if remaining in seen: #3
               return [i, seen[remaining]]  #4
           else:
               seen[value] = i  #5

    def brute(nums:list[int],target:int) -> list[int]:
        