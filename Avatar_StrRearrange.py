s= input()
num= 0
strList= []

for i in range(len(s)):

    if ord(s[i])< ord("A"):
        num+= int(s[i])
    else:
        strList.append(s[i])

strList.sort()
total= ''.join(strList)+ str(num)
print(total)