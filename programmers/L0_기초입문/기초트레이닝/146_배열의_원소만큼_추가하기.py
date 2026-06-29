# 배열의 원소만큼 추가하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181861
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 06. 29. 16:43:26

def solution(arr):
    answer = []
    
    for i in arr:
        # [num] 리스트를 num 번 복사해서 answer 리스트 뒤에 붙임
        # extend(): 여러 원소를 한 번에 리스트 뒤에 이어 붙여줌
        answer.extend([i]*i)
    
    return answer