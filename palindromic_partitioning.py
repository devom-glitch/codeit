from re import S


class Solution: 
    def __init__(self,s):
        self.s = s 
        self.mp = {}
        
    def is_palin(self,i,j):
        while(i<=j):
            if self.s[i] != self.s[j] : return False
            i+=1
            j-=1
        return True

    def dp(self,i):
        if i == len(self.s): return [[]]
        if i in self.mp.keys(): return self.mp[i]
        ans = [[]]
        for j in range(i,len(self.s)):
            if(self.is_palin(i,j)):
                res = self.dp(j+1)
                sub = self.s[i:j+1]
                for x in res:
                    x.append(sub)
                if len(res) == 0:
                    res.append({sub})
                for x in res:
                    ans.append(x)
        self.mp[i] = ans 
        return self.mp[i]
s = 'aa'
H = Solution(s)
res = H.dp(0)
print(res)
    