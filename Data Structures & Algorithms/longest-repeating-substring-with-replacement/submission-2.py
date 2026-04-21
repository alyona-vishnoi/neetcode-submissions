from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        l = 0
        result = 0

        for r in range(len(s)):
            ch = s[r]
            # update counts for what right pointer is pointing to
            # bc thats the one we incrementing
            freq[ord(ch) - ord('A')] += 1

            # If window invalid, shrink from left until valid
            while ((r - l + 1) - max(freq)) > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result


        