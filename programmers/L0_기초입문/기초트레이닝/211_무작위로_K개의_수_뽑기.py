# 무작위로 K개의 수 뽑기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181858
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 07. 12. 16:41:12

def solution(arr, k):
    answer = []
    
    for num in arr:
		    # answer에 포함된 값이면 건너뜀
        if num in answer:
            continue
        else:
            answer.append(num)
        
        # answer의 길이가 k와 같아지면 즉시 stop
        if len(answer) == k:
            return answer
    
    # k보다 짧다면 -1을 채워 길이가 k가 되도록 함    
    while len(answer) < k:
        answer.append(-1)
    
    return answer 