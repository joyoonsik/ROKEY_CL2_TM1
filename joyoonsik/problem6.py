#문제링크 : https://school.programmers.co.kr/learn/courses/30/lessons/150370
def solution(today, terms, privacies):
    answer = []
    # 22.1.5 -> 12개월 -> 23.1.5에파기
    dic={i.split(' ')[0]:int(i.split(' ')[1]) for i in terms}
    print(dic)
    
    today_sum=int(today.split('.')[0])*12*29+int(today.split('.')[1])*29+int(today.split('.')[2])
    
    
    for idx,i in enumerate(privacies):
        tmp = int(i.split(' ')[0].split('.')[0])*12*29+int(i.split(' ')[0].split('.')[1])*29+int(i.split(' ')[0].split('.')[2])+dic[i.split(' ')[1]]*29
        
        if tmp<=today_sum:
            answer.append(idx+1)
    
    return answer
