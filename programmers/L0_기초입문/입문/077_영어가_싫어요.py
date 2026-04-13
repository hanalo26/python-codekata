# 영어가 싫어요
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120894
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 04. 13. 21:53:43

def solution(numbers):
    # 인덱스가 번호가 되고, 영단어가 리스트 내 값이 되도록 만듦
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    # 반복문을 돌며 영단어를 숫자로 치환
    # .replace() : 문자열 안에서 특정 word를 찾아 다른 글자로 바꿈
    for i, word in enumerate(words):
        numbers = numbers.replace(word, str(i))
        
    return int(numbers)
    