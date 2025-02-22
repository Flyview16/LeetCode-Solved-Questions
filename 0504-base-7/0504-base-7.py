class Solution:
    def convertToBase7(self, num: int) -> str:
        output = []
        is_negative = num < 0
        num = abs(num)   # work with absolut value of num

        if num == 0:
            return "0"

        while num > 0:
            output.append(str(num % 7))
            num //= 7
        
        if is_negative:
            output.append("-")
        output.reverse()
        return "".join(output)
            