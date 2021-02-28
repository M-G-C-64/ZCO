n = int(input())
lst = list(map(int, input().split()))

if n<3:
    print(0)
else:
    minn = min(lst[0],lst[1],lst[2])
    temp = [lst[0],lst[1],lst[2]]
    for i in range(1,n-2):
        temp.append(lst[i+2]+minn)
        minn = min(temp[i],temp[i+1],temp[i+2])
    print(minn)
