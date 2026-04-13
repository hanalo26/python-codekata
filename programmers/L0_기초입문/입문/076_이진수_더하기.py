# 이진수 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120885
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 04. 13. 21:24:34

def solution(bin1, bin2):
    # int(string, base)
    #   string: 숫자로 바꾸고 싶은 문자열
    #   base: 해당 문자열이 몇 진수인지 작성
    answer = int(bin1, 2) + int(bin2, 2)
    
    # bin(): 이진수임을 나타내기 위해 결과 앞에 항상 **0b**라는 접두사를 붙임
    return bin(answer)[2:]