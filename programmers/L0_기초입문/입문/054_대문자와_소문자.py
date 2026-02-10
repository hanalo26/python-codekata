# 대문자와 소문자
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120893
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 02. 10. 09:48:45

# 첫 번째 시도
def solution(my_string):
    answer = ''
    
    for text in my_string:
        if text.isupper():
            answer += text.lower()
        else:
            answer += text.upper() 
  
    return answer        
    
# 새롭게 배운 .swapcase() 매서드 활용
# .swapcase() : 문자열 내에서 대문자는 소문자로, 소문자는 대문자로 바꿔줌
def solution(my_string):
    return my_string.swapcase()    