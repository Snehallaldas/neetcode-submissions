class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frq = {}
        a = []
        for num in nums:
            if num not in frq:
                frq[num] = 1
            else:
                frq[num] += 1
        
        frq = sorted(frq.items(), key=lambda x: x[1], reverse=True)
        
        result = []

        for number, frequency in frq[:k]:
            result.append(number)
        return result