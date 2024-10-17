# 과제 진행하기
# https://school.programmers.co.kr/learn/courses/30/lessons/176962

def solution(plans):
    answer = []
    for i in range(len(plans)):
        plans[i][1] = int(plans[i][1][:2] ) * 60 + int(plans[i][1][-2:])
        plans[i][2] = plans[i][1] + int(plans[i][2])
        
    schedule = sorted(plans, key=lambda x:x[1])
    notDone = []
    
    while schedule:
        if len(schedule) == 1:
            answer.append(schedule[0][0])
            schedule.pop()
        else:
            if schedule[0][2] > schedule[1][1]:
                notDone.append([schedule[0][0], schedule[0][2] - schedule[0][1] - (schedule[1][1] - schedule[0][1])])
                schedule = schedule[1:]
            elif schedule[0][2] == schedule[1][1]:
                answer.append(schedule[0][0])
                schedule = schedule[1:]
            else:
                answer.append(schedule[0][0])
                now_time = schedule[0][2]
                schedule = schedule[1:]
                while notDone:
                    if not schedule:
                        answer.append(notDone[-1][0])
                        notDone.pop()
                    else:
                        schedule = [[notDone[-1][0], now_time, now_time + notDone[-1][1]]] + schedule
                        notDone.pop()
                        if schedule[0][2] > schedule[1][1]:
                            notDone.append([schedule[0][0], schedule[0][2] - schedule[0][1] - (schedule[1][1] - schedule[0][1])])
                            schedule = schedule[1:]
                            break
                        elif schedule[0][2] == schedule[1][1]:
                            answer.append(schedule[0][0])
                            schedule = schedule[1:]
                            break
                        else:
                            answer.append(schedule[0][0])
                            now_time = schedule[0][2]
                            schedule = schedule[1:]
    
    while notDone:
        answer.append(notDone[-1][0])               
        notDone.pop() 
    return answer

# print(solution(
#     [["science", "12:40", "50"], 
#       ["music", "12:20", "40"], 
#       ["history", "14:00", "30"], 
#       ["computer", "12:30", "100"]]
#     )
# )
