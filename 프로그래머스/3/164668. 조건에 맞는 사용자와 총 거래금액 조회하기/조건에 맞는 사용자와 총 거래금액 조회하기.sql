-- 코드를 입력하세요
SELECT u.USER_ID, u.NICKNAME, sum(b.PRICE) as TOTAL_SALES

from USED_GOODS_BOARD b
join USED_GOODS_USER u on u.USER_ID=b.WRITER_ID
where b.STATUS ='DONE'
group by u.USER_ID
having TOTAL_SALES >=700000
order by TOTAL_SALES asc