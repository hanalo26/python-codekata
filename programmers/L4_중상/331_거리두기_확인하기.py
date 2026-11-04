# 거리두기 확인하기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/81302
# 알고리즘: BFS, 시뮬레이션
# 작성자: 백하은
# 작성일: 2026. 11. 04. 16:15:01

"""
* 맨해튼 거리 구하는 공식 = (r1-r2)의 절댓값 + (c1-c2)의 절댓값
** P: 응시자
** O: 빈 테이블
** X: 파티션
*** 각 대기실별로 거리두기를 지켰다면 1, 한 명이라도 어겼다면 0을 반환
"""
from collections import deque

# 보조
def check(place):
    # 1. 대기실 전체를 돌며 모든 응시자('P')의 위치 찾기
    persons = []
    for r in range(5): # 모든 대기실의 크기 = 5 x 5
        for c in range(5):
            if place[r][c] == 'P':
                persons.append((r,c))
    
    # 2. 각 응시자마다 다른 응시자와의 거리를 계산
    for r1, c1 in persons:
        for r2, c2 in persons:
            # 동일인을 비교하는 경우는 무시
            if (r1,c1) == (r2,c2):
                continue
                
            # 맨해튼 거리 계산 및 안전거리 수칙 준수 여부 확인
            dist = abs(r1 - r2) + abs(c1 - c2)
            
            if dist > 2:
                continue
            
            elif dist < 2:
                return 0 # 안전수칙 위반
            
            elif dist == 2:
                # 같은 행에 있을 때
                if r1 == r2:
                    mid_c = (c1+c2)//2
                    if place[r1][mid_c] != 'X':
                        return 0
                
                # 같은 열에 있을 때
                elif c1 == c2:
                    mid_r = (r1+r2)//2
                    if place[mid_r][c1] != 'X':
                        return 0
                
                # 대각선 방향으로 떨어져 있는 경우   
                else:
                    # 사이에 존재하는 두 칸이 모두 파티션으로 가려져 있어야 함
                    if place[r1][c2] != 'X' or place[r2][c1] != 'X':
                        return 0
                    
    return 1
            

# 메인
def solution(places):
    answer = []
    
    for place in places:
        answer.append(check(place))
    
    return answer