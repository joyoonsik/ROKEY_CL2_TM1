#문제링크:https://school.programmers.co.kr/learn/courses/30/lessons/67256
#같은번호 분기처리.. if elif 문을 생각하고 써야겠다는것을 배움
#인덱스로 처리
def check(i,left_finger, right_finger, hand):
    arr=[[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    for j,v1 in enumerate(arr):
        for k,v2 in enumerate(v1):
            if i==v2:
                tmp1=(j,k)
            if left_finger==v2:
                tmp2=(j,k)
            if right_finger==v2:
                tmp3=(j,k)
                
    if abs(tmp1[0]-tmp2[0])+abs(tmp1[1]-tmp2[1]) < abs(tmp1[0]-tmp3[0])+abs(tmp1[1]-tmp3[1]):
        answer='L'
    elif abs(tmp1[0]-tmp2[0])+abs(tmp1[1]-tmp2[1]) > abs(tmp1[0]-tmp3[0])+abs(tmp1[1]-tmp3[1]):
        answer='R'
    else:
        answer=hand[0].upper()
    return answer
    
def solution(numbers, hand):
    answer = ''
    left_finger = '*'
    right_finger = '#'
    for i in numbers:
        if i==1 or i==4 or i==7:
            left_finger = i
            answer+='L'
        elif i==3 or i==6 or i==9:
            right_finger = i
            answer+='R'
        else:
            tmp = check(i,left_finger, right_finger, hand)
            answer+=tmp
            if tmp=='L':
                left_finger = i
            else:
                right_finger = i     
    return answer
