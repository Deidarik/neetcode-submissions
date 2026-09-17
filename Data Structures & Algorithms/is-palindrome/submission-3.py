class Solution:

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        t = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                t +=char
        l_bound = 0
        r_bound = len(t) - 1
        while r_bound - l_bound > 0 if len(t) % 2 == 0 else r_bound - l_bound > 1:
              if t[l_bound] != t[r_bound]:
                 return False
              l_bound+=1
              r_bound-=1
        return True