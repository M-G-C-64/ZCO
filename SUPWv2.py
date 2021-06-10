#https://www.codechef.com/ZCOPRAC/problems/ZCO14002

n = int(input())
lst = list(map(int, input().split()))
temp = [0,0,0]
lst = temp+lst

res = []
res.extend(lst)


for i in range(4,n+3):
	res[i] = lst[i] + min(res[i-1],res[i-2],res[i-3])
print(min(res[-3:]))
