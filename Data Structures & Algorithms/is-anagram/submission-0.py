class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_freq={}
        t_freq={}
        for ss in s:
            if ss in s_freq:
                s_freq[ss]+=1
            else:
                s_freq[ss]=1
        for tt in t:
            if tt in t_freq:
                t_freq[tt]+=1
            else:
                t_freq[tt]=1
        if s_freq==t_freq:
            return True
        else:
            return False
                
        