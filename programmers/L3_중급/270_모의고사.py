# 모의고사
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42840
# 알고리즘: 완전탐색
# 작성자: 백하은
# 작성일: 2026. 07. 22. 21:41:01

def solution(answers):
    # 1. 수포자 3인방의 찍기 패턴
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 2. 수포자 3인방의 정답 개수 (p1, p2, p3)
    # 채점 전에는 모두 0점 
    scores = [0,0,0]
    
    # 3. 답지와 비교
    # i : 문제 번호
    # an : 답
    for i, an in enumerate(answers):
        # p1 채점
        if an == p1[i % len(p1)]:
            scores[0] += 1
        # p2 채점
        if an == p2[i % len(p2)]:
            scores[1] += 1
        # p3 채점
        if an == p3[i % len(p3)]:
            scores[2] += 1
            
    max_score = max(scores)
    
    # 4. 최고 점수를 받은 학생 확인
    answer = []
    for p, score in enumerate(scores):
        if score == max_score:
            answer.append(p+1)     
            
    return answer