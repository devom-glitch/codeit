event_days = int(input())
dutyperday = [int(i) for i in input().split()]
dp = [0] * event_days 
dp[0] = dutyperday[0]
dp[1] = dutyperday[1]
dp[2] = dutyperday[2]
for i in range(3,event_days):
    dp[i] = min(dp[i-1],dp[i-2],dp[i-3]) + dutyperday[i]
print(min(dp[-3:]))