dp = [-1] * 1000
def rodcut(n,prices):
    if n == 0: return 0
    if dp[n] != -1: return dp[n]
    ans = 0 
    for i in range(1,n+1):
        ans = max(ans,prices[i] + rodcut(n-i,prices))
    dp[n] = ans 
    return ans
n = 8
prices = [None,1,3,4,5,7,9,10,11]
print(rodcut(n,prices))