# 문자열 내림차순으로 배치하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12917
# 알고리즘: 문자열, 정렬
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:54:44

def solution(s):
    empty_str = ''
    answer = empty_str.join(sorted(s, reverse=True))
    return answer