# 진료순서 정하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120835
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 03. 31. 20:44:12

def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True) # 내림차순 정렬
    
# list.index(값): 리스트에서 해당 값이 처음 등장하는 위치를 반환
    return [sorted_emergency.index(i)+1 for i in emergency]