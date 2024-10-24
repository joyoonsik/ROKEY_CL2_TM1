# 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    answer = {}
    for person in participant:
        if person not in answer:
            answer[person] = 1
        else:
            answer[person] += 1
    
    for runner in completion:
        if answer[runner] == 1:
            del answer[runner]
        else:
            answer[runner] -= 1
    
    return ', '.join(f'{name}' for name in answer.keys())


# print(solution(["mislav", "stanko", "mislav", "ana"],
#                ["stanko", "ana", "mislav"]))