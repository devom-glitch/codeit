nums = [2,7,9,3,1]

def houserob(nums):
    n = len(nums)
    if n == 1: return nums[0]
    a = [nums[0], max(nums[0],nums[1])]
    for i in range(2,n):
        ans = max(nums[i]+a[i-2],a[i-1])
        a.append(ans)
    return a[n-1]

print(houserob(nums))
        