/*job_gradesjobsjob_gradesemployeesemp_details_viewcountrieslocations*/
/*
SELECT *
FROM employees;
SELECT 컬럼이름, 컬럼이름,,,,
FROM 테이블 또는 뷰(물리적인 테이블에서 뽑아낸 가상의 테이블)
WHERE 조건절
GROUP BY
ODERY BY 순서*/


/* SELECT DEPARTMENT_ID, AVG(salary)
FROM employees
GROUP BY DEPARTMENT_ID; */

SELECT FIRST_NAME
FROM employees
ORDER BY FIRST_NAME ASC;

SELECT FIRST_NAME  
FROM employees
ORDER BY FIRST_NAME DESC;

SELECT FIRST_NAME
FROM employees
WHERE EMPLOYEE_ID = 103;

SELECT 5*6
FROM DUAL;
/*더미 테이블 DUAL*/

/*급여가 5000이상 10000미만인 사원의 이름과 급여를 출력하시요.*/
SELECT  FIRST_NAME, salary
FROM employees
WHERE salary>5000 AND salary<10000;


SELECT  FIRST_NAME, salary
FROM employees
WHERE salary BETWEEN 5000 AND 10000;
/*BETWEEN은 작은수가 먼저 나와야하고, =이 포함된다.*/
SELECT  FIRST_NAME, salary
FROM employees
WHERE salary BETWEEN 5000 AND 1000;

SELECT FIRST_NAME
FROM employees;

/*종류구하기, 중복제외시키기*/
SELECT DISTINCT FIRST_NAME
FROM employees;

/*AS를 통해 이름을 바꿀 수 있다.*/
SELECT FIRST_NAME AS "사원이름"
FROM employees;

SELECT FIRST_NAME AS 사원이름
FROM employees;

SELECT FIRST_NAME  사원이름
FROM employees;

SELECT FIRST_NAME  '사원 이름'
FROM employees;

/*% : 1번 이상 나올수 있고, 안나와도 됨*/
/*_ : 반드시 나와야되고 1번만 옴*/
SELECT FIRST_NAME
FROM employees
WHERE FIRST_NAME LIKE '%J%';


SELECT FIRST_NAME
FROM employees
WHERE FIRST_NAME LIKE '%a_';  /*오라클의 LIKE문의 경우는 대소문자 구분함.*/
                              /*MySQL의 LIKE문의 경우는 대소문자 구분함.*/


/*정렬은 안적어주면 ASC(오름차순)*/
SELECT FIRST_NAME
FROM employees
ORDER BY FIRST_NAME ASC;

SELECT FIRST_NAME
FROM employees
ORDER BY FIRST_NAME DESC;

SELECT FIRST_NAME, LAST_NAME
FROM employees
ORDER BY FIRST_NAME, LAST_NAME ASC;  /*FIRST_NAME이 같으면 LAST_NAME으로 정렬하게 됨.*/

/*1. FIRST_NAME에 A가 들어가는 사원들의 이름을 출력하시요.*/
SELECT FIRST_NAME
FROM employees
WHERE FIRST_NAME LIKE '%a%';

/*이름과 월급을 출력하는데 월급이낮은 사원부터 높은 사원순으로 출력*/
SELECT  FIRST_NAME, salary
FROM employees
ORDER BY salary;

/*join연습하기
사원번호가 110인 사원의 FIRST_NAME과 부서이름(DEPARTMENT_NAME)을 출력*/
SELECT  e.FIRST_NAME, d.DEPARTMENT_NAME
FROM employees E, departments D  /*테이블이름을 할때는 as를 붙이지 않는다. */
WHERE E.employee_id = 110
	AND E.department_id = D.department_id;

SELECT  employees.FIRST_NAME, departments.DEPARTMENT_NAME
FROM employees, departments /*테이블이름을 할때는 as를 붙이지 않는다. */
WHERE employees.employee_id = 110
	AND employees.department_id = departments.department_id;
	
	
/*department_id에 현재 null이 있어 검색결과에 null이 들어가면 오류가 나므로 outer join을 한다*/

/*모든인 사원의 FIRST_NAME과 부서이름(DEPARTMENT_NAME)을 출력*/
SELECT  e.FIRST_NAME, d.DEPARTMENT_NAME
FROM employees E, departments D  
WHERE E.department_id = D.department_id;  /*107명이나 null 때문에 106명이 보이는 문제가 생긴다. join하는 컬럼에 null값이 잇음, outer join으로 행결해야함*/


/*사원번호 1-8번인 사원의 이름과 사수의 이름, 사수의 사원번호를 출력해라*/
/*self join : 테이블을 선언할 때 반드시 익명을 써야함.*/
SELECT E1.FIRST_NAME AS "사원이름", E2.manager_id, E2.FIRST_NAME AS "사수이름"
FROM employees E1, employees E2
WHERE E1.employee_id = 108
	AND E1.manager_id = E2.employee_id;


/*FIRST_NAME에 Z가 들어가는 사원의 이름과 부서이름을 출력하시오*/
SELECT employees.FIRST_NAME, Departments.DEPARTMENT_NAME
FROM employees, departments 
WHERE employees.FIRST_NAME LIKE '%z%'
	AND employees.department_id = departments .department_id;


/*부서이름(CITY)이 'TORONTO'인 사원의 이름 부서이름을 출력하시오*/
SELECT employees.first_name, departments.DEPARTMENT_NAME
FROM employees, departments, locations
WHERE locations.city = "TORONTO"
	AND employees.department_id = departments.department_id
	AND departments.location_id = locations.location_id;
	
	
/*트랜잭션*/
JOIN 많이하면 LOCK 만아져서 처리속도가 느려진다.*/


/**/
SELECT FIRST_NAME
FROM employees
WHRER department_id IS NULL; /* WHERE department_id = NULL 나오지 않음*/
WHRER department_id IS NOT NULL; /*맞다 아니라를 is, is not;*/

SELECT First_NAME, commission_PCT
FROM employees
WHERE commission_PCT IS NOT NULL;

/*모든 사원의 급여와 상여금(salary * commission_PCT)을 출력하시오*/
SELECT first_name, salary, salary * commission_PCT
FROM employees;
/*결과값에 null이 등장하는 문제가 생긴다.*/

SELECT first_name, salary, salary * IFNULL(commission_PCT,0)
FROM employees;


SELECT first_name, department_id
FROM employees
WHERE department_id!=20;


/*부서의 (CITY)가 'TORONTO'인 사원의 이름 부서이름을 출력하시오(서브쿼리를 사용)*/
SELECT employees.first_name, departments.DEPARTMENT_NAME
FROM employees, departments
WHERE employees.department_id = departments.department_id
	AND departments.location_id = (SELECT location_id          
      	                        FROM locations
      	                        WHERE city = "toronto"
											 );
							
/*모든 사원의 first_name과 부서이름(department_name)을 출력
ANSI SQL으로 해결해야함*/
SELECT E.first_name, D.department_name
FROM employees E JOIN departments D
	ON E.department_id = D.department_id;	
	
	
/*평균급여보다 많이 받는 사원의 이름과 급여 출력*/
/*AVG(salary)  : 함수들은 자동으로 null을 뺀다.*/
SELECT E.first_name, E.salary
FROM employees E
WHERE salary > (SELECT AVG(salary)     /*에러 : WHERE salary >AVG(salary);*/
               FROM employees);                                              


/*'Ernst'(LAST_NAME)의 급여와 동일하거나 더 많이 받는 사원의 이름(LAST_NAME)과 급여를 출력하시오(서브쿼리)*/
SELECT LAST_NAME, salary
FROM employees
WHERE salary >= (SELECT salary
                FROM employees
                WHERE LAST_NAME = 'Ernst');
                
/*위의 문제를 join으로 풀어보자.(self join을 이용한다.)*/
SELECT E2.LAST_NAME, E2.salary
FROM employees E1, 	employees E2				
WHERE E1.last_name = 'Ernst'
	AND E1.salary <= E2. salary;  							
							
/*부서번호가 30인 부서에 근무하는 사원들의 이름(last_name), 부서위치(city), 직업(job_title)을 출력하자*/
SELECT e.last_name, l.city, j.job_title
FROM employees e, departments d, jobs j, locations l
WHERE e. department_id = 30
      AND e.department_id = d.department_id
      AND d.location_id = l.location_id
		AND e.job_id = j.job_id;
		
		
SELECT COUNT(*)     
FROM employees
WHERE DEPARTMENT_ID = 30;

/*직급(job_title)이 'accountant', 'programmer'도 아닌 사람을 출력하시오*/

SELECT e.last_name, j.job_title
FROM employees e, jobs j
WHERE e.job_id = j.job_id
   AND j.job_title != 'accountant' 	
	AND j.job_title <> 'programmer';	   

/* -- != 과 <>은 모두 아니다 라는 뜻이다. */
	
/*교재P.164 IN  하위질의  OR의 개념이다.*/

SELECT e.last_name, j.job_title
FROM employees e, jobs j
WHERE e.job_id = j.job_id
   AND j.job_title NOT IN('accountant', 'programmer'); 		
	
SELECT FIRST_NAME
FROM employees
ORDER BY FIRST_NAME;

/*my_SQL은 사이 값을 읽어내기 위한 limit이 있지만,
오라클은from절의 서브인 인라인뷰를 2번써야함.*/ 	
	
SELECT FIRST_NAME
FROM employees LIMIT 5,3;	


/*LIMIT은 orderby의 뒤에 나와야 하고, 0부터 시작한다., */	
SELECT FIRST_NAME
FROM employees	
ORDER BY FIRST_NAME
LIMIT 5,3;	

	
/*outer join : 조인할 때 null값이 안보이는 현상 */
/*모든 사원의 first_name과 부서이름(department_name)을 출력
ANSI SQL으로 해결해야함*/
SELECT E.first_name, D.department_name
FROM employees E JOIN departments D
	ON E.department_id = D.department_id;	

/*모든 사원(107명)의 first_name과 부서이름(department_name)을 출력을 원하였으나 106명만 출력됨.
ANSI SQL으로 해결하거나 outer join으로 해결한다.*/
SELECT E.first_name, D.department_name
FROM employees E JOIN departments D
	ON E.department_id = D.department_id;	
	
	
/*oracle에서	*/
SELECT E.first_name, D.department_name
FROM employees E JOIN departments D
	ON E.department_id = D.department_id(+);
	
/*My SQL에서*/	
SELECT E.first_name, D.department_name
FROM employees E LEFT OUTER JOIN  departments D
	ON E.department_id = D.department_id;
	
SELECT E.first_name, D.department_name
FROM employees E LEFT JOIN  departments D   /*OUTER 생략가능, null의 위치를 left, right로 표시한다.*/
	ON E.department_id = D.department_id; 

SELECT E.first_name, D.department_name
FROM employees E right JOIN  departments D   /*OUTER 생략가능, null의 위치를 left, right로 표시한다.*/
	ON E.department_id = D.department_id; 
	
/*full outer join*/	
UNION
SELECT E.first_name, D.department_name
FROM employees E right JOIN  departments D   /*OUTER 생략가능, null의 위치를 left, right로 표시한다.*/
	ON E.department_id = D.department_id; 
/*PRIMARY KEY과 FK가있으면, PK에서는 NULL 허용하지 않는다.*/

/* KEY가 없으면 INDEX 달아서 B*TREE(balance)라는 자료구조를 사용한다.
이 방법은 속도를 빠르게 해준다.별도의 테이블을 만들어준다.삽입삭제가 일어나면 B*TREE를 쓸 수 없다*/

/*나중을 대비해서 outer join을 해줘야한다.*/

/*모든 사원의 이름(last_name), 부서위치(city), 직급(job_title)을 출룍하시오*/
SELECT e.last_name, l.city, j.job_title
FROM employees e, departments d, jobs j, locations l
WHERE e.department_id = d.department_id
      AND d.location_id = l.location_id
		AND e.job_id = j.job_id;              /*결과값 106개*/
		
SELECT e.last_name, l.city, j.job_title
FROM employees e
LEFT join departments d
ON e.department_id = d.department_id
join locations l
on d.location_id = l.location_id
join jobs j
on e.job_id = j.job_id;                     /*결과값 106개*/
	
		
SELECT e.last_name, l.city, j.job_title
FROM employees e
LEFT join departments d
ON e.department_id = d.department_id
LEFT join locations l
on d.location_id = l.location_id
LEFT join jobs j
on e.job_id = j.job_id;		                 /*결과값 107개*/
		
SELECT e.last_name, l.city, j.job_title
FROM employees e
LEFT join departments d
ON e.department_id = d.department_id
LEFT join locations l
on d.location_id = l.location_id
join jobs j
on e.job_id = j.job_id;	                   /*결과값 107개*/


SELECT e.last_name, l.city, j.job_title
FROM employees e LEFT JOIN(departments d, jobs j, locations l)
on e.department_id = d.department_id
      AND d.location_id = l.location_id
		AND e.job_id = j.job_id;             /*결과값 107개*/
		
		
/*mySQL은 대소문자를 구분하지 않는데, 이를 보완하고자 cast(as binary)를 사용하면 된다.*/
SELECT  e.FIRST_NAME, d.DEPARTMENT_NAME
FROM employees E, departments D  
WHERE BINARY(First_name) LIKE '%A%'
	AND E.department_id = D.department_id;
	
SELECT  e.FIRST_NAME, d.DEPARTMENT_NAME
FROM employees E, departments D  
WHERE First_name LIKE BINARY '%A%'
	AND E.department_id = D.department_id;
	
SELECT  e.FIRST_NAME, d.DEPARTMENT_NAME
FROM employees E, departments D  
WHERE cast(First_name as BINARY) like '%A%'
	AND E.department_id = D.department_id;
	
	
	/*서브쿼리의 종류  1. from절 뒤에 쓰이면, 임시로 만드는 뷰가 된다.2. IN*/
	
SELECT e.last_name, j.job_title, j.MIN_SALARY
FROM employees e, jobs j
WHERE e.job_ID = j.job_ID
      AND j.job_TITLE IN(SELECT JOB_TITLE
      							FROM JOBS
      							WHERE MIN_SALARY > 7000);
      							

/*사원의 이름(last_name)이 'Abel'인 사원과 같은 부서에 근무하는 사원의 이름과 부서번호를 출력하시요.(self join 사용) */
SELECT E2.LAST_NAME, E2.department_id
FROM employees E1, EMPLOYEES E2
WHERE E1.LAST_NAME = 'Abel'
	AND E1.department_id = E2.department_id;
	
/* null이 있기 때문에 outer-join을 이용해야한다.*/
SELECT E2.LAST_NAME, E2.department_id
FROM employees E1 LEFT OUTER EMPLOYEES E2
	ON  E1.department_id = E2.department_id
	WHERE E1.LAST_NAME = 'Abel';
	
/*ABLE이 들어가버린다. ABLE은 빼야함.*/	
SELECT E2.LAST_NAME, E2.department_id
FROM employees E1 LEFT join EMPLOYEES E2
	ON  E1.department_id = E2.department_id
	WHERE E1.LAST_NAME = 'Abel'
   AND E1.LAST_NAME != E2.LAST_NAME;



/*INSERT문 : 테이블(뷰)에 데이터를 입력 -> 데이터컬럼의 순서는 중요.데이터는 컬럼순으로 추가한다.
				 insert시에는 꼭 컬럼의 제약조건을 확인해야한다.
				 VARCHAR순서대로 가변길이 문자열, DECIMAL소숫점 있을 수 있음.
             PK는 중복되서는 안되는데, PK가 저절로 +1이 되면 좋다. (자동증가OUTO_INCREMENT를 하면 INSERT시에 해당 key를 입력해줄 필요가 없다.)
             null허용 여부, null이 혀용된 컬럼의 값에 대해서는 꼭 outer join을 해야함.
UPDATE : 테이블의 값을 수정
DELETE : 테이블의 값을 삭제
update와 delete의 경우, 위치지정을 하지 않으면 컬럼 전체가 사라지거나 수정되어 버린다.*/

/*INSERT INFO테이블 이름(컬럼명, 컬럼명,...) VALUES(값, 값,...)
  INSERT INFO 테이블 이름 VALUES(값, 값,...)
특정 컬럼값만 적고 값을 주면, 나며지 컬럼은 null이 들어가고 만약 null이 허용되지 않으면 에러가 뜬다.
보통은 컬럼명을 다 적지 않고,값에 null을 넣어 사용한다.*/

/*
UPDATE 테이블
SET  컬럼명=값, 컬럼명 =값,...
WHERE..*/

/*id를 쓰는 이유는 이름을 바꿀 때마다 모든 테이블마다 바꿔으므로 pk별로 따로 테이블을 만드는 것이 좋다.
그리고id값이 테이블에 없으면 에러가 도출이 되어준다.*/

/*
DELETE
From 테이블명
where *
*/

/*내가 수정, 삭제, 업데이트는 바로 테이블에 적용되지 않는다. 임시테이블에 적용되기 때문에  COMMIT  것을 통해 영구히 테이블에 적용시키도록 한다.
commit을 하기 전에 임시테이블에 적용된 내용은  rollback하면 원상복귀 된다.*/

/*그런데 mySQL은 autocommit을 해버린다.이를 못하게 하고자 아래의 쿼리를 준다
SELECT @@AUTOCOMMIT;
SET autocommit = TRUE;
SET autocommit = FALSE; */

SELECT @@AUTOCOMMIT;
SET autocommit = FALSE;

/*참조무결성조건에 의해 FK가매칭되지 않으면 에러가 뜬다.*/

INSERT INTO employees
VALUES(300,'A', 'A', 'A', 'A', '2011-01-01', 'AD_VP', 8000, NULL, 111, 80);

ROLLBACK;

/*secure coding을 해야한다.이를 하지 않으면 쿼리문을 해석해서 아이디 비번을 빼낼 수 있게되어버린다.*/

UPDATE employees
SET  FIRST_NAME='bbbB', LAST_NAME ='45454352'
WHERE EMPLOYEE_ID = 300;

DELETE
From employees
WHERE EMPLOYEE_ID = 300;  /*특정한 하나의 레코드만 삭제되도록 where절을 준다.*/
/*삭제시 참조되어 있으면, delete가 안된다.*/


COMMIT;

/*DDL : CREATE(계정, 테이블을 만들자), ALTER(계정, 테이블을 수정하자),  DROP(계정, 테이블을 삭제하자)*/
/*BBS 테이블 만들기*/
/*COMMENTS 테이블 만들기*/
create Table BBS(
  Article_num INT AUTO_INCREMENT PRIMARY KEY, 
  WRITER_ID VARCHAR(30) NOT NULL,
  TITLE VARCHAR(2	00) NOT NULL,
  CONTENTS VARCHAR(10000) NOT NULL,
  WRITE_DATE DATE NOT NULL  #년월일
  );
 
 create Table BBS(
  Article_num INT AUTO_INCREMENT PRIMARY KEY, 
  WRITER_ID VARCHAR(30) NOT NULL,
  TITLE VARCHAR(200) NOT NULL,
  CONTENTS VARCHAR(10000) NOT NULL,
  WRITE_DATE DATETIME NOT NULL #년월일시분초
  ); 
  
create Table COMMENTS1(
  COMMENT_num INT AUTO_INCREMENT PRIMARY KEY, 
  WRITER_ID VARCHAR(30) NOT NULL,
  CONTENT VARCHAR(1500) NOT NULL,
  Article_num INT NOT NULL,  
  CONSTRAINT FOREIGN KEY(Article_num)
  REFERENCES bbs(Article_num)
  );
  
create Table COMMENTS(
  COMMENT_num INT AUTO_INCREMENT PRIMARY KEY, 
  WRITER_ID VARCHAR(30) NOT NULL,
  CONTENT VARCHAR(1500) NOT NULL,
  Article_num INT NOT NULL,  
  CONSTRAINT comments_ARTICLE_NUM_FK FOREIGN KEY(Article_num)
  REFERENCES bbs(Article_num)
  );  
  
SELECT NOW();  #쿼리문 수행시 무조건 그 시간이 잡힘.
SELECT SYSDATE(); 
SELECT CURRENT_TIMESTAMP();  #내장함수
SELECT CURRENT_TIMESTAMP;     #함수 : MYSQL이 가지고 있음. #SLEEP으로 쓰레드를 줘서 딜레이는 시켜서 시간이 잡힘.

SELECT NOW(), sleep(5), CURRENT_TIMESTAMP(), SYSDATE();  ##DB에 저장될때 시간이 될 수 있도록 SYSDATE를 사용.
  
INSERT INTO bbs VALUES(NULL, 'A', 'A', 'A', NOW());  
INSERT INTO bbs VALUES(NULL,'A', 'A', 'A', sysdate());  
  
INSERT INTO comments VALUES(NULL,'A', 'A', 2);  ##bbs의 2번 글은 참조가 되었기에  삭제(drop)할 때 에러가 난다.
  
DROP TABLE bbs;
DROP TABLE comments;  #테이블 없애기 

 SELECT * FROM EMPLOYEES;

/*뷰 만들기
로그인과 관련하여 뷰를 아이디 비번만 불러오도록 만들거나, 반복해서 쓰이는 셀렉트문을 뷰로 만들어둔다.
테이블에서 뷰를 만들고, 뷰에서 뷰를 만들 수 있다. 
뷰를 바꾸면 뷰 앞단계의 뷰와 테이블도 변경되게 되어 부하가 걸린다.그래서 뷰 생성 권한 계정마다 제한적으로 준다*/

CREATE OR REPLACE VIEW EMP #없으면 새로 만들고, 있으면 대체하자.
AS SELECT FIRST_NAME, LAST_NAME, SALARY
FROM employees;

CREATE OR REPLACE VIEW emp1 #값은 필요없고 틀만 필요한 경우.
AS SELECT FIRST_NAME, LAST_NAME, SALARY
FROM employees
where 1=2;

DROP VIEW emp1;

/*계정만들기 : root계정에 들어가서 
root 계정으로 접속, hr 데이터베이스 생성, hr 계정 생성 
MySQL Workbench에서 초기화면에서 +를 눌러 root connection을 만들어 접속한다. 

DROP DATABASE IF EXISTS hr;
DROP USER IF EXISTS  hr@localhost;
create user hr@localhost identified by 'hr';
create database hr;
grant all privileges on hr.* to hr@localhost with grant option;*/
  
/*프로그래머스쿨 https://school.programmers.co.kr/learn/courses/30/lessons/164673*/


/*오라클은 내가 원하는 값만큼을 증가시킬 수 있으나 mySQL은 1씩만 증가한다.*/
# select @@OUTO_INCREMENT_INCREMENT;
# set @@OUTO_INCREMENT_INCREMENT = 10;


# 제약조건 이름 확인 할 수 있는 방법(view로 TABLE_CONSTRAINTS을 불러온다)
SELECT*
FROM information_schema.TABLE_CONSTRAINTS;



/*시간을 연산해보면 밀리초로 단위가 나온다.*/
SELECT NOW()-HIRE_DATE
FROM employees;


SELECT CONCAT(FIRST_NAME, '는')
FROM employees;
 
SELECT CONCAT(CONCAT(CONCAT(FIRST_NAME, '는'), SALARY),'입니다');

#DATEDIFF(일수로 나옴)
SELECT DATEDIFF(NOW(), HIRE_DATE)
FROM employees; 

/*SUBSTR*/
SELECT FIRST_NAME, SUBSTR(FIRST_NAME, 2)
FROM employees; 

SELECT FIRST_NAME, SUBSTR(FIRST_NAME, 2,2)
FROM employees; 


/*REPLACE*/
SELECT FIRST_NAME, REPLACE(FIRST_NAME, 'ex','AAAAAAAA')  #대소문자 구분함.
FROM employees; 
SELECT FIRST_NAME, REPLACE(FIRST_NAME, 'Ex','AAAAAAAA')  #대소문자 구분함.
FROM employees; 


/*모든 사원의 근무년수를 출력하시오(년수만 나오게) TRUNCATE(버리는 함수, 나머지를 잘라내버림), CONCAT사용 출력형태 : 25년*/
SELECT CONCAT(TRUNCATE(DATEDIFF(NOW(), HIRE_DATE)/365,0), '년')  
FROM employees;


/*모든 사원의 근무년수를 제외한 개월을 출력하시오 MOD(나머지를 구함), CONCAT사용 출력형태 : 25개월*/
SELECT CONCAT(TRUNCATE(MOD(DATEDIFF(NOW(), HIRE_DATE),365)/30,0), '개월')  
FROM employees;


/**/
SELECT FIRST_NAME, SALARY, CASE WHEN JOB_ID ='IT_PROG' THEN SALARY*1.1 
                                WHEN JOB_ID ='ST_MAN' THEN SALARY*1.2
									     WHEN JOB_ID ='SA_MAN' THEN SALARY*1.3
									     ELSE SALARY
									END AS '보너스 포함'
FROM employees;		

SELECT FIRST_NAME, SALARY, CASE JOB_ID WHEN 'IT_PROG' THEN SALARY*1.1 
                                       WHEN 'ST_MAN' THEN SALARY*1.2
									            WHEN 'SA_MAN' THEN SALARY*1.3
									            ELSE SALARY
									END AS '보너스 포함'
FROM employees;

/*COUNT함수*/
SELECT COUNT(*)
FROM employees; ##107명

SELECT COUNT(DEPARTMENT_ID)
FROM employees;    ##106명 : 집합함수는 NULL은 제외해버림.

/*사원들의 FIRST_NAME의 총 갯수*/
SELECT COUNT(DISTINCT(DEPARTMENT_ID))
FROM employees;  ##11가지


SELECT SUM(SALARY)
FROM employees;

SELECT AVG(SALARY)
FROM employees;

SELECT MAX(SALARY)
FROM employees;

SELECT MIN(SALARY)
FROM employees;

SELECT AVG(SALARY)
FROM employees
WHERE DEPARTMENT_ID =30;

/*Mysql group함수
특정 속성(ATTRIBUTE, 애트리뷰트)의 값이 같은 튜플을 모아 그룹을 만들어 그룹별 검색
SELECT절에는 그룹으로 묶은 속성과 그룹함수만 사용가능
HAVING을 사용하여 GROUP BY절의 조건 작성*/

# 다른 값을 하려면 값의 매칭이 다르기 떄문에 에러가 난다.아래는 예시이다.
SELECT first_name, AVG(SALARY)
FROM employees
GROUP BY DEPARTMENT_ID;   #에러

/*해결을 위해서는 */
SELECT first_name, AVG(SALARY)
FROM employees
GROUP BY first_name;

SELECT DEPARTMENT_ID, AVG(SALARY)
FROM employees
GROUP BY DEPARTMENT_ID;   # 그륩함수는 NULL 알아서 처리한다.

SELECT AVG(SALARY)
FROM employees
GROUP BY DEPARTMENT_ID;



SELECT first_name,DEPARTMENT_ID, AVG(SALARY)
FROM employees
GROUP BY first_name,DEPARTMENT_ID;

SELECT first_name,DEPARTMENT_ID, AVG(SALARY)
FROM employees
GROUP BY DEPARTMENT_ID;   #에러



/*WHERE조건절에  그룹함수를 바로 쓰면 에러가 나므로 서브쿼리를 써야한다. */
SELECT first_name
FROM employees
WHERE SALARY > AVG(SALARY);  #에러 ->서브 쿼리를 써야함.

SELECT first_name
FROM employees
WHERE SALARY > (SELECT AVG(SALARY)
                FROM employees
                );



#아래 두개 쿼리는 같지만, where절은 그룹함수를 쓰지 못하기 때문에 
SELECT DEPARTMENT_ID, AVG(SALARY)
FROM employees
WHERE DEPARTMENT_ID=30
GROUP BY DEPARTMENT_ID;

SELECT DEPARTMENT_ID, AVG(SALARY)
FROM employees
GROUP BY DEPARTMENT_ID
HAVING DEPARTMENT_ID=30;
 
/*부서인원이 5인 이상인 부서의 평균급여를 구하시오*/
SELECT DEPARTMENT_ID, COUNT(DEPARTMENT_ID) AS  "부서인원", AVG(SALARY)   #AS가 없어도 되고, 띄어쓰기가 없다면 ""도 필요없다.
FROM employees
GROUP BY DEPARTMENT_ID
HAVING COUNT(*)>=5;


/*멘티(부하)직원이 1명인 사수(멘토)의 사원번호 검색(사수가 없는 사원은 제외)*/
SELECT manager_id, COUNT(*)
FROM employees
WHERE manager_id IS NOT null
GROUP BY manager_id 
HAVING COUNT(*)=1;


#USE HR:


# --root계정으로 들어가기
CREATE USER 'HUMAN'@'LOCALHOST' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON HR.* TO 'HUMAN'@'LOCALHOST';


ALTER USER 'HUMAN'@'LOCALHOST' IDENTIFIED BY '0000';  ##비번변경

DROP USER 'HUMAN'@'LOCALHOST';  ##사용자 계정 없애기



##인덱스 쓰기.

CREATE INDEX EMP_IDX ON employees(First_name);

SHOW INDEX FROM employees;

###########################################################################################################################

#예제 풀기#
/*테이블 생성*/
 create Table SCHOOL(
  NUM INT AUTO_INCREMENT PRIMARY KEY, 
  NAME VARCHAR(50) NOT NULL,
  AREA VARCHAR(20) NOT NULL,
  COURSE_CNT INT NOT NULL,
  C_DATE DATETIME NOT NULL 
  ); 
  
  
 create Table COURSE01(
  NUM INT AUTO_INCREMENT PRIMARY KEY, 
  SCHOOL_NUM INT NOT NULL,
  NAME VARCHAR(15) NOT NULL,
  STUDENT_CNT INT NOT NULL,
  C_DATE DATETIME NOT NULL 
  ); 

/*테이블 입력*/
INSERT INTO SCHOOL VALUES('1', '서울대학교', '서울', '35', '80/07/01');
INSERT INTO SCHOOL VALUES('2', '중앙대학교', '서울', '27', '81/08/01');
INSERT INTO SCHOOL VALUES('3', '동아대학교', '부산', '32', '82/09/01');
INSERT INTO SCHOOL VALUES('4', '부산대학교', '부산', '21', '83/10/01');

INSERT INTO COURSE01 VALUES(NULL, '4', 'IT', '50', '00/07/09') ;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              , '00/07/09');
INSERT INTO COURSE01 VALUES(NULL, '3', '경영', '60', '10/01/01');
INSERT INTO COURSE01 VALUES(NULL, '2', '식품영양', '70', '09/03/01');
INSERT INTO COURSE01 VALUES(NULL, '1', '화학', '80', '08/05/01');
 

DROP TABLE SCHOOL;

/*학교명과 지역에 '서울'이란 단어가 들어가는 학교 조회*/
SELECT *
FROM SCHOOL
WHERE NAME LIKE '%서울%' AND AREA LIKE '%서울%';

/*설립일자 중 월이 '08'인 학교 조회 (date_format(), %M  )*/
SELECT *
FROM SCHOOL
WHERE DATE_FORMAT(C_DATE, '%m') = '08';

/*2009년 4월 이전에 개강된 과정 조회*/
SELECT *
FROM COURSE01
WHERE DATE_FORMAT(C_DATE, '%y/%m/%d') < '09/04/01';


/*개강일자를 YYY-MM-DD형식으로 조회*/
SELECT DATE_FORMAT(C_DATE, '%Y-%m-%d')
FROM COURSE01;

/*학교번호가 1이면 서울대학교, 2이면 중앙대학교, 3이면 동아대학교, 4이면 부산대학교로 바꿔서 조회(CASE문)*/
SELECT CASE NUM  WHEN '1' THEN '서울대학교'
                 WHEN '2' THEN '중앙대학교'
                 WHEN '3' THEN '동아대학교'
                 WHEN '4' THEN '부산대학교'
                 END 
                 AS '별칭'
FROM SCHOOL;

/**/
create table emp2 (
	empno int,
	ename varchar(10),
	job varchar(9),
	mgr int,
	hiredate datetime,
	sal int,
	comm int,
	deptno tinyint,
	primary key(empno),
	constraint fk_emp_dept
	foreign key(deptno) references dept(deptno)
	on delete CASCADE
	);