# 세 개의 구분자
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181862
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 09. 15:50:14

def solution(myStr):
    answer = []
    temp = ""  # 글자 조각을 임시로 모아둘 빈 문자열 가방
    
    for char in myStr:
        # 현재 글자가 구분자(a, b, c) 중 하나라면
        if char in ['a', 'b', 'c']:
            # 임시 가방에 글자가 들어있을 때만 정답에 추가 (연속된 구분자 방지)
            if temp:
                answer.append(temp)
                temp = ""  # 다음 조각을 위해 가방을 비움
        else:
            # a, b, c가 아니라면 임시 가방에 글자를 수집
            temp += char
            
    # 중요! 문자열이 끝났는데 마지막 가방에 글자가 남아있다면 추가
    if temp:
        answer.append(temp)
        
    # 만약 정답 리스트가 비어있다면 ["EMPTY"] 반환, 있다면 리스트 반환
    return answer if answer else ["EMPTY"]