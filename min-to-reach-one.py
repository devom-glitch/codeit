# you are given number and reduce to 1 
# reduce options 1. reduce n-1 2. divide by 3 3. divide by 2 
import math
n = 10 
dp = [-1] * (n + 1)

def min_reach(n):
    if n == 1:
        return 0
    ans = math.inf
    if n % 2 == 0:
        ans = min(ans,min_reach(n/2))
    if n % 3 == 0:
        ans = min(ans,min_reach(n/3))
    ans = min(ans,min_reach(n-1))
    ans = ans + 1
    return ans 

print(min_reach(n))