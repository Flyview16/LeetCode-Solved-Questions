class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        count = {}

        # Count occurence of each number
        for num in nums:
            if num in count:
                count[num] +=1
            else:
                count[num] = 1
        
        # Find numbers that appear twice and xor them
        xor_result = 0
        for num, times in count.items():
            if times == 2:
                xor_result ^= num
        
        return xor_result