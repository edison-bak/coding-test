-- 코드를 입력하세요
SELECT B.CATEGORY AS CATEGORY, sum(A.SALES) as TOTAL_SALES
from BOOK_SALES A
join BOOK B on A.BOOK_ID=B.BOOK_ID
where DATE_FORMAT(A.sales_date, '%Y-%m') = '2022-01'
group by B.CATEGORY
order by B.CATEGORY asc
