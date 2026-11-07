# 시소 짝꿍
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/152996
# 알고리즘: 해시, 수학
# 작성자: 백하은
# 작성일: 2026. 11. 07. 15:22:16

"""
(1) weights : 사람들의 몸무게 목록

(2) '시소 짝꿍'이란?
    - 탑승한 사람의 무게와 시소 축과 좌석 간의 거리의 곱이 양쪽 다 같은 경우
    - 시소 축과 좌석 간의 거리는 '2m, 3m, 4m' 중 하나이므로 거리비는 
    '1:1, 2:3, 1:2, 3:4'로 존재
    
(3) 몸무게가 w일때, 시소 짝꿍이 될 수 있는 상대방의 몸무게는 'w, (3/2)w, 2w, (4/3)w'이고, 각 값이 정수가 되는 경우에만 유효한 후보가 됨

(4) 같은 몸무게를 가진 사람들끼리의 조합은 조합 공식을 사용해 한 번에 계산하고, 서로 다른 몸무게를 가진 사람들끼리는 {(몸무게 1)인 사람들의 수 * (몸무게 2)인 사람들의 인원수}로 경우의 수를 구할 예정 

"""
from collections import Counter

def solution(weights):
    answer = 0
    
    # 몸무게별 인원수를 딕셔너리(Counter)에 기록
    weight_c = Counter(weights)
    
    # 고유한 몸무게 목록 순회
    for w in weight_c:
        # 같은 몸무게인 사람들끼리 짝꿍이 되는 경우
        n = weight_c[w]
        
        if n > 1:
            answer += n * (n-1) // 2
        
        # 서로 다른 몸무게와 비율(2:3, 2:4, 3:4)을 이루는 경우
        # 거리비가 2:3 일때
        if (w * 3) % 2 == 0:
            t1 = (w * 3) // 2
            if (t1 in weight_c) and t1 > w: 
                # t1 > w 조건으로 중복 계산 방지
                answer += weight_c[w] * weight_c[t1]
        
        # 거리비가 1:2 일때
        t2 = w * 2
        if (t2 in weight_c) and t2 > w:
            answer += weight_c[w] * weight_c[t2]
        
        # 거리비가 3:4 일때
        if (w * 4) % 3 == 0:
            t3 = (w * 4) // 3
            if (t3 in weight_c) and t3 > w: 
                answer += weight_c[w] * weight_c[t3]
        
    return answer