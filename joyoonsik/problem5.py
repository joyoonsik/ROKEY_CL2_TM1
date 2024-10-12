# 문제링크 : https://school.programmers.co.kr/learn/courses/30/lessons/92334
# 해결법 : 문자열로품 리스트 순회안하고 이게 확실히 리스트 순회가 몇십만 몇백만이 되면 참 비효율적이기때문에
# for문을 이용해서 순회하지않고 한번에 문자열로 변환시켯다가 딱딱 필요할때만 순환
# 근데 그것보다 리스트마다 split하는거에서 오래걸림 그래서 어떻게 보면 리스트->문자열->쪼개기->리스트로 푼거임
def solution(id_list, report, k):
    answer = []
    dic = {i:0 for i in id_list}
    dic2 = {i:0 for i in id_list}
    dic3 = {i:0 for i in id_list}
    report = set(report)
    report = list(report)
    
    hi = []
    for i in report:
        dic[i.split(' ')[1]]+=1
        
    
    for key,value in dic.items():
        if int(value)>=k:
            answer.append(key)
    
    if not answer:
        return [0,0]
    
    hi = ' '.join(report)
    hi = hi.split(' ')
    
    idx_result = []
    for i in range(1,len(hi),2):
        for j in answer:
            if hi[i]==j:
                dic3[hi[i-1]]+=1
    
    result = []
    for k,v in dic3.items():
        result.append(v)
        
    return result
