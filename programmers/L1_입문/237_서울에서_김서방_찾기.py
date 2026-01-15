# 서울에서 김서방 찾기
# 프로그래머스 L1 (입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12919
# 알고리즘: 배열, 탐색
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:51:00

def solution(seoul):
    
    for i, name in enumerate(seoul):
        if name == "Kim":
            return f"김서방은 {i}에 있다"