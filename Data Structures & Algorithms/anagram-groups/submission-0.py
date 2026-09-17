class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 58
            for c in s:
                if c.isalpha():
                    count[ord(c) - ord('A')] += 1
            res[tuple(count)].append(s)
        return list(res.values())