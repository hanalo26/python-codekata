# 멀쩡한 사각형
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/62048
# 알고리즘: 수학, GCD
# 작성자: 백하은
# 작성일: 2026. 11. 06. 14:12:58

"""
(1) 구해야 하는 것: W*H 크기의 직사각형을 잘라서 생긴 두 개의 직각삼각형에 존재하는 모든 1*1 크기의 정사각형 크기의 개수

(2) W*H 크기의 직사각형을 대각선으로 자를 때, 버려지는 1*1 크기의 정사각형의 개수
    - 하나의 대각선이 반대쪽 아래 꼭짓점에 닿기 위해 이동해야 하는 방향을 x,y축의 이동으로 쓰면 x축 방향으로 W만큼 오른쪽으로 이동해야 하고, y축 방향으로 H만큼 아래쪽으로 이동해야 함
    - 이때, 이동하면서 서로 다른 정사각형의 꼭짓점만 통과하는 경우가 있는데 이렇게 지나게 되는 점의 개수 = 가로 길이와 세로 길이의 최대공약수와 같음
    -> W + H - math.gcd(W,H)와 같음
"""
import math

def solution(w,h):
    # 전체 사각형 개수
    total_squares = w * h
    
    # 대각선이 지나가는 정사각형 개수
    gcd_value = math.gcd(w,h)
    
    unusable_squares = w + h - gcd_value
    
    # 사용할 수 있는 정사각형의 개수 = 전체 사각형 개수 - 대각선이 지나가는 정사각형 개수
    answer = total_squares - unusable_squares
    
    return answer