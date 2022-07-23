
class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        st = [A[N-1]]
        max_right = A[N-1]
        for i in range(N-2,-1,-1):
            if A[i] >= max_right:
                st.append(A[i])
                max_right = A[i]
        return reversed(st)
            