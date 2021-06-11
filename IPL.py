#https://www.codechef.com/ZCOPRAC/submit/ZCO14004

n = int(input())
lst = list(map(int, input().split()))

res = [0]*n
res[0] = lst[0]

for i in range(1,n):
    res[i] = max(res[i-1], lst[i]+lst[i-1]+res[i-3], lst[i]+res[i-2])

print(res[-1])
