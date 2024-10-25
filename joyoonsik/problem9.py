# https://school.programmers.co.kr/learn/courses/30/lessons/150370
def day(day):
    day = int(day.split(".")[0])*12*30 + int(day.split(".")[1])*30 + int(day.split(".")[2])
    return day
def solution(today, terms, privacies):
    dic = {i.split(" ")[0]:int(i.split(" ")[1])*30 for i in terms}
    today = day(today)
    answer = []
    for idx,i in enumerate(privacies):
        if today-day(i.split(" ")[0])>=dic[i.split(" ")[1]]:
            answer.append(idx+1)
    return answer
