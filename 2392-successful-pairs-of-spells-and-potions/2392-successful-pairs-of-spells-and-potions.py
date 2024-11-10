class Solution:
    def lowerBound(self,potions,key):
            l = 0
            n = len(potions)
            h = n

            while l<h:
                mid = (l+h)//2

                if potions[mid]<key:
                    l = mid+1
                else:
                    h = mid
            return l

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        answers = [0]*len(spells)
        maxPotion = potions[-1]

        for i in range(len(spells)):
            spell = spells[i]
            minPotion = math.ceil(success/spell)

            ind = self.lowerBound(potions,minPotion)

            answers[i] = m -ind
        return answers
