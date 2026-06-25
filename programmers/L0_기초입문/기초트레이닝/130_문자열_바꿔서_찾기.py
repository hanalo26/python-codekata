# 문자열 바꿔서 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181864
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 06. 25. 20:09:24

def solution(myString, pat):
    answer = ''
    
    # 텍스트 변환
    for txt in myString:
        if txt == 'A':
            answer += 'B'
        elif txt == 'B':
            answer += 'A'
    
    # pat이 있는지 확인
    if pat in answer:
        return 1
    else:
        return 0