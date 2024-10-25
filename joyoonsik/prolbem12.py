# https://school.programmers.co.kr/learn/courses/30/lessons/72410
def solution(new_id):
    answer=''
    new_id=new_id.lower()
    for i in range(len(new_id)):
        if 'a'<=new_id[i]<='z' or new_id[i]=='.' or '0'<=new_id[i]<='9' or new_id[i]=='_' or new_id[i]=='-':
            answer+=new_id[i]
    
    tmp = ''
    for i in range(len(answer)-1):
        if answer[i]=='.' and answer[i+1]=='.':
            continue
        tmp+=answer[i]
    tmp+=answer[-1]
    answer=tmp
    
    if answer[0]=='.':
        answer=answer[1:]
    if len(answer)==0:
        answer='a'
    if answer[-1]=='.':
        answer=answer[:-1]
    if len(answer)>=16:
        answer=answer[:15]
    if answer[-1]=='.':
        answer=answer[:-1]
    if len(answer)<=2:
        tmp=answer[-1]
        answer+=tmp*(3-len(answer))
    return answer
