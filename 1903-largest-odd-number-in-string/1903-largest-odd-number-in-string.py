class Solution:
    def largestOddNumber(self, num: str) -> str:
        max_odd = ""
        for i in range(len(num)):
            for j in range(i, len(num)):
                substring = num[i:j + 1]
                if int(substring) % 2 == 1 and (max_odd == "" or int(substring) > int(max_odd)):
                    max_odd = substring
        return max_odd