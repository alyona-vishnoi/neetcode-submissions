from collections import defaultdict 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      # sliding window of size len(s1). 

        n, m = len(s1), len(s2)
        if n > m:
            return False

        target = [0] * 26
        window = [0] * 26

        # build target freq
        for c in s1:
            target[ord(c) - ord('a')] += 1

        # build initial window freq
        for i in range(n):
            window[ord(s2[i]) - ord('a')] += 1

        if window == target:
            return True

        # slide the window
        for i in range(n, m):
            window[ord(s2[i]) - ord('a')] += 1          # add new right char
            window[ord(s2[i - n]) - ord('a')] -= 1      # remove left char
            if window == target:
                return True

        return False

        