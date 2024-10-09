# 점 찍기
# https://school.programmers.co.kr/learn/courses/30/lessons/140107

def solution(k, d):
    answer = 0
    b = 0
    while b <= d:
        a = (d**2 - b**2)**0.5
        a //= 1
        answer += a // k + 1
        b += k
    
    return answer

# print(solution(2, 4))