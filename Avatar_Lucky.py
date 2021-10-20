score= str(input())
m= int(len(score)/2)
lSum= 0
rSum= 0

for i in range(m):
    lSum+= int(score[i])
    rSum+= int(score[m+i])

if lSum== rSum:
    print("LUCKY")
else:
    print("READY")
