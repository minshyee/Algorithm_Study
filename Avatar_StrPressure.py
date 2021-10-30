## 숫자 자릿수 체크


s= "aabbaccc"

lenList= []

for i in range(1, int(len(s)/2)+1): #문자열 자르는 단위
    ind= 0
    l= 0
    count= 1
    d=0
    
    for j in range(len(s)): #전체 문자열 검사
        if ind+ i> len(s): #현재 인덱스범위가 전체 길이를 벗어나면 반복문 탈출
            print(ind, ind+2*i)
            break
        if s[ind:ind+i]== s[ind+i:ind+ 2*i]:
            l+=i
            count+= 1
            
            # print(len(s), l)
        elif count>1:
            d+= len(str(count)) #숫자의 자릿수 정보
            count= 1
        ind+=i
    lenList.append(len(s)-l+d)
    #print(lenList)

print(min(lenList)) 
