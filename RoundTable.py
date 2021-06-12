#https://www.codechef.com/ZCOPRAC/problems/ZCO12004


n = int(input())
lst = list(map(int, input().split()))

if n <= 2:
    print(min(lst))
else:
    flst = []
    flst.extend(lst)
    elst = []
    elst.extend(lst)
    for i in range(2,n):
        flst[i] += min(flst[i-1],flst[i-2])
        elst[n-i-1] += min(elst[n-i],elst[n-i+1])
    print(min(flst[-1],elst[0]))
