# 5명씩
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181886
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 07. 03. 15:37:10

def solution(names):
    
    # 리스트_슬라이싱 문법: 리스트명[시작:끝:증감폭(Step)] 
    answer = names[::5]
    return answer