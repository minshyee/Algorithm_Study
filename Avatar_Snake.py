n= int(input()) # 게임판의 크기
k= int(input()) # 사과의 개수
board= [[0]*n for i in range(n) ] #게임판 0- 게임판, 1- 뱀, 2- 사과
board[0][0]= 1
apple= []
turnInfo= []
time= 0
cursor= [0,0]
wayInfo= [[0,1],[1,0],[0,-1],[-1,0]] #우,하,좌,상
way= 0
snake= [[cursor[0], cursor[1]]] #뱀이 위치한 인덱스 정보 저장
escape= False

# 사과 좌표 정보
for i in range(k):
    apple.append(tuple(map(int, input().split()))) 

# 방향 전환 횟수
l= int(input())

# 방향 전환 정보
for i in range(l):
    turnInfo.append(list(input().split()))
    turnInfo[i][0]=int(turnInfo[i][0])
    
#보드판에 사과 추가
for i in range(k):
    board[apple[i][0]-1][apple[i][1]-1]= 2 # 보드판은 (1,1)부터 시작


while escape== False:
    if turnInfo and time == turnInfo[0][0]:
        if turnInfo[0][1]== "D":
            if way== 3:
                way= 0
            else:
                way+= 1 
        else:
            if way== 0:
                way= 3
            else:
                way-= 1 
        turnInfo.pop(0)

    # 뱀 이동
    # print("이동 좌표 ", cursor[0]+wayInfo[way][0], cursor[1]+wayInfo[way][1])
    if 0<= cursor[0]+wayInfo[way][0]<n  and 0<= cursor[1]+wayInfo[way][1]<n and [cursor[0]+wayInfo[way][0],cursor[1]+wayInfo[way][1]] not in snake:
        snake.append([cursor[0]+wayInfo[way][0],cursor[1]+wayInfo[way][1]])
        
        cursor[0]+=wayInfo[way][0]
        cursor[1]+=wayInfo[way][1]
            
        if board[cursor[0]][cursor[1]]== 0: #이동한 위치가 비었으면 
            board[cursor[0]][cursor[1]]= 1 # 뱀 머리 이동
            delInd= snake.pop(0)
            board[delInd[0]][delInd[1]]= 0 # 뱀 꼬리 이동
                     
        elif board[cursor[0]][cursor[1]]== 2: # 사과를 먹으면
            board[cursor[0]][cursor[1]]= 1 # 뱀 머리 이동

        # 뱀 이동 및 몸통 확인
        # for i in range(n):
            # print(board[i])  
    else: # 뱀 몸통을 만나거나 범위를 벗어났을 때 
        escape= True
        time+= 1
        # print("Else Time", time)
        break
    time+= 1
    # print("time", time)
            
        

print(time)
