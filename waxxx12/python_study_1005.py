def solution(a, b):
    # 각 달의 일수를 리스트로 저장 (윤년이므로 2월은 29일)
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 1월 1일이 금요일이므로 'FRI'부터 시작하는 요일 리스트
    days_of_week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    # 1월 1일에서 (a월 b일까지의) 총 일수를 계산
    total_days = sum(days_in_month[:a-1]) + (b - 1)

    # 총 일수를 7로 나눈 나머지를 이용해 요일을 계산
    answer = days_of_week[total_days % 7]

    return answer
print(solution(5, 24))
