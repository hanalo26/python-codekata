# 홀짝 구분하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181944
# 알고리즘: 출력
# 작성자: 백하은
# 작성일: 2026. 06. 09. 21:27:17

n = int(input())

if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")