class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        people = list(range(1,(n+1)))
        ind = 0

        while len(people)>1:
            ind = (ind+(k-1))%len(people)
            people.pop(ind)

        return people[0]

