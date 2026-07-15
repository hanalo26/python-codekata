# 이상한 문자 만들기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12930
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 15. 12:07:41

def solution(s):
    answer = []
    idx = 0 # 각 단어별 인덱스를 기록할 예정
    
    for char in s:
        # 공백을 만난 경우
        if char == " ":
            answer.append(char)
            idx = 0 # 새로운 단어가 시작될 테니 0으로 초기화
        else:
            if idx % 2 == 0:
                answer.append(char.upper())
            else:
                answer.append(char.lower())
            idx += 1
    
    return "".join(answer)