#문제링크:https://school.programmers.co.kr/learn/courses/30/lessons/340198
#레벨1, 정답률 33%, 문제특징:단순 요구사항 구현

# 1. 정사각형을 만들 수 있는지 없는지 체크해주는 함수 구현
# 2. 아이디어를 생각하는데 꽤 오래걸렸다
# 3. 다른사람들의 코드를 보니 5중 for문 형태 이상이 나와 내 코드에 이상은 없었다. 오히려 함수화를 통해 가독성을 높임.

# 해결포인트
# 기능을 쪼개서 가독성을 높임
# 적절한 조건문의 사용

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
