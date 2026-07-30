# 성격 유형 검사하기
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/118666
# 알고리즘: 해시, 시뮬레이션
# 작성자: 백하은
# 작성일: 2026. 07. 30. 14:25:04

def solution(survey, choices):
    # 각 성격 유형별 점수를 저장할 딕셔너리
    scores = {
        "R":0,
        "T":0,
        "C":0,
        "F":0,
        "J":0,
        "M":0,
        "A":0,
        "N":0
    }
    
    # 매우 비동의(1정) ~ 매우 동의 (7점) 에 따른 점수 부여
    for s, choice in zip(survey, choices):
        disagree_type = s[0]
        agree_type = s[1]
        
        if choice < 4: # 비동의 선택
            scores[disagree_type] += (4-choice)
            
        elif choice > 4: # 동의 선택
            scores[agree_type] += (choice-4)
            
    # 성격 유형 탐지
    answer = ""
    
    # RT
    if scores["R"] >= scores["T"]:
        answer += "R"
    else:
        answer += "T"
    
    # CF
    if scores["C"] >= scores["F"]:
        answer += "C"
    else:
        answer += "F"
    
    # JM
    if scores["J"] >= scores["M"]:
        answer += "J"
    else:
        answer += "M"
    
    # AN
    if scores["A"] >= scores["N"]:
        answer += "A"
    else:
        answer += "N"
    
    return answer