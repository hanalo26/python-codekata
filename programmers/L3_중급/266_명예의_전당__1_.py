# 명예의 전당 (1)
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/138477
# 알고리즘: 정렬, 힙
# 작성자: 백하은
# 작성일: 2026. 07. 22. 14:55:51

def solution(k, score):
    # 매일 명예의 전당 내 최소 점수 기록
    answer = []
    
    # 명예의 전당 내 점수
    hold = []
    
    for s in score:
        hold.append(s)
        # 내림차순 정렬
        hold.sort(reverse=True)
        
        if len(hold) > k:
            hold = hold[:k]
            
        answer.append(hold[-1])
    
    return answer