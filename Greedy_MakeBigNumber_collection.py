####################################################
## 단순한 편,테스트케이스1, 정확성 11/ 12통과
# 앞쪽에서부터 작은 수 K개 제거 
def solution(number, k):
    answer = ''
    numList= list(map(int, number))
    
    
    for i in range(k):
        for i in numList:
            if min(numList)== i:
                numList.remove(min(numList))

        
    for i in numList:
        i= str(i)
        answer+= i
    
    return answer

number= "1924"
print(solution(number, 2))
##############################################################
############################################################
## 테스트케이스 1/ 2, 정확성11/ 12 통과
# max값 앞의 숫자 개수와 K비교하여 k가 더 크면, max 앞의 숫자 지우고 뒤에 작은 수부터 남은 만큼 지우기

def solution(number, k):
    answer = ''
    numList= list(number)
    print(numList)
    sortNum= list(number)
    sortNum.sort(reverse=True)
    
    print(sortNum)

    for i in range(k):
        getInd= numList.index(sortNum[i])
        print("i= {}, getInd= {}, sortNum[i]= {}, ".format(i, getInd, sortNum[i]))
        if getInd< k :
    
            numList= numList[getInd:]
            print("getInd < k", numList)
            k-= getInd
            break
    
    for i in range(k):
        print("min(numList)", min(numList))
        numList.remove(min(numList))
            

    for i in numList:
        i= str(i)
        answer+= i
    
    return answer

number= "4177252841"
print(solution(number, 4))
##############################################################
############################################################
## 테스트케이스 1/ 2/ 3, 정확성 11통과_ timeOut발생
# 전체를 검사_오른쪽 인덱스와 비교
# k가 0보다 크면 제거할 인덱스의 value제거 후 다시 비교
# while문 탈출하면 제거할 인덱스의 value제거
def solution(number, k):
    answer = ''
    numList= list(number)
    removeList= []
    ind= 0

    while k> 0:
        if ind<len(number)- 1 and numList[ind]<numList[ind+ 1]:
            print("오른쪽 값이 더 클 때", ind, numList, numList[ind], numList[ind+1], "K= ", k)
            removeList.append(ind)
            k-= 1

        #한바퀴 다 돌고, k가 0보다 클때 제거할 인덱스로 value제거
        elif ind== len(number)- 1 and removeList:
            for i in range(len(removeList)- 1, -1, -1):
                print("index가 한바퀴를 다 돌았을 때, 제거할 index", removeList[i])
                numList.pop(removeList[i])
                removeList.pop(i)

            ind= -1                
            print("after for", numList, ind)    
            
        
        ind+= 1

   #제거할 value의 인덱스로 value 제거, 리스트에서 제거하는 것임으로 뒤에서부터 제거
    for i in range(len(removeList)- 1, -1, -1):
        print("While을 탈출해서 제거할 ind", removeList[i])
        numList.pop(removeList[i])


    for i in numList:
        answer+= str(i)
    
    return answer

number= "1231234"
print(solution(number, 3))
##############################################################
############################################################
## 테스트케이스 1/ 2/ 3, 정확성 11통과_ timeOut발생