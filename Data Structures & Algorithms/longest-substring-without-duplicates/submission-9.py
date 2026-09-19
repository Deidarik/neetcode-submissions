class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or s =="":
            return 0
        left = 0
        s_map = {}
        answer = 1
        for right in range(0, len(s)):
            if s[right] in s_map:
                left = max(left, s_map[s[right]] + 1)
                s_map[s[right]] = right
            else:
                s_map[s[right]] =  right
            answer = max(answer, right - left + 1)
        return answer
