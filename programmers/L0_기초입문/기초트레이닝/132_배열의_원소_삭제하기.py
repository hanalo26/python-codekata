# 배열의 원소 삭제하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181844
# 알고리즘: 조건문 활용
# 작성자: 백하은
# 작성일: 2026. 06. 25. 20:23:30

def solution(arr, delete_list):
    answer = []
    for num in arr:
        if num not in delete_list:
            answer.append(num)
            
    return answer