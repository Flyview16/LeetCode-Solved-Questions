class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum_num = 0
        while n > 0:
            num = n % 10
            product *= num
            sum_num += num
            n//=10
        return product - sum_num

    
