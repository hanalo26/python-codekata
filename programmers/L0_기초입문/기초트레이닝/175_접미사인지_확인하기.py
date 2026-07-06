# 접미사인지 확인하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181908
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 06. 15:02:50

def solution(my_string, is_suffix):
    # .endswith(): 특정 문자열로 끝나는지 확인해 주는 내장 메서드
    if my_string.endswith(is_suffix):
        return 1
    else:
        return 0