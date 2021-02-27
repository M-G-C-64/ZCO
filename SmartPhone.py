n = int(input())
lst = []
for i in range(0,n):
    lst.append(int(input()))
lstt = sorted(lst, reverse=True)
temp = []
for i in range(0,len(lst)):
    temp.append((lstt[i])*(i+1))
print(max(temp))
