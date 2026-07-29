# 대충 만든 자판
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/160586
# 알고리즘: 해시
# 작성자: 백하은
# 작성일: 2026. 07. 29. 18:50:11

def solution(keymap, targets):
    answer = []
    
    # 어떤 알파벳을 입력할 떄, 주어진 key 중에서 같은 알파벳을 인쇄하기 위해 클릭해야 하는 횟수를 딕셔너리로 정의
    key_press = {}
    
    for k in keymap:
        for idx, txt in enumerate(k):
            press_cnt = idx+1
            # 입력 가능한 알파벳에 아직 저장되지 않은 경우
            if txt not in key_press:
                key_press[txt] = press_cnt
            # 입력 가능한 알파벳에 저장되어 있는 경우
            else:
                key_press[txt] = min(press_cnt,key_press[txt])
                
    
    for t in targets:
        total_press = 0
        is_possible = True # 만들 수 있는 단어인가?
        
        for c in t:
            if c in key_press:
                total_press += key_press[c]
            else:
                is_possible = False
                break
                
                
        if is_possible:
            answer.append(total_press)
        else:
            answer.append(-1)
            
    return answer