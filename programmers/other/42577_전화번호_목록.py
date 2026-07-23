# 전화번호 목록
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 작성자: 백하은
# 작성일: 2026. 07. 23. 21:19:45

# 문제 이해
# 접두어는 아무래도 가장 짧은 숫자일 가능성이 높음
# 숫자를 사전순으로 정렬하면 i번째랑 i+1번째랑 비교하면서 .startswith()를 써서 푼다면?

def solution(phone_book):
    # 1.phone_book을 사전순으로 정렬
    phone_book.sort()
    
    n = len(phone_book)
    
    # 2.i번째 숫자랑 i+1번째 숫자를 비교 (.startswith 활용):
    # 문자열의 길이가 n이라면 인덱스는 n-1까지 존재
    # i는 0부터 n-2까지 나오도록 해야 함 -> i+1이 있기 때문에
    for i in range(n-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
        
    return True