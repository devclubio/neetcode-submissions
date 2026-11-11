class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = [0] * 26
        for i in range(len(s)):
            freq[ord(s[i]) % 26] += 1
            freq[ord(t[i]) % 26] -= 1
        
        for num in freq:
            if num:
                return False
        return True