def move(ind, name, side):
    start= ind
    count= 1

    while name[ind]== name[ind+side]:
        if ind+side< 0:
            ind= len(name)- 1

        elif ind+ side>len(name)-1:
            ind= 0

        if name[ind]== name[ind+side]:
            count+=1

        ind+=side
    end= ind
    stEnd=[count, start, end]
    
    return stEnd

def solution(name):
    # answer= 0
    lrMove= 0
    udMove= 0
    ind= 0
    way= 1
    aIndList= list(filter(lambda x: name[x]== "A", range(1, len(name)-1)))
    nIndList= list(filter(lambda x: name[x]!= "A", range(len(name))))

    value= {"A":0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, 
            "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, 
           "O": 12, "P": 11, "Q": 10, "R": 9, "S": 8, "T":7, "U":6, 
            "V": 5, "W": 4, "X": 3, "Y": 2, "Z":1}

    # A가 존재할 때, 연속된 A에 대한 정보 저장
    if aIndList:
        contiA= []
        for i in aIndList:
            contiA.append(move(i, name, 1))
    
        maxInfo= max(contiA)
    
    # 첫글자와 마지막 글자가 A가 아닐 때
    if len(aIndList)== len(name)-2:
        for i in range(2):
            udMove+= value[name[ind]]
            lrMove+= 1
            ind= len(name)-1
        lrMove-=1
            
    else:
        #0번에서 끝번을 먼저 가는 것이 더 빠른 경우
        if len(name)-1 in nIndList and len(name)-2== maxInfo[2]: 
            udMove+= value[name[len(name)-1]]
            lrMove+= 2
            for i in range(len(name)-1):
                udMove+= value[name[ind]]
                lrMove+= 1

        else:
            for i in range(len(name)):    
                if ind in aIndList:
                    if len(name)-ind >ind: #남은 갯수가 현재 인덱수 보다 크면 되돌아 가기
                        lrMove+= ind- 2
                        ind= len(name)
                        way=-1
                    elif : # 연속된 A의 개수보다 다음 글자까지의 이동이 적을 때
                        
                        
                elif ind in nIndList:
                    nIndList.remove(ind)
                    
                if ind!= len(name):
                    udMove+= value[name[ind]]
                    
                if not nIndList:
                    break
                else:
                    lrMove+=1
                    ind+=way
            
    answer= lrMove+ udMove
    
    return answer