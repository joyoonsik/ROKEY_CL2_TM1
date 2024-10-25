# https://school.programmers.co.kr/learn/courses/30/lessons/161990
def solution(wallpaper):
    answer = []
    x = []
    y = []
    for i,v1 in enumerate(wallpaper):
        for j,v2 in enumerate(v1):
            if v2=='#':
                x.append(i)
                y.append(j)
    
    answer.append(min(x))
    answer.append(min(y))
    answer.append(max(x)+1)
    answer.append(max(y)+1)
    return answer
