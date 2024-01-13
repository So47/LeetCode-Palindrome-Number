class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        reversed_x = x_str[::-1]
        return x_str == reversed_x
        
