def squre(n,x,y,park):
    for i in range(n):
        for j in range(n):
            if park[y+i][x+j]!='-1':
                return False
    return n

def solution(mats, park):
    col = len(park)
    row = len(park[0])
    mats = sorted(mats)
    answer = -1
    
    for n in mats:
        tmp=False
        for y in range(col):
            for x in range(row):
                if (x+n-1<row) and (y+n-1<col):
                    tmp=squre(n,x,y,park)
                if tmp:
                    answer=tmp
                    break
            if tmp:
                break   
    return answer
