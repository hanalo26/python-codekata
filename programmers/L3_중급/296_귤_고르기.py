# 귤 고르기
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/138476
# 알고리즘: 해시, 그리디
# 작성자: 백하은
# 작성일: 2026. 08. 05. 12:54:30

from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    # 가장 큰 귤부터 상자에 담으면서 가장 큰 귤을 다 담으면 k개에서 차감하고, 그 다음으로 크 귤을 채워넣는 방식으로 진행
    counts = Counter(tangerine) # {귤의 크기:개수}
    
    sorted_counts = sorted(counts.values(),reverse=True)
    
    for c in sorted_counts:
        k = k - c
        answer += 1 # 상자에 담긴 귤의 종류
        
        if k <= 0: # c가 k보다 크거나 같으면 반복문 종료 후, 결과 반환
            break
    
    return answer