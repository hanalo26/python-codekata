# 주차 요금 계산
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/92341
# 알고리즘: 해시, 시뮬레이션
# 작성자: 백하은
# 작성일: 2026. 07. 24. 23:12:28

import math

# HH:MM을 MM 형태의 정수로 변환하는 함수
def to_mins(time_str):
    hour, mins = map(int, time_str.split(":"))
    
    time = hour * 60 + mins
    
    return time


# 주차 시간별 주차 요금 계산 
def solution(fees, records):
    
    # 기본 주차 시간/요금, 초과 시간당 요금 변수에 저장
    basic_time, basic_fee, over_time, over_fee = fees
    
    # 현재 주차 되어 있는 차 (차량 번호:입차 시간(분))
    parkings = {}
    
    # 차량번호별 누적 주차 시간 {차량 번호:누적 주차 시간(분)}
    total_times = {}
    
    # records에서 하나씩 꺼내면서 parkings와 total_time에 저장
    for record in records:
        # t는 입차 또는 출차 시간
        # n은 차량 번호
        # io는 입차/출차 여부
        t, n, io = record.split()
        
        # 시간 변환
        time = to_mins(t)
        
        # 입차라면?
        if io == "IN":
            parkings[n] = time
            
        # 출차라면?    
        else: 
            # 누적 시간 계산
            duration = time - parkings[n]
            total_times[n] = total_times.get(n,0) + duration
            
            # 주차 목록에서 제거
            del parkings[n]
            
    # 23:59까지 출차하지 않은 경우
    max_time = to_mins("23:59")
    
    for car_n, car_t in parkings.items():
        duration = max_time - car_t
        total_times[car_n] = total_times.get(car_n,0) + duration
    
    # 반드시 최종 답을 반환하는 형태로 변경해야 함!
    # 차량변호가 작은 순서대로 청구할 주차요금을 담아서 반환
    answer = []
    
    A = sorted(total_times.keys()) # 차량 번호를 정렬하기 위해 만든 임시 변수
    
    for i in A:
        time_to_fee = total_times[i]
        
        # 기본 시간 이하인지 확인
        if time_to_fee <= basic_time:
            answer.append(basic_fee)
        else:
            fee = basic_fee + math.ceil((time_to_fee-basic_time)/over_time)*over_fee
            answer.append(fee)
    
    return answer