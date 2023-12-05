CREATE TABLE board(
	seq bigint NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	title VARCHAR(255),
	content TEXT,
	writer VARCHAR(50)
);

DESC board;

INSERT INTO board(title,content,writer)
	VALUES('test','오늘할일','이강욱');
	
SELECT * FROM board;

SELECT content FROM board WHERE seq=1;

UPDATE board SET title="내일할일", content="식사" WHERE seq=2;

SELECT * FROM board WHERE seq=2;

UPDATE board SET title="변경", content="변경" WHERE seq=3;

ALTER TABLE board ADD COLUMN(search_count INT DEFAULT 1);

SELECT * FROM board;

CREATE TABLE board_answer(
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
seq INT NOT NULL, 
answer VARCHAR(255));
kepcoa
DESC board_answer;

SELECT * FROM board;

INSERT INTO board_answer(seq, answer) VALUES(4, "잘 했습니다");

SELECT * FROM board_answer;

SELECT COUNT(*) AS count FROM board_answer WHERE seq=1;


SELECT * FROM board_answer;

SELECT @@AUTOCOMMIT;

DELETE FROM board_answer;

SELECT * FROM board_answer;

SET AUTOCOMMIT = FALSE;


INSERT INTO board_answer(seq,answer) VALUES(4,"장성호선생님 댓글감사");


SELECT * FROM board_answer;

COMMIT;


DELETE FROM board_answer;

ROLLBACK;

SELECT a.search_count, b.answer FROM board a, board_answer b
WHERE a.seq=b.seq AND a.seq=10;
demo
COMMIT;
SET AUTOCOMMIT = TRUE;

DROP TABLE demo;
CREATE TABLE demo (seq BIGINT PRIMARY KEY,USER VARCHAR(20));

INSERT INTO demo(seq,USER) VALUES(1,'AAA');
INSERT INTO demo(seq,USER) VALUES(2,'BBB');
kepcoa
ALTER TABLE board ADD COLUMN(writer_date VARCHAR(20));

ALTER TABLE board change writ_date write_date VARCHAR(20);board