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
