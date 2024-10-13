# 점프와 순간 이동
# https://school.programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    k = 0
    while True:
        if n == 0:
            break
        elif n % 2 == 1:
            n -= 1
            k += 1
        else:
            n /= 2
    return k

# def solution(n):
#     return bin(n).count('1')

# print(solution(5))