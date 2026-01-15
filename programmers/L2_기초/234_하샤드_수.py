# 하샤드 수
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12947
# 알고리즘: 수학, 문자열
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:50:03

def solution(number):
    # 각 자릿수에 있는 숫자들의 합이 저장되는 변수
    each_digits_sum = 0 
    
    # 입력한 숫자를 보존하기 위한 변수 
    # 원본숫자가 변형되면 하샤드 수 계산에 오차가 생기기 때문에 만들었음
    original_number = number 
    
    while original_number > 0:
        # 가장 낮은 자릿수의 숫자를 추출하는 코드
        last_digit = original_number % 10
        each_digits_sum = each_digits_sum + last_digit
        # 나눗셈의 몫만 반환하는 // 연산자를 이용해 가장 낮은 자릿수에 있는 숫자를 제거하는 코드
        original_number = original_number // 10
        
    if number % each_digits_sum == 0:
        print(f'{number}는 하샤드 수입니다.')
        return True
    else:
        print(f'{number}는 하샤드 수가 아닙니다.')
        return False
    
    