class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_signature = [0] * 26

        for c in s1:
            s1_signature[ord(c) - ord('a')] += 1

        left = 0

        for right in range(len(s1), len(s2) + 1):

            signature = [0] * 26

            for c in s2[left:right]:
                signature[ord(c) - ord('a')] += 1

            if signature == s1_signature:
                return True

            left += 1

        return False

            



        