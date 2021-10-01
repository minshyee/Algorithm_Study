# 문자열 뒤집기
str= input()

count= 0 #연속된 문자열의 수

for i in range(len(str)-1):
    if str[i]!= str[i+1]: # 이전 문자와 다른 문자이면 count
        count+=1 
          
if count% 2 == 0:# count는 해당 문자열 그룹의 시작과 끝에 증가함으로 나눠줌
    count= int(count/ 2)
    
else:
    count= int(count/2+ 1)
    

print(count)