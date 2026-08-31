class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_words= ''.join(char.lower() for char in s if char.isalnum())

        start  = 0 
        end = len(clean_words) - 1 
        while start < end :
            if clean_words[start] != clean_words[end] : 
                return False
            start += 1
            end -= 1

        return True 

        