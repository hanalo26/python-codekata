# 배열에서 문자열 대소문자 변환하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181875
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 06. 30. 14:05:57

def solution(strArr):
    
    for txt in strArr:
        for i in range(0,len(strArr)):
            if i % 2 == 0:
                strArr[i] = strArr[i].lower()
            else:
                strArr[i] = strArr[i].upper()
    
    return strArr