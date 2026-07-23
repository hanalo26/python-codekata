# K번째수
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42748
# 알고리즘: 정렬
# 작성자: 백하은
# 작성일: 2026. 07. 23. 23:38:18

def solution(array, commands):
    answer = []
    
    # [[i,j,k]]의 형태로 commands에 저장됨
    # i, j: array에서 잘라서 가져올 부분과 관련된 변수
    # k: 부분 리스트에서 k번째에 있는 수를 answer에 담아서 반환
    
    for c in commands:
        i = c[0]
        j = c[1]
        k = c[2]
        
        # 인덱스는 0부터 이므로 뜯어와야 하는 부분의 인덱스는 (i-1) ~ (j-1)
        part = array[i-1:j]
        
        sorted_part = sorted(part)
        
        answer.append(sorted_part[k-1])
    
    return answer