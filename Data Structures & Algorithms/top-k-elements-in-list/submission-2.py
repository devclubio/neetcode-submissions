class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        lst = [x for x,y in c.most_common(k)]
        return lst
        