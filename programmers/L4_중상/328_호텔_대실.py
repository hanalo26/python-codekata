# 호텔 대실
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/155651
# 알고리즘: 정렬, 그리디
# 작성자: 백하은
# 작성일: 2026. 10. 28. 13:07:11

"""
(1) book_time은 [대실 시작 시각, 대실 종료 시각]으로 구성된 이차원 배열
(2) 대실 종료 후, 10분은 청소 시간이므로 다음 고객은 대실 종료 시각+10분 후부터 입장 가능
"""
import heapq

# 문자열을 분 단위의 숫자로 변환하는 함수
def traslate_time(time_str):
    h, m = map(int, time_str.split(':'))
    
    t = h*60+m
    
    return t

def solution(book_time):    
    # 고객별 퇴실시간에 청소시간을 더해서 새로운 배열 생성
    convert_time = []
    
    for start, end in book_time:
        start_time = traslate_time(start)
        end_time = traslate_time(end)+10
        
        convert_time.append((start_time, end_time))
        
    # 입실 시간을 기준으로 정렬
    convert_time.sort(key=lambda x: x[0])
    
    # 현재 사용 중인 방들의 청소 완료 시간을 관리할 최소 힙
    room = []
    
    # 방이 오픈되어 있고, 가장 빨리 비어 있는 방의 청소 완료 시간이 다른 손님의 입실 시간보다 빠르거나 같다면 기존에 썼던 방을 재사용할 수 있으므로 해당 방의 퇴실 시간을 새로운 값으로 갱신한다.
    # 그렇지 않다면 새로운 방을 배정할 것
    for s, e in convert_time:
        if room and room[0] <= s:
            heapq.heappop(room)
            
        heapq.heappush(room, e)
    
    return len(room)