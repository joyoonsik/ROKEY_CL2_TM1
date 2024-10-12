# 기능개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    releases = []
    for i in range(len(progresses)):
        needDay = (100 - progresses[i]) / speeds[i]
        if needDay % 1 > 0:
            needDay = needDay // 1 + 1
        releases.append(int(needDay))
    
    releaseDay = 0
    count = 0
    
    for element in releases:
        if releaseDay == 0:
            releaseDay = element
            count = 1
        else:
            if releaseDay >= element:
                count += 1
            else:
                answer.append(count)
                releaseDay = element
                count = 1
                
    if releaseDay:
        answer.append(count)
    
    return answer

# print(solution(
#     [93, 30, 55], [1, 30, 5]))