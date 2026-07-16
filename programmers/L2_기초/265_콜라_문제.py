# 콜라 문제
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/132267
# 알고리즘: 시뮬레이션
# 작성자: 백하은
# 작성일: 2026. 07. 16. 12:27:38

def solution(a, b, n):
    answer = 0
    
    # 보유한 빈 병(n)이 마트에 줘야 하는 개수(a) 이상인 경우
    while n >= a:
        # q는 마트에 몇 번 교환 세트를 들이밀 수 있는지(몫)
        # remainder는 남은 병(나머지)
        q, remainder = divmod(n,a)
        
        # 새롭게 교환받은 콜라 수
        new_coke = q * b
        
        # 상빈이가 총 얻은 콜라 수 (누적)
        answer += new_coke
        
        # 내가 가진 총 빈 병 개수 (새로 마신 병 + 교환 못 하고 남은 병)
        n = new_coke + remainder
    
    return answer