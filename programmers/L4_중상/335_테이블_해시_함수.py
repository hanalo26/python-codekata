# 테이블 해시 함수
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/147354
# 알고리즘: 정렬, 해시
# 작성자: 백하은
# 작성일: 2026. 11. 07. 16:15:25

"""
(1) 정렬 기준
    - col번째 컬럼의 값을 기준으로 오름차순 정렬
    - col번째 컬럼 값이 동일할 경우, 1번째 컬럼(기본키)의 값을 기준으로 내림차순 정렬
    ※ 주의, col과 row의 인덱스가 1부터 시작하는 것으로 설정되어 있으므로 배열에 접근할 때는 i번째 항이 i-1 인덱스를 갖고 있음
    
(2) 구해야 하는 것
    - 정렬된 데이터의 i번째 행의 각 원소를 i로 나눈 나머지들의 총합의 XOR(^) 비트 연산을 한 값
    - XOR 비트연산이란? 
        -> 두 개의 입력값이 서로 다를 때만 1(True)이 되고, 서로 같으면 0(False)이 되는 연산
"""

def solution(data, col, row_begin, row_end):
    # 정렬 조건
    # col번째 컬럼(col-1 인덱스) 기준 오름차순, 1번째 컬럼(0 인덱스) 기준 내림차순(-x[0])
    data.sort(key=lambda x: (x[col-1], -x[0]))
    
    answer = 0
    
    # row_begin부터 row_end까지 순회
    for i in range(row_begin, row_end+1):  
        # i번째 행 (0-based 인덱스로는 i - 1)
        row = data[i-1]
        
        # si : 각 원소를 i로 나눈 나머지들의 합
        si = 0
        for val in row:
            si += val % i
            
        # si 값을 누적하여 XOR 비트 연산
        # 비교는 이진수로 변환해서 수행하지만, answer에 담길 때는 우리에게 익숙한 십진수 형태로 담김
        answer = answer ^ si
    
    return answer