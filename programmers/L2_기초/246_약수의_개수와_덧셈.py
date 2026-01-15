# 약수의 개수와 덧셈
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/77884
# 알고리즘: 수학
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:54:20

def solution(left, right):
    result = 0
    for number in range(left, right+1):
        num = int(number ** 0.5) # number의 제곱근을 구함
        if num * num == number: # 제곱해서 나오는 수라면 뺼셈을, 아니라면 덧셈을 하도록 함
            result = result - number
        else:
            result += number
            
    return result       