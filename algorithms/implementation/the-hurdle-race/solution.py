import sys
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
dif = max(height) - k
if dif > 0:
    print(dif)
else:
    print(0)
