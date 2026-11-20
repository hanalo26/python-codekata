# 우박수열 정적분
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/134239
# 알고리즘: 수학, 시뮬레이션
# 작성자: 백하은
# 작성일: 2026. 11. 20. 14:28:10

"""
[우박수열 만드는 방법]
1. 시작 숫자인 k가 1이 될 때까지 아래 규칙을 반복해 적용
    1-1. 입력된 수가 짝수라면 2로 나눕니다.
    1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.

[은지가 구하고자 하는 것]
1. 위 규칙을 적용하며 k가 1이 될때까지 계산하면서 나온 값을 모두 그래프에 찍어 꺾은선 그래프를 그리고, 구간 [a,b]까지의 넓이가 담긴 리스트
2. (0,k), (1, 두번째 항), . . . , (n, 1)로 점을 찍음
3. 정적분한 넓이 구하는 식 
    = (윗변 + 아랫변) × 높이 ÷ 2 
    = (y[i] + y[i + 1]) × 1 ÷ 2 {x = i, x = i + 1일때}
4. 구간 [a,b]의 규칙
    - b는 0 또는 음수이므로, 실제로는 전체 구간인 [0,n]을 정적분한 값에서 n에서 b의 값을 뺀 구간의 넓이를 구하는 것과 같음
    - 단, n+b보다 a가 더 크면 그건 유효하지 않은 구간이므로 -1을 반환한다.
"""

def solution(k, ranges):
    # 1. 우박수열 만들기
    seq = [k]
    n = 0 # 우박수열을 만들기 위해 시도한 횟수
    while k > 1:
        if k % 2 == 0:
            k = k // 2
        else:
            k = k * 3 + 1
        seq.append(k)
        n += 1
    
    # 2. 높이가 1인 평행사변형의 넓이를 모두 구해 누적합 배열 제작
    prefix_area = [0.0]
    for i in range(n):
        area = (seq[i]+seq[i+1]) / 2.0
        # 직전 항의 값과 계산한 값을 더해 누적합을 담을 예정 (원하는 값을 바로 꺼내서 사용할 수 있도록 하기 위해서)
        prefix_area.append(prefix_area[-1]+area)
    
    # 3. 주어진 구간을 확인하면서 답을 계산
    answer = []
    for a, b in ranges:
        start = a
        end = n + b
        
        if start > end:
            answer.append(-1.0)
        else:
            # 넓이 계산 = (0~end까지의 넓이) - (0~start까지의 넓이)
            a = prefix_area[end] - prefix_area[start]
            answer.append(a)
    
    return answer