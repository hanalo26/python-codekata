# 문자열 밀기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120921
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 05. 22. 13:41:07

def solution(A, B):
    # A, B가 처음부터 같을 때
    if A == B:
        return 0
    
    # 문자열 밀기 시작
    for cnt in range(1, len(A)):
        # 오른쪽으로 하나씩 밀고, 마지막 글자는 처음으로
        A = A[-1] + A[:-1]
        
        if A == B:
            return cnt
    
    # A의 길이만큼 밀어도 같아지지 않는 경우
    return -1