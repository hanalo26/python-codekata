# OX퀴즈
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120907
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 05. 29. 21:18:06

def solution(quiz):
    answer = []
    # 쉼표를 기준으로 quiz 내 요소들을 각각 q에 저장
    for q in quiz:
        # 공백을 기준으로 문자열 분리: ["X", "연산자", "Y", "=", "Z"]
        parts = q.split()
        x, op, y, eq, z = int(parts[0]), parts[1], int(parts[2]), parts[3], int(parts[4])
        
        # 연산자에 따른 결과 계산
        if op == '+':
            result = x + y
        else:
            result = x - y
            
        # 결과 비교 후 정답 처리
        if result == z:
            answer.append("O")
        else:
            answer.append("X")
    return answer