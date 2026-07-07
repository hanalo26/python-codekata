# 빈 배열에 추가, 삭제하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181860
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 07. 07. 16:16:26

def solution(arr, flag):
    answer = []
    
    # arr의 숫자(num)와 flag의 조건(f)을 한 쌍으로 묶어 순회
    for num, f in zip(arr, flag):
        if f:
            # num을 num * 2번 반복한 리스트를 뒤에 이어 붙임
            answer.extend([num]*(num*2))
        else:
            # 맨 뒤에서부터 num개만큼 원소를 잘라내어 제거
            answer = answer[:-num]
    
    return answer