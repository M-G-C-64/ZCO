def run(i):
    global inilst
    global z
    global l

    if i == 1:#move left
        if z>0:
            z = z-1
    elif i == 2:#move right
        if z<(int(R)-1):
            z = z+1
    elif i == 3:#pick up box
        if l == 0:
            if inilst[z]>0:
                inilst[z] = inilst[z]-1
                l = 1
    elif i == 4:#drop box
        if l == 1:
            if inilst[z] < int(H):
                inilst[z] = inilst[z]+1
                l = 0
    else:
        return 0

R, H = input().split()
inilst = list(map(int, input().split()))
funlst = list(map(int, input().split()))

z = 0
l = 0
for i in funlst:
    run(i)
print(*inilst)
