# 체육복
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42862
# 알고리즘: 그리디
# 작성자: 백하은
# 작성일: 2026. 07. 23. 13:15:24

# 문제 조건
# 체육복이 있어야 체육 수업을 들을 수 있음
# 체육복을 빌릴때는 자신의 번호를 기준으로 바로 앞뒤 번호 학생에게만 빌릴 수 있음

# lost: 체육복을 잃어버린 학생
# reserve: 여벌의 체육복을 가져온 학생
# 여벌의 체육복을 가져왔는데, 도난당했다면 체육복을 빌려줄 수 없음
# lost, reverse에서는 중복되는 값이 없음
# n: 전체 학생 수, 2~30명

def solution(n, lost, reserve):
    # lost와 reserve에 중복이 있는지 확인 -> 중복이 있다면 reserve, lost에서 삭제
    both = list(set(lost)&set(reserve))
    
    for i in both:
        lost.remove(i)
        reserve.remove(i)
    
    # n에서 잃어버린 학생 수를 제외해 자신의 체육복으로 수업을 들을 수 있는 학생 수 count
    can_n = n - len(lost)
    
    
    # lost를 번호 순으로 돌면서, 앞번호에 여벌이 있으면 빌리고, 없으면 뒷번호에서 빌린다
    # lost 학생의 번호에서 -1을 했을 때, 여벌이 있다면 그 학생에게 빌리고 없다면 lost 학생의 번호에서 +1을 한 학생에게 빌린다. 그리고 체육복을 빌려준 학생은 reserve에서 제거한다
    
    # lost의 번호를 오름차순으로 정렬
    sorted_lost = sorted(lost)
    
    for j in sorted_lost:
        if j-1 in reserve:
            reserve.remove(j-1)
            can_n += 1
            
        elif j+1 in reserve:
            reserve.remove(j+1)
            can_n += 1
            
    return can_n