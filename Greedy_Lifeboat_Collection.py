############################################################
#######################################################
## 테스트 케이스 통과, 2/ 8/ 14/ 15 정확성 통과_그외 실패, 4/ 5효율성 통과_ 그외 TimeOut
# 제한 무게에서 0번 인덱스 값을 뺀 값이 존재하면 해당 값과 0번 인덱스 제거하고 +1, 아니면 0번 인덱스 제거하고 +1
people= [70, 80, 50]	
limit= 100

def solution(people, limit):
    answer = 0
    # ind= 0

    if min(people)> limit/2:
        answer= len(people)
    else:
        while people:
            minPeople= limit- people[0]
            
            if minPeople in people:
                print(people, answer)

                if len(people)> 1:
                    people.remove(minPeople)

        
            people.pop(0)
            answer+= 1
                


    return answer

print(solution(people, limit))

############################################################
#######################################################
## 테스트 케이스 통과, 정확성 통과, 2/ 3/ 4/ 5효율성 통과_ 1번 TimeOut
# people을 오름차순으로 정렬한 뒤, 가장 큰 무게와 가장 작은 무게 비교
#_55분 정도
people= [50, 70, 80, 50]	
limit= 100

def solution(people, limit):
    answer = 0
    # ind= 0

    if min(people)> limit/2:
        answer= len(people)
    else:
        people.sort()
        
        while people:
            minPeople= limit- people[-1]
            
            if minPeople >= people[0]:
                print(people, answer)

                if len(people)> 1:
                    people.pop(0)

        
            people.pop(-1)
            answer+= 1
                


    return answer

print(solution(people, limit))
############################################################
#######################################################
## 테스트 케이스 통과, 2/ 6/ 8/ 11/ 12/ 13/ 14/ 15정확성 통과, 2/ 4/ 5효율성 통과_ 1/ 3번 실패
# people을 오름차순으로 정렬한 뒤, 가장 큰 무게와 가장 작은 무게 비교
people= [100,500,500,900,950]	
limit= 1000

def solution(people, limit):
    answer = 0
    sInd= 0
    lInd= len(people)- 1

    if min(people)> limit/2:
        answer= len(people)
    else:
        people.sort()
        
        while lInd>= sInd :
            if people[lInd] <limit/2:
                answer= answer+ len(people)/2 if len(people)%2== 0 else answer+ int(len(people)/2)+1
                break

            elif limit- people[lInd] >= people[sInd]:
                print(people[sInd],people[lInd], answer)
                sInd+= 1


        
            lInd-= 1
            answer+= 1
                


    return answer

print(solution(people, limit))
############################################################
#######################################################
## 테스트 케이스 통과,정확성 통과, 효율성 통과
# people을 오름차순으로 정렬한 뒤, 가장 큰 무게와 가장 작은 무게 비교
#_1시간 32분
people= [10, 10, 10, 20, 30, 40, 50, 50, 60, 80, 80]	
limit= 100

def solution(people, limit):
    answer = 0
    sInd= 0
    lInd= len(people)- 1

    if min(people)> limit/2:
        answer= len(people)
    else:
        people.sort()
        
        while lInd>= sInd :
            # print(lInd, sInd)
            if people[lInd] <limit/2:
                answer= answer+ (lInd-sInd+1)/2 if (lInd-sInd+1)%2== 0 else answer+ int((lInd-sInd+1)/2)+1
                break

            elif limit- people[lInd] >= people[sInd]:
                # print(people[sInd],people[lInd], answer)
                sInd+= 1


        
            lInd-= 1
            answer+= 1
                


    return answer

print(solution(people, limit))
