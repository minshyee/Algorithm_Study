#큰 수의 법칙

n, m, k= map(int, input().split())
alist= list(map(int, input().split()))

alist.sort(reverse=True)

result= 0

if m> 0:
    count= k
    for i in range(m):
        if count>0:
            result+= alist[0]
            count-=1
        else:
            result+= alist[1]
            count= k       
        print("result: ", result, "\tcount: ", count)

if k>m or m<0:
    print('올바르지 못한 입력값입니다.')
else:
    print(result)
