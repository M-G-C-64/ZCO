n = int(input())
lst = list(map(int, input().split()))

lst.sort()
tsum = lst[0]
temp = [tsum]
for i in range(1,len(lst)):
    tsum += lst[i]
    temp.append(tsum)
count = 0
for i in range(1, len(lst)):
    count += ((n-i)*lst[-i])-temp[-(1+i)]
print(count)

