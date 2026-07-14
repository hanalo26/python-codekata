# 코드 처리하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181932
# 알고리즘: 조건문
# 작성자: 백하은
# 작성일: 2026. 07. 14. 10:41:41

def solution(code):
    ret=[]
    mode=0 #처음 시작할 때는 0으로 설정
    
    for idx in range(len(code)):
        char = code[idx]
        
        if char == '1':
            mode = 1 - mode
            
        else:
            if mode == 0:
                if idx % 2 == 0:
                    ret.append(char)
            elif mode == 1:
                if idx % 2 != 0:
                    ret.append(char)
                    
    result = "".join(ret)
    
    return result if result else "EMPTY"