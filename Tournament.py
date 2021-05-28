def summ(lst):
    sumlst = [0]*(len(lst)+1)
    for i in range(1,len(lst)+1):
        sumlst[i] = lst[i-1]+sumlst[i-1]
    sumlst.pop(0)
    return sumlst[::-1]

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

sumlst = summ(lst[::-1])
trev = 0

for i in range(n-1):
    trev += abs((lst[i])*(n-1-i) - sumlst[i+1])

print(trev)
