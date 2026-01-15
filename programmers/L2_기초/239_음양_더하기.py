# 음양 더하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/76501
# 알고리즘: 배열
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:51:43

def solution(absolutes, signs):
    total = 0
    
    # signs에서 True면 양수, False면 음수
    # zip() 함수를 사용해 두 배열을 동시에 순회할 예정
    for number, sign in zip(absolutes, signs):
        if sign == True:
            total += number
        else:
            total -= number
    return total    