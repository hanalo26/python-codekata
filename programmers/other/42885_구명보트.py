# 구명보트
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42885
# 작성자: 백하은
# 작성일: 2026. 07. 23. 15:17:11

# 구해야 하는 것: 모든 사람을 구출하기 위해 필요한 최소한의 구명보트 수

# 가장 무거운 사람은 가장 가벼운 사람과 함께 탈 수 없더라도 무조건 해당 순서에 혼자서라도 떠난다!

def solution(people, limit):
    
    # 1. 몸무게가 가벼운 순서대로 배치
    people.sort()
    
    # 2. 남은 사람 중에 가장 가벼운 사람의 번호(left)와 가장 무거운 사람의 번호(right)라 한다.
    left = 0
    right = len(people) - 1
    
    # 3. 사용한 구명보트의 개수
    cnt = 0
    
    # 4. 가장 가벼운 사람 = 가장 무거운 사람, 즉 혼자 남을 때까지 반복
    while left <= right:
    
        # 5. 가장 가벼운 사람과 가장 무거운 사람이 함께 떠날 수 있는지 확인
        if people[left] + people[right] <= limit:
            
            left += 1
        
        # 6. 가장 무거운 사람 혼자 떠나야 하는 경우(같이 타더라도 보트 수는 무조건 +1)
        right = right - 1
        cnt += 1
        
    # 7. 최종 답
    return cnt