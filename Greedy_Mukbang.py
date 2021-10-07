def solution(food_times, k):
    answer = 0
    inNum= 0
    i= 0 #시간

    while i< k:
        if food_times[inNum]> 0:
            food_times[inNum]-= 1
            i+=1        
            
        if len(food_times)- 1== inNum:
            inNum= 0
        else:
            inNum+= 1
        
        if max(food_times)== 0:
            answer= -1 
            break    

    #k초에 먹은 음식 다음이 0일 때
    if answer!= -1 and food_times[inNum]== 0:
        temp= list(filter(lambda x:food_times[x]> 0, range(len(food_times)))) #남아있는 음식의 인덱스값 

        if temp and max(temp)> inNum:
            for j in temp:
                if inNum< j:
                    inNum= j
                    break
        else:
            inNum= temp[0]
                
    if answer!= -1:
        answer= inNum+1 
    
    return answer
