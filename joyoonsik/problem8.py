# https://school.programmers.co.kr/learn/courses/30/lessons/172928
def solution(park, routes):
    for idx,i in enumerate(park):
        if "S" in i:
            answer=[idx,i.index('S')]
            break
        
    for i in routes:
        vector = i.split(" ")[0]
        scala = int(i.split(" ")[1])
        check=True
        
        if vector=='E':
            for j in range(1,scala+1):
                if answer[1]+j>=len(park[0]):
                    check=False
                    break
                if park[answer[0]][answer[1]+j]=='X':
                    check=False
                    break
            if check:
                answer[1]+=scala
        
        elif vector=='W':
            for j in range(1,scala+1):
                if answer[1]-j<0:
                    check=False
                    break
                if park[answer[0]][answer[1]-j]=='X':
                    check=False
                    break
            if check:
                answer[1]-=scala
        
        elif vector=='S':
            for j in range(1,scala+1):
                if answer[0]+j>=len(park):
                    check=False
                    break
                if park[answer[0]+j][answer[1]]=='X':
                    check=False
                    break
            if check:
                answer[0]+=scala
            
        elif vector=='N':
            for j in range(1,scala+1):
                if answer[0]-j<0:
                    check=False
                    break
                    
                if park[answer[0]-j][answer[1]]=='X':
                    check=False
                    break
            if check:
                answer[0]-=scala

    return answer
