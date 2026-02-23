# 합성수 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120846
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 02. 23. 09:50:19

def solution(n):
    answer = 0
    
    # 1 ~ n까지의 모든 수 확인
    for num_1 in range(1, n+1):
        cnt_of_divisor = 0
        # 약수의 개수 확인
        for num_2 in range(1, num_1+1):
            if num_1 % num_2 == 0:
                cnt_of_divisor += 1
        # 약수의 개수 >= 3        
        if cnt_of_divisor >= 3:
            answer += 1

    return answer

