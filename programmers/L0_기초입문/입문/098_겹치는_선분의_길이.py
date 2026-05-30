# 겹치는 선분의 길이
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120876
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 05. 30. 15:29:08

def solution(lines):
    # -100 ~ 100 범위를 처리하기 위한 배열 (0~200의 인덱스를 처리하기 위해서는 201칸 필요)
    line_cnt = [0]*201
    
    for start, end in lines:
    # 인덱스 접근 시 +100을 하여 음수 좌표를 양수로 변환
    # 각 선분이 지나는 곳에 +1
        for i in range(start, end):
            line_cnt[i+100] += 1
        
    # 값이 2 이상인 칸의 개수 count
    answer = sum(1 for cnt in line_cnt if cnt >1)
    return answer