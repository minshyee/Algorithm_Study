def solution(n, lost, reserve):
    inNum= 0
    check= [1]* n
    for j in lost:
        check[j-1]= -1
    

    while inNum<len(lost):
        loTemp= lost[inNum]- 1
        
        for i in range(len(reserve)):
            temp= reserve[i]- 1
            
            if check[temp]== 1 and check[loTemp]== -1:
                if lost[inNum]== reserve[i]- 1 or lost[inNum]== reserve[i] or lost[inNum]== reserve[i]+ 1:
                    check[temp]= 0
                    check[loTemp]= 0
                    break
                    
        inNum+=1
        
                
            
    return n- check.count(-1)
