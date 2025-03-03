nums=[1,2,3,4,5]
target=6
l=[]
for i in nums:
    if i+(i+1) == target:
        l.extend([nums.index(i),nums.index(i+1)])
    elif i+(i+2) == target:
        l.extend([nums.index(i),nums.index(i+2)])
print(l)
    

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l=[]
        for i in nums:
            if i+(i+1) == target:
                l.extend([nums.index(i),nums.index(i+1)])
            elif i+(i+2) == target:
                l.extend([nums.index(i),nums.index(i+2)])
        print(l)
Solution.twoSum(self=Solution, nums=[1,2,3,4,5,6], target=4)

 