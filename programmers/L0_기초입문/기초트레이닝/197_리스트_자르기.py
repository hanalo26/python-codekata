# 리스트 자르기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181897
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 07. 10. 22:02:23

def solution(n, slicer, num_list):
    a = slicer[0]
    b = slicer[1]
    c = slicer[2]
    
    # 조건별 처리
    if n == 1:
        return num_list[:b+1]
    elif n == 2:
        return num_list[a:]
    elif n == 3:
        return num_list[a:b+1]
    elif n == 4:
        return num_list[a:b+1:c]