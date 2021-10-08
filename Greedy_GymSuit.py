def solution(n, lost, reserve):
    answer = n- len(lost)
    inNum= 0
    check= [1]* n
    for j in lost:
        check[j-1]= 0
    

    while inNum<len(lost):
        for i in range(len(reserve)):
            temp= reserve[i]- 1
            if check[temp]== 1:
                print(check, lost[inNum], reserve[i])
                if lost[inNum]== reserve[i]:
                    answer+=1
                    check[temp]= 0
                    print("==")
                    break
                    
                elif lost[inNum]== reserve[i]-1:
                    answer+=1
                    check[temp]= 0
                    print("-1")
                    break
                    
                elif lost[inNum]== reserve[i]+1:
                    answer+=1
                    check[temp]= 0
                    print("+1")
                    break
            
        inNum+=1
                
            
    return answer, check

#전체 학생수: n, 도난당한 학생 리스트: lost, 여분 체육복 학생 리스트: reserve


n= int(input())
lost= list(map(int, input().split()))
reserve= list(map(int, input().split()))

print(solution(n, lost, reserve), )