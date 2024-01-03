-- 코드를 입력하세요
select concat('/home/grep/src/',type.board_id,'/',type.FILE_ID,type.FILE_NAME,type.FILE_EXT) as FILE_PATH
from USED_GOODS_BOARD ge
join USED_GOODS_FILE type on type.BOARD_ID=ge.BOARD_ID
WHERE views = (SELECT MAX(views) FROM used_goods_board)
order by type.FILE_ID desc
