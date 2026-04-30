# 로그인 성공?
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120883
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 04. 30. 10:14:28

def solution(id_pw, db):
    user_id, user_pw = id_pw # 유저가 입력한 값
    
    for db_id, db_pw in db: # DB에 저장된 값
        if user_id == db_id: 
            if user_pw == db_pw:
                return 'login'
            else:
                return "wrong pw"
    return "fail"