# 문자열 정렬하기 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120911
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 02. 09. 14:02:20

def solution(my_string):
    my_string = my_string.lower()
    sorted_str = sorted(my_string)
    answer = "".join(sorted_str)
    return answer