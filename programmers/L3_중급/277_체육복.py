# 체육복
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42862
# 알고리즘: 그리디
# 작성자: 백하은
# 작성일: 2026. 07. 23. 17:13:32

def solution(n, lost, reserve):
    # 1. 여벌의 체육복이 있는데, 도난당한 학생은 두 리스트에서 모두 제외
    both = list(set(lost)&set(reserve))
    
    for i in both:
        lost.remove(i)
        reserve.remove(i)
    
    # 2. 우선 잃어버린 학생을 제외하고 수업을 들을 수 있는 인원
    can_n = n - len(lost)
    
    # 3. 잃어버린 학생 중 체육복을 빌려 입을 수 있는 인원
    lost.sort()
    
    for j in lost:
        if j-1 in reserve:
            reserve.remove(j-1)
            can_n += 1
        elif j+1 in reserve:
            reserve.remove(j+1)
            can_n += 1
            
    return can_n