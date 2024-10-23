# 행렬의 곱셈
# https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    answer = []
    len_arr = len(arr2)
    for i in range(len(arr1)):
        arr_temp = []
        for k in range(len(arr2[0])):
            temp = 0
            for j in range(len(arr1[i])):
                temp += arr1[i][j] * arr2[j][k]
            arr_temp.append(temp)
        answer.append(arr_temp)
    return answer

# print(solution([[1, 4], [3, 2], [4, 1]],
#                [[3, 3], [3, 3]]))

# print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],
#                [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))