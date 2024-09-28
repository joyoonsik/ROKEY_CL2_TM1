# 호텔 대실
# https://school.programmers.co.kr/learn/courses/30/lessons/155651

def solution(book_time):
    time_in_minutes = []
    max_room = 0
    for start, end in book_time:
        start_hour, start_minute = map(int, start.split(":"))
        end_hour, end_minute = map(int, end.split(":"))
        start_in_minute = start_hour * 60 + start_minute
        end_in_minute = end_hour * 60 + end_minute + 10
        time_in_minutes.append((start_in_minute, end_in_minute))
    
    time_in_minutes.sort(key=lambda x: x[0])
    cur_rooms = []
    
    for start, end in time_in_minutes:
        rooms = 0
        cur_rooms.append((end))
        for reserved_end in cur_rooms:
            if start < reserved_end:
                rooms += 1
        
        if rooms > max_room:
            max_room = rooms       
        
        
    return max_room


# print(solution([
#     ["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]
#     ]))