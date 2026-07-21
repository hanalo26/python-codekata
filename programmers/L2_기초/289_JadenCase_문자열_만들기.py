# JadenCase 문자열 만들기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12951
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 21. 13:22:54

def solution(s):
    # 공백 한 칸을 기준으로 분할
    # 연속된 공백도 빈 문자열로 보존할 수 있는 방식
    words = s.split(" ")
    
    # capitalize(): 첫 글자가 영문인 경우에 대문자로 변환시켜줌
    Jaden_words = []
    
    for word in words:
        Jaden_words.append(word.capitalize())
        
    # 공백 한 칸씩 띄어서 하나의 문자열로 연결
    return " ".join(Jaden_words)