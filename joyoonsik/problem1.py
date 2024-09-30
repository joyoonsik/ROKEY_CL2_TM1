#문제링크 : https://school.programmers.co.kr/learn/courses/30/lessons/258712
#레벨1, 정답률 25%, 문제특징:단순 요구사항 구현

#문제요약
#선물지수:준선물-받은선물
#선물지수가 더 높은사람이 선물받음
#선물지수가 같다면 선물 주고받지 않음
#다음달 가장 많이 선물받는자의 선물 수를 예측하라

#해결포인트
#1.먼저 딕셔너리의 키값을 friends값으로 할당시킨것
#2.문제에서 제시한 표를 순서대로 구현
def solution(friends, gifts):
    #준사람,받은사람
    dic = {i:{j:0 for j in friends} for i in friends}
    
    #받을선물,선물지수
    dic_gift = {i:[0,0] for i in friends}
    
    for i in gifts:
        dic[i.split(" ")[0]][i.split(" ")[1]]+=1
        dic_gift[i.split(" ")[0]][1]+=1
        dic_gift[i.split(" ")[1]][1]+=-1

    for i,v in enumerate(friends):
        for j in friends[i+1:]:
            if dic[v][j] < dic[j][v]:
                dic_gift[j][0]+=1
            elif dic[v][j] > dic[j][v]:
                dic_gift[v][0]+=1
            else:
                if dic_gift[j][1] < dic_gift[v][1]:
                    dic_gift[v][0]+=1
                elif dic_gift[j][1] > dic_gift[v][1]:
                    dic_gift[j][0]+=1     
    
    return max([i[0] for i in dic_gift.values()])
