#https://school.programmers.co.kr/learn/courses/30/lessons/92334
def solution(id_list, report, k):
    
    dic = {i:set() for i in id_list}
    report_dic = {i:0 for i in id_list}

    
    for i in report:
        dic[i.split(" ")[0]].add(i.split(" ")[1])
    
    sum_report = []
    for i in dic.values():
        sum_report+=list(i)
    
    
    for i in sum_report:
        report_dic[i]+=1
    
    
    answer = []
    for key,value in report_dic.items():
        if value>=k:
            answer.append(key)
    
    
    result = []
    
    for i in dic.values():
        tmp=0
        for j in i:
            if j in answer:
                tmp+=1
        result.append(tmp)
    
    return result
        
