# 직사각형 별찍기
# 프로그래머스 L1 (입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12969
# 알고리즘: 반복문
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:52:33

width, height = map(int, input().split(' '))

for i in range(height):
    print('*' * width)  