# 모의고사
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42840
# 알고리즘: 완전탐색
# 작성자: 백하은
# 작성일: 2026. 07. 22. 15:27:14

def solution(answers):
    # 각 수포자가 객관식을 찍는 패턴
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 각 수포자가 객관식을 맞힌 개수
    # [p1, p2, p3] 순서대로 배치
    scores = [0, 0, 0]
    
    # 정답지와 비교
    # i : 문제 번호
    # a : 각 문항별 정답
    for i, a in enumerate(answers):
        # 나머지 연산자로 서로 다른 길이의 패턴이라도 순환하면서 비교
        if a == p1[i % len(p1)]:
            scores[0] += 1
            
        if a == p2[i % len(p2)]:
            scores[1] += 1
            
        if a == p3[i % len(p3)]:
            scores[2] += 1
    
    # 최고점 확인
    max_score = max(scores)
    
    # 최고점을 받은 수포자 확인
    result = []
    for idx, score in enumerate(scores):
        if score == max_score:
            result.append(idx+1)
            
    return result