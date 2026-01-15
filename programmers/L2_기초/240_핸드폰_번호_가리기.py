# 핸드폰 번호 가리기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12948
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:52:00

def solution(phone_number):
    answer = ''
    
    hidden_part = '*' * (len(phone_number)-4)
    showing_part = phone_number[-4:]
    
    answer = hidden_part + showing_part
    
    return answer