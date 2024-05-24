class Solution:
    def convertToBase7(self, num: int) -> str:
        output = []
        is_negative = num < 0
        num = abs(num)
        while num > 0:
            output.append(str(num % 7))
            num //= 7
        
        if is_negative:
            output.append("-")
        output.reverse()
        return "".join(output)
            