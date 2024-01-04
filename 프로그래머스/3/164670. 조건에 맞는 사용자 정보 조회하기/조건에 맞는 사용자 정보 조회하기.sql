-- 코드를 입력하세요
SELECT us.USER_ID,us.NICKNAME,concat(us.CITY,' ',us.STREET_ADDRESS1,' ',us.STREET_ADDRESS2) as 전체주소,
CONCAT(
  SUBSTRING(TLNO, 1, 3), '-', -- 국번
  SUBSTRING(TLNO, 4, 4), '-', -- 가운데 번호
  SUBSTRING(TLNO, 8, 4)        -- 마지막 번호
) AS 전화번호
from USED_GOODS_BOARD boa
join USED_GOODS_USER us on us.USER_ID =boa.WRITER_ID
group by boa.WRITER_ID
having count(boa.WRITER_ID)>=3
order by us.USER_ID desc