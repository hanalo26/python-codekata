# 개미 군단
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120837
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 01. 29. 09:32:41

def solution(hp):
    # 출전한 장군개미의 수
    general_ant = hp // 5
    hp = hp % 5
    
    # 출전한 병정개미의 수
    soldier_ant = hp // 3
    hp = hp % 3
    
    # 출전한 일개미의 수
    worker_ant = hp // 1
    
    return general_ant + soldier_ant + worker_ant