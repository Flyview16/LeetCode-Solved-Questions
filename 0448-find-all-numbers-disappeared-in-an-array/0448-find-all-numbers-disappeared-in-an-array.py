class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        disappeared = []
        for i in range (1, n +1):
            if i not in nums:
                disappeared.append(i)  

        return disappeared