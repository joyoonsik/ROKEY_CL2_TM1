# 신규 아이디 추천
# https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''
    
    # 1
    id = new_id.lower()
    
    # 2
    for s in id:
        if s.isalnum() or s == '-' or s == '_' or s == '.':
            answer += s
        
    # 3
    temp = answer[0]
    for i in range(1, len(answer)):
        if answer[i] == '.' and answer[i - 1] == answer[i]:
            continue
        else:
            temp += answer[i]
    answer = temp
    
    # 4
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    
    # 5
    if answer == '':
        answer = 'a'
        
    # 6
    elif len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]
    
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer

# print(solution("...!@BaT#*..y.abcdefghijklm"))