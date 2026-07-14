# 배열 만들기 2
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181921
# 알고리즘: 반복문
# 작성자: 백하은
# 작성일: 2026. 07. 14. 10:36:30

def solution(l, r):
    answer = []
    
    # bin(i)[2:]를 하면 i를 2진법 문자열로 바꿔줌
    i=1
    while True:
        binary_str = bin(i)[2:]
        
        # 1를 5로 변경 (2진법 숫자에 5를 곱하는 효과)
        num = int(binary_str.replace('1','5'))

        if num > r:
            break
        elif num >= l:
            answer.append(num)
            
        i += 1
        
    return answer if answer else [-1]