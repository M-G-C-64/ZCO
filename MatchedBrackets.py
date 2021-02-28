n = int(input())
lst = list(map(int, input().split()))

modrs = 1
modr = 0
odr = 0
stk = 0
mstk = 0
mstks = 1
for i in range(0,len(lst)):

    if lst[i] == 1:
        odr = odr +1
        if odr > modr:
            modr = odr
            modrs = i + 1
        if odr > 1:
            stk += 1

    if lst[i] == 2:
        odr = odr - 1
        if odr > 0:
            stk += 1
            if stk > mstk:
                mstk = stk
                mstks = i - mstk + 1
        if odr == 0:
            stk = 0

print(modr,modrs,mstk+2,mstks)

