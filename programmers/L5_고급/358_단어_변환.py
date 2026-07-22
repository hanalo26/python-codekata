# 단어 변환
# 프로그래머스 L5 (고급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 알고리즘: DFS/BFS
# 작성자: 백하은
# 작성일: 2026. 07. 22. 20:11:54

from collections import deque

def solution(begin, target, words):
    # 1. target 단어가 words에 포함되어 있는지 확인
    if target not in words:
        return 0
    
    # 2. words에 있는 각 단어를 이미 사용했는지 확인하는 리스트 정의
    n = len(words)
    visited = [False] * n
    
    # 3. (현재 단어, 변환 횟수) 조합으로 초기 que 정의
    que = deque([(begin, 0)])
    
    # 4. 탐색 시작
    while que:
        current_word, cnt = que.popleft()
    
        # 5. 현재 단어 == target 단어인 경우
        if current_word == target:
            return cnt
        
        # 6. 현재 단어 != target 단어인 경우
        # 7. words에 남은 단어 탐색
        for i in range(n):
            next_word = words[i]
            # 8. 현재 단어와 새로운 단어간의 다른 알파벳 개수 카운트
            # (단, 앞서 사용한 단어가 아니어야 함)
            if not visited[i]:
                # 8-1. 두 단어 간의 서로 다른 알파벳 개수(diff)
                    diff = 0
                    for a1, a2 in zip(current_word,next_word):
                        if a1 != a2:
                            diff += 1
                    # 8-2. diff == 1인 경우엔 그 단어로 이동 
                    if diff == 1:
                        visited[i] = True
                        que.append((next_word, cnt+1))
                        
                    
    # 9. 모든 단어를 훑었음에도 실패한 경우
    return 0