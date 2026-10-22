# 무인도 여행
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/154540
# 알고리즘: DFS/BFS
# 작성자: 백하은
# 작성일: 2026. 10. 22. 16:14:03

"""
# 조건 정리
1. 표현
(1) 'X': 바다
(2) 1부터 9 사이의 숫자: 무인도의 식량(머물 수 있는 일수)

2. 무인도 연결 조건
(1) 상, 하, 좌, 우로 붙어 있는 땅들은 하나의 무인도로 합체
(2) 연결된 칸에 적힌 숫자를 모두 더한 값 = 그 섬에서 머물 수 있는 총 일수

3. 반환해야 하는 값
(1) 각 섬에서 머물 수 있는 일수를 모두 구해 오름차순으로 정렬하여 배열로 반환
(2) 만약 머물 수 있는 무인도가 단 하나도 없다면 [-1]을 반환
"""
from collections import deque

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    
    # 방문했던 곳을 또 방문하지 않기 위해 체크할 2차원 리스트(방문 지도)를 만듦
    visited = [[False] * cols for _ in range(rows)]
    
    answer = []
    
    # 상, 하, 좌, 우로 이동하기 위한 방향키
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    # 탐색 시작
    for r in range(rows):
        for c in range(cols):
            # 만약 바다('X')가 아니고 아직 방문하지 않은 땅이라면 새로운 섬 탐색 시작!
            if maps[r][c] != 'X' and not visited[r][c]:
                island_sum = 0
                q = deque([(r,c)])
                visited[r][c] = True
                
                # 너비 우선 탐색(BFS)을 통해 연결된 모든 땅을 탐색
                while q:
                    curr_r, curr_c = q.popleft()
                    # 현재 땅에 적힌 숫자를 섬의 총 일수에 더함
                    island_sum += int(maps[curr_r][curr_c])
                    
                    # 상, 하, 좌, 우 네 방향을 모두 탐색
                    for i in range(4):
                        next_r = curr_r + dr[i]
                        next_c = curr_c + dc[i]
                        
                        # 지도를 벗어나지 않고, 바다가 아니며, 아직 방문하지 않은 땅이라면 q에 추가
                        if (0 <= next_r < rows and 0 <= next_c < cols and maps[next_r][next_c] != 'X' and not visited[next_r][next_c]):
                            visited[next_r][next_c] = True
                            q.append((next_r,next_c))
                            
                # 한 섬의 탐색이 끝나면 그 섬의 총 일수를 결과 리스트에 추가
                answer.append(island_sum)
                
    # 만약 갈 수 있는 섬이 하나도 없다면 -1을 담아 반환하고, 있다면 오름차순으로 정렬해서 반환
    if not answer:
        return [-1]
                
    answer.sort()
    return answer