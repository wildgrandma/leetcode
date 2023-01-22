# i/p: [2,7,11,15] and target=9
# return list elements that on summation equate to the target 
# op: [2,7]
nums = [2,7,11,15]
target = 9

def twosum(self,nums:list[int],target:int)->list[int]:
    # brute force
    l = {}
    n = len(nums)
    for num in enumerate(nums):
        