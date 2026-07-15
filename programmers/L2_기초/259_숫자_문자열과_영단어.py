# 숫자 문자열과 영단어
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/81301
# 알고리즘: 문자열, 해시
# 작성자: 백하은
# 작성일: 2026. 07. 15. 12:56:43

def solution(s):
    dict_game = {
        "zero":"0",
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"
    }
    
    for key, value in dict_game.items():
        s = s.replace(key, value)
        
    return int(s)