def solution(n, lost, reserve):
    lost.sort() #13, 18번 케이스 원인
    reserve.sort() #13, 18번 케이스 원인
    inNum= 0
    check= [0]* n

    # 1, 2, 5, 6, 10, 12번 케이스 원인(-1/1에서 +-= 1로 변경)
    for j in lost:
        check[j-1]-= 1

    for j in reserve:
        check[j-1]+= 1
    ######################
    while inNum <len(lost):
        loTemp= lost[inNum]- 1

        for i in range(len(reserve)):
            temp= reserve[i]- 1

            if check[loTemp]== -1 and check[temp]== 1:
                if lost[inNum]== reserve[i]- 1 or lost[inNum]== reserve[i]+ 1:
                    check[temp]= 0
                    check[loTemp]= 0
                    break

        inNum+=1

    return n- check.count(-1)
