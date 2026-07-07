# 날짜 비교하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181838
# 알고리즘: 조건문 활용
# 작성자: 백하은
# 작성일: 2026. 07. 07. 16:07:17

def solution(date1, date2):
    # 파이썬은 리스트끼리 대소 비교 시,
    # 자동으로 0번 인덱스(연) -> 1번 인덱스(월) -> 2번 인덱스(일) 순서로 비교함 
    if date1 < date2:
        return 1
    else:
        return 0