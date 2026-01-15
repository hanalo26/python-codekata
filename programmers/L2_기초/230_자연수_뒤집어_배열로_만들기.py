# 자연수 뒤집어 배열로 만들기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12932
# 알고리즘: 문자열, 배열
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:47:27

def solution(n):
    result=[]
    n_str=str(n)
    for i in n_str[::-1]:
        result.append(int(i))
    return result