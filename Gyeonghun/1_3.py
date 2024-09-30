# 주식가격
# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    length = len(prices)
    
    for i in range(length):
        term = 0
        
        for j in range(i + 1, length):
            term += 1
            if prices[i] > prices[j]:
                break
    
        answer.append(term)

    return answer
            

# print(solution(
#     [1, 2, 3, 2, 3]
# ))