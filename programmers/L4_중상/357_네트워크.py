# 네트워크
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43162
# 알고리즘: DFS/BFS
# 작성자: 백하은
# 작성일: 2026. 07. 22. 18:42:24

from collections import deque

def solution(n, computers):
    # 컴퓨터 확인 여부 (coms)
    coms = [False] * n
    
    # 연결된 네트워크 개수 (answer)
    answer = 0
    
    # 컴퓨터 번호별로 연결된 네트워크 확인
    for i in range(n):
        # 동일한 컴퓨터끼리 확인하는 것도 네트워크 하나로 check
        # 확인하지 않은 컴퓨터 발견!
        if not coms[i]:
            answer += 1
            # que에 컴퓨터 번호 저장
            que = deque([i])
            coms[i] = True # 확인한 컴퓨터라는 의미
        
            # i번째 컴퓨터와 다른 컴퓨터의 연결 확인
            while que:
                com = que.popleft()
                
                # 다른 컴퓨터와의 연결 확인
                for other_com in range(n):
                    # i번째 컴퓨터와 연결된 컴퓨터이지만, 아직 확인하지 않은 경우 (즉, i번째 컴퓨터가 아닌 경우)
                    if computers[com][other_com] == 1 and (not coms[other_com]):
                        coms[other_com] = True # 같은 네트워크로 연결되었음을 확인
                        que.append(other_com) # 그 컴퓨터와 연결된 또 다른 컴퓨터를 찾기 위해 추가
    return answer
    