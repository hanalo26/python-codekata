# 주사위 게임 3
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181916
# 알고리즘: 조건문
# 작성자: 백하은
# 작성일: 2026. 07. 14. 10:58:29

def solution(a, b, c, d):
    dice = [a,b,c,d]
    
    count={}
    for num in dice:
        # num 키를 찾되, 없으면 0을 기본값으로 하고, 1을 더한다
        count[num] = count.get(num,0) + 1
        
    sorted_res = sorted(count.items(), key=lambda x:x[1],reverse=True)
    
    unique_cnt = len(sorted_res)
    
    if unique_cnt == 1:
        p = sorted_res[0][0]
        return 1111*p
    
    elif unique_cnt == 2:
        if sorted_res[0][1] == 3:
            p=sorted_res[0][0]
            q=sorted_res[1][0]
            return (10*p+q)**2
        else:
            p=sorted_res[0][0]
            q=sorted_res[1][0]
            return (p+q)*abs(p-q)
        
    elif unique_cnt==3:
        p=sorted_res[1][0]
        q=sorted_res[2][0]
        return p*q
    
    else:
        return min(dice)