# k의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120887
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 02. 26. 09:38:18

def solution(i, j, k):
    answer = 0
    
    # k를 문자열로 변환
    target = str(k)
    
    for num in range(i, j+1):
        str_num = str(num)
        
        # target이 str_num에 몇 개 있는지 세어서 더함
        # .count('찾고자 하는 문자', 범위)
        answer += str_num.count(target)
    
    return answer