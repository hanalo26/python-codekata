# 두 개 뽑아서 더하기
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/68644
# 알고리즘: 완전탐색
# 작성자: 백하은
# 작성일: 2026. 07. 22. 14:19:20

def solution(numbers):
    answer = set() # 집합 자료형으로 선언해 중복을 자동으로 제거
    n = len(numbers)
    
    for i in range(n):
        for j in range(i+1,n):
            answer.add(numbers[i]+numbers[j])
    
    return sorted(list(answer))