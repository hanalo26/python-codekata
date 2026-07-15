# 시저 암호
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12926
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 15. 12:49:30

def solution(s, n):
    answer = []
    
    for char in s:
        # 공백은 그대로 유지
        if char == " ":
            answer.append(char)
        
        # 대문자인 경우
        elif char.isupper():
            # 'A'의 아스키코드(65)를 기준으로 몇 번째 알파벳인지 계산 후 n만큼 밀기
            new_char = chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            answer.append(new_char)
            
        # 소문자인 경우
        elif char.islower():
            # 'a'의 아스키코드(97)를 기준으로 몇 번째 알파벳인지 계산 후 n만큼 밀기
            new_char = chr((ord(char) - ord('a') + n) % 26 + ord('a'))
            answer.append(new_char)
            
    return "".join(answer)