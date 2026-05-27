# 최빈값 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120812
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 05. 27. 19:52:24

def solution(array):
    # 0~999까지의 숫자가 등장할 때마다 해당 위치의 원소가 +1
    counts = [0] * 1000
    
    for num in array:
        counts[num] += 1
        
    # counts의 인덱스는 array의 원소를 뜻하고, 값은 빈도수를 의미함
    max_cnt = max(counts)
    
    # max_cnt가 중복값으로 몇 개 존재하는지 확인하는 메서드 : .count()
    if counts.count(max_cnt) > 1:
        return -1
    else:
        return counts.index(max_cnt)