# 점 찍기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/140107
# 알고리즘: 수학
# 작성자: 백하은
# 작성일: 2026. 10. 29. 14:03:11

"""
[문제 풀이 조건]
1. x축과 y축 방향으로 모두 0, k, 2k, 3k, ... 간격으로 점을 찍는다.

2. 원점 (0,0)에서부터 점 (x,y) 까지의 거리는 d 이하여야 한다. (피타고라스의 정리에 의해 x^2 + y^2 <= d^2)

3. 반환해야 하는 것: 두 조건을 만족하는 점의 총 개수

"""
import math

def solution(k, d):
    answer = 0
    
    # x좌표를 0부터 시작해서 k씩 증가시킴
    for x in range(0, d+1, k):
        # x^2 + y^2 <= d^2을 만족하는 y의 최댓값 구하기
        # -> d^2 - x^2의 양의 제곱근
        max_y = math.isqrt(d**2 - x**2)
        
        # y도 0부터 시작해서 k 간격으로 커지므로, 
        # 0부터 max_y 사이에 들어오는 k의 배수 개수를 구함 (단, 0을 포함해야 함)
        cnt = (max_y//k) + 1
        
        answer += cnt
    
    return answer