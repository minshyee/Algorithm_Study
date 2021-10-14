def solution(name):
    answer = 0
    gInd= list(filter(lambda x: name[x]=="A", range(len(name))))
    
    
    if len(name)== 3 and name[1]=="A":
        for i in range(0, len(name), 2):
            if i== "N":
                answer+= 13
                print(answer, "i=N", i, ord(name[i]), sep="\t")
            elif ord(name[i])> ord("N"):
                answer+= ord("Z")- ord(name[i])+ 1
                print(answer, "i>N", i, ord(name[i]), ord("Z"), sep="\t")
            else:
                answer+= ord(name[i])- ord("A")
                print(answer, "i<N", i, ord(name[i]), ord("A"), sep="\t")
            answer+= 1
    
    else:
        for i in name:
            if i== "N":
                answer+= 13
                print(answer, "i=N", i, ord(i), sep="\t")
            elif ord(i)> ord("N"):
                answer+= ord("Z")- ord(i)+ 1
                print(answer, "i>N", i, ord(i), ord("Z"), sep="\t")
            else:
                answer+= ord(i)- ord("A")
                print(answer, "i<N", i, ord(i), ord("A"), sep="\t")
            answer+= 1
        
    return answer-1




#####################################################################
def solution(name):
    answer = 0
    aIndList= list(filter(lambda x: name[x]== "A", range(1, len(name)-1)))
    nIndList= list(filter(lambda x: name[x]!= "A", range(len(name))))
    # value= [("A", 0), ("B", 1), ("C", 2), ("D", 3), ("E", 4), ("F", 5), ("G", 6), 
    #         ("H", 7), ("I", 8), ("J", 9), ("K", 10), ("L", 11), ("M", 12), ("N", 13), 
    #        ("O", 12), ("P", 11), ("Q", 10), ("R",9), ("S", 8), ("T",7), ("U",6), 
    #         ("V", 5), ("W", 4), ("X", 3), ("Y", 2), ("Z",1)]

    
    if len(aIndList)==len(name)- 2:
        ind= 0
        for i in range(2):
            if name[ind]== "N":
                answer+= 13
                
            elif ord(name[ind])> ord("N"):
                answer+= ord("Z")- ord(name[ind])+ 1
                
            else:
                answer+= ord(name[ind])- ord("A")
                
            ind= len(name)-1
            answer+=1
            
        
    else:
        for i in name:
            if i== "N":
                answer+= 13
                
            elif ord(i)> ord("N"):
                answer+= ord("Z")- ord(i)+ 1
                
            else:
                answer+= ord(i)- ord("A")
            answer+= 1

        
        
#     if len(name)== 3 and name[1]=="A":
#         for i in range(0, len(name), 2):
#             if i== "N":
#                 answer+= 13
                
#             elif ord(name[i])> ord("N"):
#                 answer+= ord("Z")- ord(name[i])+ 1
                
#             else:
#                 answer+= ord(name[i])- ord("A")
                
#             answer+= 1
    
#     else:
#         for i in name:
#             if i== "N":
#                 answer+= 13
                
#             elif ord(i)> ord("N"):
#                 answer+= ord("Z")- ord(i)+ 1
                
#             else:
#                 answer+= ord(i)- ord("A")
#             answer+= 1
        
    return answer-1
#####################################################################
### 54.5 #3,4,7,8,11
def solution(name):
    answer = 0
    ind= 0
    aIndList= list(filter(lambda x: name[x]== "A", range(1, len(name)-1)))
    nIndList= list(filter(lambda x: name[x]!= "A", range(len(name))))
    value= {"A":0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, 
            "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, 
           "O": 12, "P": 11, "Q": 10, "R": 9, "S": 8, "T":7, "U":6, 
            "V": 5, "W": 4, "X": 3, "Y": 2, "Z":1}
    
    if len(aIndList)== len(name)-2:
        for i in range(2):
            answer+= value[name[ind]]+ 1
            print(ind)
            ind= len(name)-1
    
    else:
        for i in name:
            answer+= value[i]+ 1
        
        

        
    return answer-1

#####################################################################################
#########63.3 #3,4,7,8
def solution(name):
    answer = 0
    ind= 0
    way= 1
    aIndList= list(filter(lambda x: name[x]== "A", range(1, len(name)-1)))
    nIndList= list(filter(lambda x: name[x]!= "A", range(1, len(name)-1)))
            
    value= {"A":0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, 
            "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, 
           "O": 12, "P": 11, "Q": 10, "R": 9, "S": 8, "T":7, "U":6, 
            "V": 5, "W": 4, "X": 3, "Y": 2, "Z":1}
    
    # 첫글자와 마지막 글자가 A가 아닐 때
    if len(aIndList)== len(name)-2:
        for i in range(2):
            answer+= value[name[ind]]+ 1
            ind= len(name)-1
            
    # 순행
    elif len(aIndList)<int(len(name)/2): 
        for i in range(len(name)):
            answer+= value[name[i]]+ 1
    
    # A가 연속으로 존재하고 뒤로 가는 것이 더 적게 움직일 때
    else:
        for i in range(len(name)):
            if ind in aIndList and len(name)-ind >ind and way== 1:
                way= -1
                answer+= ind
                print("연속", name[ind], ind, value[name[ind]],answer)
                ind= len(name)- 1
                
            elif way== -1 and ind not in aIndList:
                
                answer+= value[name[ind]]+ 1
                print("역순", name[ind], ind, value[name[ind]], answer )
                ind-= 1
                
            elif way== -1 and ind in aIndList:
                answer-=1
                break
            else:
                answer+= value[name[ind]]+ 1
                print("순행", name[ind], ind, value[name[ind]],answer)
                ind+= 1
                
        

        
    return answer-1