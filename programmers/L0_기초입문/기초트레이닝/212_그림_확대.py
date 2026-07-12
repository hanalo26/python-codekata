# 그림 확대
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181836
# 알고리즘: 반복문 활용
# 작성자: 백하은
# 작성일: 2026. 07. 12. 16:46:46

def solution(picture, k):
    answer = []
    
    # 한 줄씩 꺼냄
    for row in picture:
        expanded_row = ""
        
        # 해당 줄에 있는 글자(pixel)를 하나씩 꺼내 k배로 늘려 가로 문자열 작성
        for pixel in row:
            expanded_row += pixel*k
            
        # 가로로 늘어난 문자열(expanded_row)을 세로 배율 k만큼 반복해서 정답에 추가
        for _ in range(k):
            answer.append(expanded_row)
    
    return answer