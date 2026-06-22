# 주사위 게임 2
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181930
# 알고리즘: 조건문
# 작성자: 백하은
# 작성일: 2026. 06. 23. 00:22:23

def solution(a, b, c):
    # 세 숫자가 모두 같은 경우
    if a == b and b == c:
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    
    # 세 숫자가 모두 다른 경우
    elif a != b and b != c and a != c:
        return a+b+c
    
    # 그 외 (-> 세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다른 경우)
    else:
        return (a + b + c) * (a**2 + b**2 + c**2)