# 두 수의 연산값 비교하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181938
# 알고리즘: 연산
# 작성자: 백하은
# 작성일: 2026. 06. 16. 19:50:17

def solution(a, b):
    ab = int(str(a) + str(b))
    ab2 = 2*a*b
    
    if ab >= ab2:
        return ab
    else:
        return ab2