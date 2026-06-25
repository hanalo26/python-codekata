# l로 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181834
# 알고리즘: 반복문 활용
# 작성자: 백하은
# 작성일: 2026. 06. 25. 17:52:38

def solution(myString):
    answer = ''
    
    for txt in myString:
        # 문자열을 비교할 때 숫자를 비교하는 것과 동일한 비교연산자 사용 가능 -> 내부적으로 문자를 아스키코드 숫자로 인식하기 때문에
        if txt < 'l':
            answer += 'l'
        else:
            answer += txt
    
    return answer