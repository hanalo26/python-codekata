# 주차 요금 계산
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/92341
# 알고리즘: 해시, 시뮬레이션
# 작성자: 백하은
# 작성일: 2026. 07. 25. 21:34:18

# fees: 주차요금 [기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)]
## 주차 요금은 분 단위로 진행 -> 00:00를 기준으로 n분 지난 시간이 입/출차 시간인지 변환 필요
# records: 자동차의 입/출차 내역 ["시각 차량번호 내역(IN/OUT)"]
## IN/OUT으로 입/출차 구분
## 23:59까지 출차 기록이 없다면, 해당 차량은 23:59에 출차한 것으로 계산
# 주차요금이 담긴 리스트 출력 (최종 답) - 단, 정렬 기준은 차량번호

# 문제를 구하기 위해 필요한 것
## 입차 ~ 출차까지 누적 주차시간, 00:00를 기준으로 N분이 지난 시간인지 계산, 청구할 요금 계산, 누적주차시간과 요금은 차량번호와 반드시 연결해서 사용

# ======================================
import math

# HH:MM을 00:00을 기준으로 몇 분 지난건지, 분으로 환산하는 함수
def hour_to_min(time_str):
    hour, mins = map(int, time_str.split(":"))
    
    answer = hour * 60 + mins
    
    return answer

# 메인
def solution(fees, records):
    answer = [] # 누적 요금만 담아서 출력
    
    # fees 분리
    basic_time, basic_fee, over_time, over_fee = fees
    
    # records 분해 -> 시각, 차량번호 입/출차 내역이 나올 예정
    
    ## 현재 주차 되어 있는 차량 목록 {차량번호:입차시간}
    parkings = {}
    
    ## 출차한 차량의 주차 요금 {차량번호:누적 시간}
    total_time = {}
    
    for record in records:
        time, car_num, in_out = record.split()
        
        t = hour_to_min(time)
        
        # 입차라면 -> parkings에 담기 // 출차라면 -> 시간을 분으로 환산해서 누적 주차시간 계산
        if in_out == "IN":
            parkings[car_num] = t
        else:
            durations = t - parkings[car_num]
            total_time[car_num] = total_time.get(car_num,0) + durations
            del parkings[car_num]
        
    # 주차된 차량 목록에 차량이 남아있다면 -> 주차시간은 23:59 기준으로 계산
    for n, t in parkings.items():
        duration = hour_to_min("23:59") - parkings[n]
        total_time[n] = total_time.get(n,0) + duration
        
        
    # total_time를 키인 차량 번호 순서대로 정렬하고, 주차 요금 계산
    CAR_NUM_sorted = sorted(total_time.keys())
    
    for n in CAR_NUM_sorted:
        sum_time = total_time[n]
        
        # 기본 시간 이하일 때 -> 기본요금 // 기본 시간 초과 추가요금 계산
        if sum_time <= basic_time:
            answer.append(basic_fee)
        else:
            fee = basic_fee + math.ceil((sum_time-basic_time)/over_time)*over_fee
            answer.append(fee)
            
    return answer