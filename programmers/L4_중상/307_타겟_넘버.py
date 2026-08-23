# 타겟 넘버
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 알고리즘: DFS, 완전탐색
# 작성자: 백하은
# 작성일: 2026. 08. 24. 00:11:12

from collections import deque

def solution(numbers, target):
    # 타겟 넘버를 만드는 방법의 수
    answer = 0
    
    # (누적합, 사용한 숫자의 개수) 조합으로 만든 큐 생성
    q = deque([(0,0)])
    
    while q:
        total_sum, used_num_cnt = q.popleft()
        
        if used_num_cnt == len(numbers):
            if total_sum == target:
                answer += 1
                
        else:
            q.append((total_sum+numbers[used_num_cnt], used_num_cnt+1))
            q.append((total_sum-numbers[used_num_cnt], used_num_cnt+1))
    
    return answer