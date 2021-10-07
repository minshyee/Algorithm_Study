def solution(food_times, k):
    answer = 0
    inNum= 0
    for i in range(k+1):
        if food_times[inNum]>0:
            food_times[inNum]-=1
        if len(food_times)-1== inNum:
            inNum= 0
        else:
            inNum+=1
    answer= inNum+1
    
    return answer

foodTimes= list(map(int, input().split()))
k= int(input())

print(solution(foodTimes, k))