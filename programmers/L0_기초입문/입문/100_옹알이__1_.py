# 옹알이 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120956
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 04. 29. 16:43:32

def solution(babbling):
    answer = 0
    can_speak = ["aya", "ye", "woo", "ma"]
    
    for bab in babbling:
        for word in can_speak:
            bab = bab.replace(word, " ")
        
        # 모든 단어를 훑은 뒤, 공백을 제거(.strip())했을 때
        # 아무것도 남지 않아야 조카가 완벽하게 발음한 것
        if bab.strip() == "":
            answer += 1
    
    return answer