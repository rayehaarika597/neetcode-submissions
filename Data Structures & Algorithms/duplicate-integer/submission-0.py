class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for value in freq.values():
            if value>1:
                return True
        else:
            return False
        
        