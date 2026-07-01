# 원하는 문자열 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181878
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 01. 14:40:38

def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    
    if pat in myString:
        return 1
    else:
        return 0