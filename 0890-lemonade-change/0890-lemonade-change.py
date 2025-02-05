class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveChange = 0
        tenChange = 0
        for val in bills:
            if val == 5:
                fiveChange+=1

            elif val == 10:
                if fiveChange>0:
                    fiveChange = fiveChange-1
                    tenChange+=1
                else:
                    return False
            elif val == 20:
                if tenChange>0 and fiveChange>0:
                    fiveChange=fiveChange-1
                    tenChange= tenChange-1
                elif fiveChange>=3:
                    fiveChange=fiveChange-3
                else:
                    return False

                
        return True

        