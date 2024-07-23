import math

class Solution:
    def gcdOfStrings(self, str1, str2):
        # Helper function to check if s can be constructed by repeating t
        def canConstruct(s, t):
            return t * (len(s) // len(t)) == s
        
        # Find the greatest common divisor of the lengths of str1 and str2
        gcd_len = math.gcd(len(str1), len(str2))
        
        # The candidate substring is the prefix of length gcd_len
        candidate = str1[:gcd_len]
        
        # Check if the candidate divides both str1 and str2
        if canConstruct(str1, candidate) and canConstruct(str2, candidate):
            return candidate
        else:
            return ""    
