class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        result = 0
        for bit in range(24):  # Numbers up to 10^7 need at most 24 bits
            count = sum(1 for num in candidates if num & (1 << bit))
            result = max(result, count)
        return result