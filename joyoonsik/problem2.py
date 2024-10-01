#문제 링크:https://school.programmers.co.kr/learn/courses/30/lessons/340213
#정답률:33%, 문제특징:단순 요구사항 구현

# 1. pos가 오프닝 시작과 끝 사이이면 자동으로 오프닝 끝으로 리턴
# 2. next:10초후, prev:10초전
# 3. pos가 오프닝 시작과 끝 사이이면 자동으로 오프닝 끝으로 리턴

# 해결포인트
# 일단 전부 초단위로 변환해서 쉽게 계산
# zfill 함수를 통해 0 채워주기

# 실수 주의 : pos를 계속해서 업데이트 해줘야함. next 혹은 prev 할때마다 posCheck함수를 통해 업데이트 

def minuteToSecond(tmp):
    return int(tmp.split(":")[0])*60+int(tmp.split(":")[1])

def posCheck(pos, op_start, op_end, video_len):
    if (op_start<=pos) & (pos<=op_end):
        pos=op_end
    elif pos+10>video_len:
        pos=video_len
    return pos

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len = minuteToSecond(video_len)
    pos = minuteToSecond(pos)
    op_start = minuteToSecond(op_start)
    op_end = minuteToSecond(op_end)
    
    pos = posCheck(pos, op_start, op_end, video_len)
    for i in commands:
        if i=="next":
            pos+=10
        elif i=="prev":
            pos-=10
            if pos<0:
                pos=0
        pos = posCheck(pos, op_start, op_end, video_len)
    
    answer = str(pos//60).zfill(2)+":"+str(pos-60*(pos//60)).zfill(2)
    
    return answer
