
s = '1223'
memo = [-1] * len(s)
def dp(i):
    if i == len(s): return 1;
    if(memo[i] != -1): return memo[i]
    ans = 0 
    if(s[i] >= '1' and s[i] <='9'): ans += dp(i+1)
    if(s[i] == '1' and i+1 < len(s)): ans += dp(i+2)
    if(s[i] == '2' and s[i+1] <= '6' and i + 1 < len(s)): ans += dp(i+2)
    memo[i] = ans
    return memo[i]

print(dp(0))