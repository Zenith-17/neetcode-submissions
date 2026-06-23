class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)

        n1, n2 = len(s1), len(s2)

        if n2 < n1:
            return False

        s = ""
        for i in range(n1):
            s += s2[i]

        if sorted(s) == s1:
            return True

        right = n1

        while right < n2:
            s = s[1:] + s2[right]

            if sorted(s) == s1:
                return True

            right += 1

        return False