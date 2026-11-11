class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = Counter(nums)
        num_freq = dict(sorted(num_freq.items(), key=lambda item: item[1], reverse=True))
        return list(num_freq.keys())[:k]
