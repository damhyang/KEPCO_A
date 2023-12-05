create table dept (
	deptno tinyint primary key,
	dname varchar(14),
	loc varchar(13)
);


create table emp (
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
	on delete cascade
);

insert into dept values (10, 'accounting', 'new york');
insert into dept values (20, 'research',   'dallas');
insert into dept values (30, 'sales',      'chicago');
insert into dept values (40, 'operations', 'boston');

insert into emp values
        (7369, 'smith',  'clerk',     7902,
        '1980-12-17',  800, null, 20);
insert into emp values
        (7499, 'allen',  'salesman',  7698,
        '1981-02-20', 1600,  300, 30);
insert into emp values
        (7521, 'ward',   'salesman',  7698,
        '1981-02-22', 1250,  500, 30);
insert into emp values
        (7566, 'jones',  'manager',   7839,
        '1981-04-02',  2975, null, 20);
insert into emp values
        (7654, 'martin', 'salesman',  7698,
        '1981-09-28', 1250, 1400, 30);
insert into emp values
        (7698, 'blake',  'manager',   7839,
        '1981-05-01',  2850, null, 30);
insert into emp values
        (7782, 'clark',  'manager',   7839,
        '1981-06-09',  2450, null, 10);
insert into emp values
        (7788, 'scott',  'analyst',   7566,
        '1982-12-09', 3000, null, 20);
insert into emp values
        (7839, 'king',   'president', null,
        '1981-11-17', 5000, null, 10);
insert into emp values
        (7844, 'turner', 'salesman',  7698,
        '1981-09-08',  1500,    0, 30);
insert into emp values
        (7876, 'adams',  'clerk',     7788,
        '1983-01-12', 1100, null, 20);
insert into emp values
        (7900, 'james',  'clerk',     7698,
        '1981-12-03',   950, null, 30);
insert into emp values
        (7902, 'ford',   'analyst',   7566,
        '1981-12-03',  3000, null, 20);
insert into emp values
        (7934, 'miller', 'clerk',     7782,
        '1982-01-23', 1300, null, 10);

COMMIT;



SELECT SUM(E.SAL), D.DNAME
FROM emp E, dept D
WHERE D.LOC IN('new york', 'dallas')
	AND E.deptno = D.deptno
GROUP BY D.DNAME;