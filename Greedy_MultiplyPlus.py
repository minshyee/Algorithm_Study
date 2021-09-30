# 곱하기 혹은 더하기
sNum= input()
result= 0

for i in sNum: # 한자리씩 읽어오기
    i= int(i) # int로 형변환
    if i > 1 and result > 1: #큰수가 만들어질 조건 **기존: if i > 2 and result != 0:
        result*= i

    else:
        result+= i

print(result)
