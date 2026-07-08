# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181872
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 08. 14:12:49

def solution(myString, pat):
    # rfind(): 찾고자 하는 문자열이 마지막으로 등장하는 시작 인덱스를 반환
    start_idx = myString.rfind(pat)
    
    # pat이 끝나는 위치까지 포함해야 하므로 startIdx + pat.length()를 함
    return myString[:start_idx + len(pat)]