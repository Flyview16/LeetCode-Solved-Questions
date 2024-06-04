class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
       n = len(s)
       answer = [0] * n

       # Find the indices of the character c
       indices = [i for i, char in enumerate(s) if char == c]
       
       # Compute the smallest distance btn index in string s and all indices of character c in string s
       for i in range(n):
            min_distance = float('inf')
            for index in indices:
                min_distance = min(min_distance, abs(i - index))
            answer[i] = min_distance
       return answer
    