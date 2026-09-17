from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        sort_freq = {}
        max_freq = 0
        
        for num in nums:
            if num in freq:
                freq[num] += 1
                sort_freq[freq[num] - 1].remove(num)
                
                # Явно проверяем и создаем ключ, если нужно
                if freq[num] not in sort_freq:
                    sort_freq[freq[num]] = set()
                sort_freq[freq[num]].add(num)
            else:
                freq[num] = 1
                if 1 not in sort_freq:
                    sort_freq[1] = set()
                sort_freq[1].add(num)
            
            max_freq = max(max_freq, freq[num])
        
        ans = []
        while len(ans) < k and max_freq > 0:
            ans.extend(sort_freq[max_freq])
            max_freq -= 1
        
        return ans[:k]