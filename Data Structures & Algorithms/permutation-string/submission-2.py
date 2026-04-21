from collections import defaultdict 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      # sliding window of size len(s1). 

      if len(s1) > len(s2):
        return False

      l = 0
      r = l + len(s1) - 1

      target = [0] * 26
      for c in s1:
        target[ord(c) - ord('a')]+=1

      running_freq = [0] * 26

      # first window
      for i in range(len(s1)):
        ch = s2[i]
        running_freq[ord(ch) - ord('a')]+=1

      # sliding winow
      while r < len(s2):
        if running_freq == target:
            return True
        else:
            if r + 1 == len(s2):
                return False
            
            ch_l = s2[l]
            running_freq[ord(ch_l) - ord('a')]-=1
            l +=1
            r +=1
            ch_r = s2[r]
            running_freq[ord(ch_r) - ord('a')]+=1

      return False

        