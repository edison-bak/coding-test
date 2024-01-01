-- 코드를 입력하세요
-- 자동차 종류가 '세단' 또는 'SUV' 인 자동차
-- 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고
-- 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차
-- 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력
SELECT menu.CAR_ID,menu.CAR_TYPE,
menu.DAILY_FEE*30*(1-0.01*REPLACE(pro.DISCOUNT_RATE, '%', '')) as FEE

from CAR_RENTAL_COMPANY_CAR as menu
join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as pro on menu.CAR_TYPE=pro.CAR_TYPE
join CAR_RENTAL_COMPANY_RENTAL_HISTORY as his on his.CAR_ID=menu.CAR_ID
where menu.CAR_TYPE in ('세단','SUV')
and pro.DURATION_TYPE='30일 이상'
group by menu.CAR_ID
having max(his.END_DATE)<='2022-11-01'
and FEE BETWEEN 500000 AND 2000000
order by FEE desc, CAR_TYPE , CAR_ID desc
