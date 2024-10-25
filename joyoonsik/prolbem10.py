# https://school.programmers.co.kr/learn/courses/30/lessons/178871
def solution(players, callings):
    player_idx = {player: idx for idx, player in enumerate(players)}
    print(player_idx)
    answer = players.copy()

    for call in callings:
        idx = player_idx[call]
        
        answer[idx], answer[idx-1] = answer[idx-1], answer[idx]
        
        player_idx[answer[idx]] = idx
        player_idx[answer[idx-1]] = idx - 1

    return answer

