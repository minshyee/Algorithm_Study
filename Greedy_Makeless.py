# n개의 동전으로 만들 수 없는 가장 작은 정수 만들기s
from itertools import combinations

n= int(input())
coin=list(map(int, input().split()))
result= 0
temp=[]
coin.sort()

if coin[0] != 1: # 가지고 있는 동전 중에 1이 없다면 만들 수 없는 최소값은 1 
    result= 1

else:
    for i in range(1, n+1):
        temp1=list(combinations(coin, i)) # coin으로 만들 수 있는 조합 찾기
        temp+=temp1 # temp에 모두 담기
        
    makeNum= []
    for i in range(len(temp)): #combimations가 tuple형식으로 조합
        temp1= list(temp[i]) #list로 변환한 뒤
        makeNum.append(sum(temp1)) # 각 조합으로 만든 금액 저장

    set_temp=set(makeNum) # set을 이용해 중복 제거
    makeNum=list(set_temp)

    for i in range(len(makeNum)): 
        if i+1!= makeNum[i]: # 1부터 만들어진 금액을 비교
            result= i+1 # 만들 수 없는 금액 
            break
        else:
            result= sum(coin)

print(result)