from collections import Counter


def solve(nums):
   count = Counter(nums)
   ans = 0
   for index,value in enumerate(nums):
      if count[value]==1:
         ans+=value
   return ans

nums = [5,2,1,5,3,1,3,8]
print(solve(nums))