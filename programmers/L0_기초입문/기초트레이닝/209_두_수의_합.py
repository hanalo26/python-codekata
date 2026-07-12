# 두 수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181846
# 알고리즘: 함수(메서드)
# 작성자: 백하은
# 작성일: 2026. 07. 12. 16:28:12

import sys

# 정수 변환 자릿수 제한을 100,000자리 이상 늘림
sys.set_int_max_str_digits(200000)

def solution(a, b):
    return str(int(a)+int(b))