import math as m
from statistics import mean

'''
n = int(input('個数の入力>> '))
nlist =list()
for i in range(1, n + 1):
    v =float(input('{}個目の値の入力>> '.format(i)))
    nlist.append(v)
vmax = max(nlist)
vmin = min(nlist)
print('最大値:', vmax)
print('最小値:', vmin)
'''
n = int(input('個数の入力>> '))
nlist =list()
for i in range(1, n + 1):
    v =float(input('{}個目の値の入力>> '.format(i)))
    nlist.append(v)
for i in range(len(nlist)):
    if i == 0:
        vmax = nlist[0]
    elif i >= 1:
        if nlist[i] > vmax:
            vmax = nlist[i]
vmin = min(nlist)
mean = mean(nlist)
#mean = sum(nlist) / len(nlist)
print('最大値:', vmax)
print('最小値:', vmin)
print('平均値:', mean)