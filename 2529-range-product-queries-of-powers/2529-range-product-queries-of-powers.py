class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = pow(10,9)+7
        powers = []
        binary = bin(n)[2:]
        res = []
        for ind,val in enumerate(binary[::-1]):
            if val == '1':
                powers.append(pow(2,ind))
        
        for i in range(1,len(powers)):
            powers[i] = powers[i]*powers[i-1]

        for l,r in queries:
            if l == 0:
                res.append((powers[r])%MOD)
            else:
                res.append((powers[r]//powers[l-1])%MOD)
        return res

                
        # while n > 0:

        #     if n & 1:
        #         powers.append(2**i)
        #     n >>= 1
        #     i += 1
        # answers = []
        # for i in queries:
        #     prod = 1
        #     for val in range(i[0],i[1]+1):
        #         prod = prod *powers[val]
        #     answers.append((prod)%(109 + 7) )
        # return answers

        