class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            sortedS = ''.join(sorted(i))
            if sortedS not in dic:
                dic[sortedS] = []
            dic[sortedS].append(i)
        return list(dic.values())