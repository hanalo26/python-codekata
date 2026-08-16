# 주차 요금 계산
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/92341
# 알고리즘: 해시, 시뮬레이션
# 작성자: 백하은
# 작성일: 2026. 08. 16. 19:28:28

"""
<문제 조건 정리>
(1) 변수
fees = [기본요금(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)]

records = ["입차 또는 출차 시각(시:분) 차량번호 내역(IN/OUT)"]
ㄱ. 23:59까지 출차기록이 없다면 요금은 23:59에 출차한 것을 기준으로 계산한다.

(2) 차량번호가 작은 차량부터 순서대로 청구할 주차요금이 담긴 리스트 반환

(3) 구해야 하는 것
ㄱ. HH:MM을 모두 분단위로 변환 -> 입차~출차까지 누적 주차시간(분)
ㄴ. 주차요금
"""
import math

# HH:MM -> 00:00를 기준으로 분으로 변환
def h_to_m(time_str):
    h, m = map(int, time_str.split(':'))
    
    t = h * 60 + m
    
    return t

# 주차요금 계산
def solution(fees, records):
    answer = []
    
    # 요금표 내 원소들을 각각 변수에 할당
    basic_time, basic_fee, over_time, over_fee = fees
    
    # records 요소 분해
    parking = {} # 주차되어 있는 차량 {차량번호:입차시간}
    total_t = {} # 출차된 차량의 주차시간 {차량번호:주차시간}
    
    for r in records:
        time, car_num, in_out = r.split()
        
        t = h_to_m(time)
        
        # 입차일 때
        if in_out == "IN":
            parking[car_num] = t
        # 출차일 때
        else:
            durations = t - parking[car_num]
            # 같은 번호의 차량이 두 번 입차했을 경우를 대비
            # 예제 케이스에서 0000 차량이 실제로 2번 입차함
            total_t[car_num] = total_t.get(car_num, 0) + durations
            del parking[car_num] # 출차하였으므로 주차 목록에서 삭제
            
    # 23:59까지 출차기록이 없다면?
    for n, t in parking.items():
        durations = h_to_m("23:59") - parking[n]
        total_t[n] = total_t.get(n, 0) + durations

    # 차량번호가 작은 순서대로 정렬
    sorted_CarNums = sorted(total_t.keys())
        
    # 주차 요금 계산
    for n in sorted_CarNums:
        sum_time = total_t[n] # 차량번호만 정렬된 리스트에서 차량번호를 꺼낸 뒤, 요금 계산에 활용
        
        # 요금 계산 시작!!!!
        if sum_time <= basic_time:
            answer.append(basic_fee)
        else:
            # 기본요금+추가요금
            m = basic_fee + math.ceil((sum_time-basic_time)/over_time)*over_fee
            answer.append(m)
    
    return answer