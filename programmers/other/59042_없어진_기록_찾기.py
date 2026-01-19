# 없어진 기록 찾기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59042
# 작성자: 백하은
# 작성일: 2026. 01. 19. 20:01:15

select 
    o.ANIMAL_ID,
    o.NAME
from ANIMAL_OUTS as o
left join ANIMAL_INS as i
  on o.ANIMAL_ID = i.ANIMAL_ID
where i.ANIMAL_ID is null
order by o.ANIMAL_ID;