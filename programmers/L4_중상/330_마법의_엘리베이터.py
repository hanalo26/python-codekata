# 마법의 엘리베이터
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/148653
# 알고리즘: 그리디
# 작성자: 백하은
# 작성일: 2026. 11. 02. 15:46:34

# storey: 민수의 현재 위치
# 목표: 현재 위치에서 0층으로 가기 위해 필요한 마법의 돌의 최소 개수
# 반올림을 적용해서 풀이할 예정
def solution(storey):
    answer = 0
    
    while storey > 0:
        # 가장 낮은 자릿수의 숫자 계산
        remainder = storey % 10
        
        # 다음 자릿수로 넘어가기 위해 10으로 나눔
        storey = storey // 10
        
        # 1. 나머지가 6 이상인 경우: 차라리 윗자리에 1을 더해주고 빼는(- 연산) 것이 이득
        if remainder > 5:
            answer += (10 - remainder)
            storey += 1 # 바로 위 자릿수에 일을 더해서 10의 제곱으로 이동할 수 있도록 계산
        
        # 2. 나머지가 4 이하인 경우: 그냥 현재 숫자만큼 빼는(- 연산) 것이 이득
        elif remainder < 5:
            answer += remainder
        
        # 3. 나머지가 정확히 5인 경우: 바로 윗자리의 숫자를 보고 결정
        else:
            # 윗자리가 5 이상이면, 윗자리에 1을 더해주는 것이 유리, 왜냐하면 다음 위 자릿수에 1을 더하는 것이 더 돌을 더 적게 쓸 수 있어서
            if storey % 10 >= 5:
                answer += 5
                storey += 1
            else:
                answer += remainder
    
    return answer