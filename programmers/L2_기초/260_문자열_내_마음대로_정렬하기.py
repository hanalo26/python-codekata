# 문자열 내 마음대로 정렬하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12915
# 알고리즘: 정렬
# 작성자: 백하은
# 작성일: 2026. 07. 15. 12:59:28

def solution(strings, n):
    # x[n]을 기준으로 -> x(문자열 자체 사전순)를 기준으로 정렬
    strings.sort(key=lambda x: (x[n], x))
    
    return strings