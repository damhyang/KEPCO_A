package com.example.board.dao;

import java.util.*;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

@Repository //DB임을 알려주는 어노테이션
public class BoardDao {
    @Autowired //bean만드는 방법
    JdbcTemplate jt; //변수선언

    //CRUD만들기

    public List<Map<String, Object>> listSelect(){
        String sqlStmt="select seq, title, writer, search_count from board";
        return jt.queryForList(sqlStmt);
    }

    public void insert(String title, String content, String writer){
        String sqlStmt=String.format("insert into board(title, content, writer) values('%s','%s','%s')",title, content, writer);
        // String sqlStmt = "insert into board(title,content,writer) values('1','2','1')";
        System.out.println(sqlStmt);
        jt.execute(sqlStmt);
    }
    
    public List<Map<String, Object>> detailSelect(String seq){
        String sqlStmt = String.format("select seq, title ,content, search_count from board where seq = %s",seq);
        return jt.queryForList(sqlStmt);
        }

    public void delete(String seq){
        String sqlStmtMain=String.format("delete from board where seq=%s;",seq);
        String sqlStmtDetail=String.format("delete from board_answer where seq=%s;",seq);
        //database에 foreign-key cascading을 해주는게 가장 좋지만, DB는 잘 안건들기 때문에 건들지 않고 하는 방법을 제시함.
        jt.execute(sqlStmtMain);
        jt.execute(sqlStmtDetail);
    }

    public void update(String title, String content,String seq){
        String sqlStmt=String.format("update board set title='%s', content='%s' WHERE seq='%s';",title, content, seq);
        jt.execute(sqlStmt);
    }

    public void updateSearchCount(String seq, String searchCount){
        String sqlStmt=String.format("update board set search_count='%s' WHERE seq='%s';",searchCount,seq);
        jt.execute(sqlStmt);
    }

    public void insertAnswer(String seq, String answer){
        String sqlStmt=String.format("insert into board_answer(seq,answer) values(%s,'%s')",seq,answer);
        jt.execute(sqlStmt);
    }

    public List<Map<String, Object>> getCountAnswer(String seq){
        String sqlStmt = String.format("select answer from board_answer where seq=%s",seq);
        return jt.queryForList(sqlStmt);
    }
}
