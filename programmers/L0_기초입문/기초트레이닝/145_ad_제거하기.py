# ad 제거하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181870
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 06. 29. 16:21:01

def solution(strArr):
    answer = []
    
    for txt in strArr:
        if "ad" not in txt:
            answer.append(txt)
    
    return answer