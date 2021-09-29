# 모험가 길드

n= int(input())
fear= list(map(int, input().split()))

fear.sort()
group= 0
c= 0

for i in range(n):
    if fear[c]<= n-c:
        t= fear[c]
        
        for i in range(n-t):
            if t-c == fear[t-1]:
                group+= 1
                c+= fear[t]
                break

            else:
                t+=1

    else:
        break

print(group)
