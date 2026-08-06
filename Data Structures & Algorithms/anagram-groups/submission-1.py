class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)

        for s in strs:
            sortedS= ''.join(sorted(s))
            hash[sortedS].append(s)

        return list(hash.values())