# 저주의 숫자 3
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120871
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 05. 21. 20:54:03

def solution(n):
    answer = 0
    
    # 1 ~ n까지의 숫자에 3x 마을만의 숫자를 순서대로 매칭 <- 마을의 숫자 매칭이 꽤 복잡해서 1부터 계산함
    for _ in range(n):
        answer += 1
        
        # answer가 3의 배수이거나 '3'을 포함하고 있다면 +1
        while (answer % 3 == 0) or ('3' in str(answer)):
            answer += 1
    
    return answer