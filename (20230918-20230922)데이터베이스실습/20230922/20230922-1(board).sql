/*테이블 생성*/
CREATE TABLE BOARD (
 SEQ_NO INT
 , TITLE VARCHAR(50)
 , CONTENT VARCHAR(100)
 , CODE VARCHAR(1)
);
INSERT INTO BOARD VALUES (1, '첫번째 공지사항', '공지사항 입니다', 'N');
INSERT INTO BOARD VALUES (2, '첫번째 FAQ', 'FAQ 입니다', 'F');
INSERT INTO BOARD VALUES (3, '첫번째 자료', '자료실 입니다', 'D');
INSERT INTO BOARD VALUES (4, '첫번째 QnA', 'QnA 입니다', 'Q');
INSERT INTO BOARD VALUES (5, '1번 게시글', '1번 게시글입니다', 'A');
INSERT INTO BOARD VALUES (6, '2번 게시글', '두번째 게시글입니다', 'A');


CREATE TABLE BOARD_CODE (
 CODE VARCHAR(1)
 , CODE_EXP VARCHAR(100)
 , USE_YN VARCHAR(1)
);
INSERT INTO BOARD_CODE VALUES ('N', '공지사항', 'Y');
INSERT INTO BOARD_CODE VALUES ('F', 'FAQ', 'Y');
INSERT INTO BOARD_CODE VALUES ('D', '자료실', 'N');
INSERT INTO BOARD_CODE VALUES ('Q', 'QnA', 'Y');
INSERT INTO BOARD_CODE VALUES ('A', '일반게시판', 'Y');


CREATE TABLE BOARD_FILE (
 FILE_SEQ_NO INT
 , BOARD_SEQ_NO INT
 , FILE_NAME VARCHAR(50)
 , FILE_SIZE INT
);
INSERT INTO BOARD_FILE VALUES (1, 1, '공지사항.hwp', 12345678);
INSERT INTO BOARD_FILE VALUES (2, 2, 'FAQ자료.zip', 10000000);
INSERT INTO BOARD_FILE VALUES (3, 5, 'readme.txt', 1000);


/*쿼리문 연습*/
# BOARD 와 BOARD_CODE 테이블 CODE를 기준으로 조인
SELECT board.SEQ_NO, board.TITLE, board.CONTENT, board.CODE, BOARD_CODE.CODE_EXP
FROM board join board_code
ON board.CODE = BOARD_CODE.CODE;

SELECT board.SEQ_NO, board.TITLE, board.CONTENT, BOARD_CODE.CODE, BOARD_CODE.CODE_EXP
FROM board join board_code
ON board.CODE = BOARD_CODE.CODE;

#BOARD 와 BOARD_CODE 테이블 CODE를 기준으로 조인하면서 게시판 구분 코드가 Q인 레코드는 제외하여 조회
SELECT board.SEQ_NO, board.TITLE, board.CONTENT, BOARD_CODE.CODE, BOARD_CODE.CODE_EXP
FROM board join board_code
ON board.CODE = BOARD_CODE.CODE
where board_code.code != 'Q';

#BOARD 와 BOARD_CODE 테이블 CODE를 기준으로 조인하면서 게시판 사용여부가 ‘Y’ 인 레코드만 조회
SELECT board.SEQ_NO, board.TITLE, board.CONTENT, BOARD_CODE.CODE, BOARD_CODE.CODE_EXP
FROM board join board_code
ON board.CODE = BOARD_CODE.CODE
where board_code.USE_YN = 'Y';


#BOARD 테이블 SEQ_NO와 BOARD_FILE 테이블 BOARD_SEQ_NO LEFT OUTER 조인
select *
FROM board B LEFT OUTER join board_file BF  #outer 생략가능
ON b.seq_no = bf. board_seq_no;

select *
FROM board B LEFT join board_file BF  #outer 생략가능
ON b.seq_no = bf. board_seq_no;
