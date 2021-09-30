# 모험가 길드

n= int(input())
fear= list(map(int, input().split()))

fear.sort()
group= 0
c= 0

for i in range(n):
    if fear[c]<= n-c: # 최소한 해당 공포도 만큼의 사람이 있어야 하므로
        t= fear[c]
        
        for i in range(n-t):
            if t-c == fear[t-1]: # 그룹의 끝 인덱스인 사람(공포도가 가장 큰 사람)의 공포도와 만들어진 그룹의 인원수가 같은지 확인
                group+= 1
                c+= fear[t] # c+= fear[t]-1 해당 공포도만큼 그룹이 만들어 졌으니 다음 인덱스는 해당 공포도만큼 이동
                break

            else:
                t+=1

    else:
        break

print(group)
