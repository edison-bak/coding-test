-- 코드를 입력하세요
SELECT A.animal_id, A.name
from ANIMAL_INS A
join ANIMAL_OUTS B on A.ANIMAL_ID=B.ANIMAL_ID
order by A.datetime-B.datetime
limit 2