# 문자열 나누기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/140108
# 알고리즘: 문자열, 시뮬레이션
# 작성자: 백하은
# 작성일: 2026. 07. 20. 16:46:22

def solution(s):
    answer = 0
    
    # 기준이 되는 글자
    target_char = ""
    
    # 기준이 되는 글자와 같은 것, 다른 것의 등장한 빈도
    same_cnt = 0
    diff_cnt = 0
    
    for char in s:
        if target_char == "":
            target_char = char
            same_cnt = 1
            continue
        
        if target_char == char:
            same_cnt += 1
        else:
            diff_cnt += 1
            
        if same_cnt == diff_cnt:
            answer += 1
            # 초기화
            target_char = ""
            same_cnt = 0
            diff_cnt = 0
            
    if target_char != "":
        answer += 1
    
    return answer