# 가운데 글자 가져오기
# 프로그래머스 L1 (입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12903
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:52:18

def solution(s):
    length_of_s = len(s)
    mid_index = length_of_s // 2
    if length_of_s % 2 == 0:
        return s[mid_index-1:mid_index+1]
    else:
        return s[mid_index]