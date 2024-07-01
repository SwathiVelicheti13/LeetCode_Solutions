class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)
        anagramList = []
        for wrd in strs:
            sort_word = "".join(sorted(wrd))
            anagramDict[sort_word].append(wrd)
        
        for value in anagramDict.values():
            anagramList.append(value)
        return anagramList
        # print(anagramDict.values())

        