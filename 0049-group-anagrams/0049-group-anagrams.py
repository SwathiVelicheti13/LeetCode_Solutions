class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)

        for val in strs:
            wordList = list(val)
            sortedWord = ''.join(sorted(wordList))
            anagramDict[sortedWord].append(val)
        return list(anagramDict.values())