# 과일 장수
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/135808
# 알고리즘: 정렬, 그리디
# 작성자: 백하은
# 작성일: 2026. 07. 18. 14:25:38

def solution(k, m, score):
    answer = 0
    
    # 내림차순 정렬
    score.sort(reverse=True)
    
    # m-1번 인덱스부터 시작해서 m개 간격(step)으로 뛰어넘으며 순회
    # 해당 자리에 있는 사과들이 각 상자의 '가장 점수가 낮은 사과'가됨
    for i in range(m-1, len(score), m):
        # 최저 점수 * 상자당 사과 개수(m)
        answer += score[i]*m
    
    return answer