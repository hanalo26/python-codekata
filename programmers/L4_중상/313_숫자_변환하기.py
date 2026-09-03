# 숫자 변환하기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/154538
# 알고리즘: BFS, DP
# 작성자: 백하은
# 작성일: 2026. 09. 03. 15:22:51

from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    # (현재 숫자, 연산 횟수) 조합으로 큐 생성
    queue = deque([(x, 0)])
    visited = {x}
    
    while queue:
        curr, count = queue.popleft()
        
        # 할 수 있는 연산 3가지 수행 결과와의 비교
        for next_val in (curr + n, curr * 2, curr * 3):
            if next_val == y:
                return count + 1
            
            # y보다 작고 아직 방문하지 않은 수만 큐에 추가
            if next_val < y and next_val not in visited:
                visited.add(next_val)
                queue.append((next_val, count + 1))
                
    return -1