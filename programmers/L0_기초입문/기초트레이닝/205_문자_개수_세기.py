# 문자 개수 세기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181902
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 07. 11. 20:11:16

def solution(my_string):
    # 대문자(0~25) + 소문자(26~51)가 순서대로 배치된 가이드 맵
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    answer = [0] * 52
    
    for char in my_string:
        # 현재 글자가 alphabet 문자열에서 몇 번째 방에 있는지 인덱스를 찾음
        idx = alphabet.index(char)
        answer[idx] += 1
        
    return answer