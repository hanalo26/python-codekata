# 구명보트
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42885
# 작성자: 백하은
# 작성일: 2026. 07. 23. 17:26:21

def solution(people, limit):
    # 1. 인원 수(n)
    n = len(people)
    
    # 2. 몸무게 기준으로 정렬
    people.sort()
    
    # 3. 가장 무거운 사람과 가장 가벼운 사람의 번호
    light = 0
    heavy = n-1
    
    # 4. 구명보트 개수
    boat = 0
    
    # 5. 탐색
    while light <= heavy:
        if people[light] + people[heavy] <= limit:
            light += 1
        
        # 무거운 사람은 무조건 탈출함
        heavy = heavy - 1
        boat += 1
    
    # 6. 답
    return boat