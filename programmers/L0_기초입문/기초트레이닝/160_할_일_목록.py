# 할 일 목록
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181885
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 07. 02. 17:09:12

def solution(todo_list, finished):
    answer = []
    
    for i in range(len(todo_list)):
        # 완료하지 못한 일(false)을 부정해야 조건문 실행 가능
        if not finished[i]:
            answer.append(todo_list[i])
    
    return answer