# 단어 변환
# 프로그래머스 L5 (고급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 알고리즘: DFS/BFS
# 작성자: 백하은
# 작성일: 2026. 07. 24. 15:27:57

from collections import deque

def solution(begin, target, words):
    # 1. target not in words -> return 0
    if target not in words:
        return 0
    
    # 2. 이미 사용한 단어는 사용 불가 -> 사용하면 False를 True로 변경
    n = len(words)
    visit = [False] * n
    
    # 3. (현재 단어, 변환 횟수)를 담은 큐 생성
    q = deque([(begin,0)])
    
    # 4. 탐색
    # 현재단어와 사용하지 않은 word 내 단어의 알파벳을 비교해서 diff가 1인 단어로 변경하고 다시 큐에 저장
    while q:
        current_word, cnt = q.popleft()
        
        if current_word == target:
            return cnt
        
        else:
            for i in range(n):
                next_word = words[i]
                
                if not visit[i]:
                    diff = 0
                    for a1, a2 in zip(current_word,next_word):
                        if a1 != a2:
                            diff += 1
                    if diff == 1:
                        visit[i] = True
                        q.append((next_word,cnt+1))
                        
    return 0