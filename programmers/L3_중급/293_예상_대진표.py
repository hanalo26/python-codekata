# 예상 대진표
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12985
# 알고리즘: 시뮬레이션
# 작성자: 백하은
# 작성일: 2026. 08. 04. 14:10:07

def solution(n,a,b):
    answer = 0

    # +1을 해서 a,b가 몇 번째 경기를 치르게 되는지 표현
    while a != b:
        # 라운드 번호 부여
        a = (a+1)//2
        b = (b+1)//2
        
        answer += 1 # 각자가 겪은 라운드 수 +1

    return answer