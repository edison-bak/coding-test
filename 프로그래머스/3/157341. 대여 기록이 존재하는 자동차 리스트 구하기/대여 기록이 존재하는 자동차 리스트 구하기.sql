-- 코드를 입력하세요
SELECT car.CAR_ID

from CAR_RENTAL_COMPANY_CAR car

join CAR_RENTAL_COMPANY_RENTAL_HISTORY rent 
on car.CAR_ID=rent.CAR_ID
where rent.START_DATE like '2022-10%' and
car.CAR_TYPE ='세단'
group by car.CAR_ID
order by car.CAR_ID desc