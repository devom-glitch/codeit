import math 

def buy_apple(n,k,prices):
    money = [0] * (k+1)
    money[0] = 0 
    for i in range(1,k+1):
        min_cost = math.inf
        for j in range(1,i+1):
            print(i,j)
            if prices[j] != -1 and money[i-j] != math.inf:
                cost = prices[j] + money[i-j]
                min_cost = min(min_cost,cost)
        money[i] = min_cost 
    return money

print(buy_apple(4,4,[None,2,4,8,7]))