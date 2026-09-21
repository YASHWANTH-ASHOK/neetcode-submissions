class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        HashMap = set()

        for n in nums:
            if n in HashMap:
                return True
            else:
                HashMap.add(n)
        return False


