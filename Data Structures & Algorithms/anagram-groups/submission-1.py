from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for w in strs:
            k="".join(sorted(w))
            d[k].append(w)
        return list(d.values())