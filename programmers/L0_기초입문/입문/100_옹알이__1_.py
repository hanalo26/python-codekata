# 옹알이 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120956
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 04. 29. 16:42:41

def solution(babbling):
    answer = 0
    can_speak = ["aya", "ye", "woo", "ma"]
    
    for bab in babbling:
        for word in can_speak:
            bab = bab.replace(word, " ")
            
        if bab.strip() == "":
            answer += 1
    
    return answer