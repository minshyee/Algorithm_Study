# 모험가 길드

n= int(input())
fear= list(map(int, input().split()))

fear.sort()
group= 0
c= 0

for i in range(n):
    if fear[c]< n-c:
        group+= 1
        c+= fear[c]
    else:
        break

print(group)
