# 귤 고르기
# https://school.programmers.co.kr/learn/courses/30/lessons/138476

def solution(k, tangerine):
    size_count = {}
    
    for num in tangerine:
        if num in size_count:
            size_count[num] += 1
        else:
            size_count[num] = 1
    
    sorted_counts = sorted(size_count.values(), reverse=True)
    
    total = 0
    unique_count = 0
    
    for count in sorted_counts:
        total += count
        unique_count += 1
        
        if total >= k:
            break
    
    return unique_count
        


print(solution(
   6, [1, 3, 2, 5, 4, 5, 2, 3]
))