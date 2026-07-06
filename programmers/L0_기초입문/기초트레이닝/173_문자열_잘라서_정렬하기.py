# 문자열 잘라서 정렬하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181866
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 06. 14:47:45

def solution(myString):
    
    # "x"를 기준으로 문자열 자르기
    split_myString = myString.split("x")
    
    # 빈 문자열이 아닌 요소만 골라서 정렬
    answer = sorted([txt for txt in split_myString if txt != ""])
    
    return answer