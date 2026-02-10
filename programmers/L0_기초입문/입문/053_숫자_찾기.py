# 숫자 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120904
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 02. 10. 09:42:30

def solution(num, k):
    str_num = str(num)
    str_k = str(k)
    
    index = str_num.find(str_k)
    if index >= 0:
        return index + 1
    else:
        return index