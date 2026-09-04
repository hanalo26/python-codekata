# 2개 이하로 다른 비트
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/77885
# 알고리즘: 비트연산
# 작성자: 백하은
# 작성일: 2026. 09. 04. 15:37:33

"""
- 짝수의 이진수 비트 마지막 숫자: 0
    ->  가장 마지막 비트(0)를 1로 바꾸는 것(즉, x + 1)이 비트 1개만 다르면서 x보다 큰 가장 작은 수
    
- 홀수의 이진수 비트 마지막 숫자: 1
    -> 오른쪽에서부터 가장 처음 나타나는 0을 1로 바꾸고, 그 바로 오른쪽의 1을 0으로 바꾸는 것이 비트가 2개만 다르면서 x보다 큰 가장 작은 수 

"""

def solution(numbers):
    answer = []
    
    for x in numbers:
        # 짝수/홀수 판단
        if x % 2 == 0:
            answer.append(x+1)
        else:
            # 비트 연산으로 가장 오른쪽에 있는 '01' 패턴 찾기
            # 가장 오른쪽 0을 찾는 이유: 수의 증가 폭을 최소화하기 위함.
            #오른쪽 1을 0으로 바꾸는 이유: 비트 변환 2개 제한 내에서 수의 크기를 다시 최대한 깎아내리기 위함
            binary = '0' + bin(x)[2:]
            # 오른쪽에서부터 탐색
            idx = binary.rfind('0')
            
            # 0은 1로, 1은 0으로 변경
            binary_l = list(binary)
            binary_l[idx] = '1'
            binary_l[idx+1] = '0'
            
            answer.append(int("".join(binary_l),2))
    
    return answer