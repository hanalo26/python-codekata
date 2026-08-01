# 이진 변환 반복하기
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/70129
# 알고리즘: 시뮬레이션, 문자열
# 작성자: 백하은
# 작성일: 2026. 08. 01. 15:22:36

def solution(s):
    # 이진변환 횟수, 제거된 0의 개수
    transform_cnt = 0
    del_zero = 0
    
    # s가 "1"이 될 때까지 반복 -> 0이 남아있지 않도록 이진 변환을 반복
    while s != "1":
        transform_cnt += 1
        
        # 0의 개수 카운트해서 누적
        del_zero += s.count("0")
        
        # 0 삭제
        s = s.replace("0","")
        
        # 남은 1의 개수 = 1의 총합
        new_s = len(s)
        
        # 다시 2진수로 변경 
        # bin()을 사용하면 "0b(이진수 변환형태)"로 나옴
        s = bin(new_s)[2:]
        
    return [transform_cnt, del_zero]