# 끝말 잇기
# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    turn = 1
    answer = [words[0]]

    for i in range(1, len(words)):
        if words[i] in answer:
            return [i % n + 1, turn]
        
        if words[i-1][-1] != words[i][0]:
            return [i % n + 1, turn]
        
        
        answer.append(words[i])
        print(answer)
        
        if (i + 1) % n == 0:
            turn += 1
        
    return [0, 0]


# print(solution(5, 
#                ["hello", "observe", "effect", "take",
#                 "either", "recognize", "encourage", "ensure",
#                 "establish", "hang", "gather", "refer",
#                 "reference", "estimate", "executive"]
#                ))