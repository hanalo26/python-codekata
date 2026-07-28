# 옹알이 (2)
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/133499
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 28. 19:49:04

def solution(babbling):
    answer = 0
    # 조카가 발음할 수 있는 발음
    can_speak = ["aya", "ye", "woo", "ma"]
    
    # 조카가 발음할 때, 발음 가능한 단어의 규칙
    """
    - 주어진 4가지 발음과 4가지 발음을 조합한 단어는 발음 가능
    - 단, 같은 발음을 연달아서 하는 단어는 발음 불가능
    babbling: 조카 발음할 수 있는지 없는지 테스트할 단어 목록
    """
      
    for word in babbling:
        # 연속된 발음 여부 
        has_repeat = False
        # 같은 발음이 연달아 존재하는가?
        for speak in can_speak:
            if speak * 2 in word:
                has_repeat = True
                break # 검사 종료 -> 발음이 불가능하므로
        if has_repeat:
            continue # 해당 단어는 조카가 발음할 수 없으므로 pass
            
        # 발음 가능한 단어라면?
        for speak in can_speak:
            word = word.replace(speak, " ") # 떨어져 있던 알파벳들이 붙으면서 생기는 단어가 발음 가능한 경우를 방지
            
        # 모든 단어에 대해 공백을 제거했을 때, 빈 문자열이 되면 조카가 발음할 수 있는 단어로 판단 가능
        if word.strip() == "":
            answer += 1

    return answer