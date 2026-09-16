class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = {}
        for char in s:
            # .get(char, 0) вернет 0, если ключа еще нет, и прибавит 1
            count_s[char] = count_s.get(char, 0) + 1 
            
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
            
        # Словари в Python можно сравнивать напрямую!
        # Ручное сравнение в одну строку
        return len(count_s) == len(count_t) and all(count_s[char] == count_t.get(char, -1)  for char in count_s)