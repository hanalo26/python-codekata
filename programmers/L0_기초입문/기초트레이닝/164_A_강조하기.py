# A 강조하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181874
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 02. 17:18:46

def solution(myString):
    myString = myString.lower()
    
    answer = ""
    
    for txt in myString:
        if txt == "a":
            answer += "A"
        else:
            answer += txt
            
    return answer