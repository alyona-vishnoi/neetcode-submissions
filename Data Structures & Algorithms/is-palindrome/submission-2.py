class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = s.lower()

        import string
        clean = ''.join(filter(lambda x: x not in string.punctuation, clean))

        cleanup = clean.replace(" ","")

        left = 0
        right = len(cleanup) - 1

        while left < right:
            if cleanup[left] != cleanup[right]:
                return False
            left+=1
            right-=1
            
        return True
        