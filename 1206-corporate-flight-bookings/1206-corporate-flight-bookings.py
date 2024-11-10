class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]* (n+1)


        for i,j,k in bookings:
            ans[i-1]+=k
            ans[j] = ans[j]-k

        ans.pop()
        prev = ans[0]

        for i in range(1,len(ans)):
            prev+=ans[i]
            ans[i] = prev

        return ans        