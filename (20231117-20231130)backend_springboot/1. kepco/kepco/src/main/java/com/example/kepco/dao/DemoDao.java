package com.example.kepco.dao;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate; //application.properties에 설정필요

import org.springframework.stereotype.Repository;

@Repository
public class DemoDao {

    @Autowired
    JdbcTemplate jt;

    public List<Map<String, Object>> select() {  //여러값을 가져오므로 LIST형태에 값은 MAP 형태
        return jt.queryForList("select * from demo");
    }

    // public static void insert(){
    //     String sqlSmt="insert into demo demo(seq, user) values(3,'CCC')";
    //     jt.execute(sqlSmt);
    // }

    public void insert(String seq, String user){
    String sqlStmt=String.format("insert into demo(seq, user) values(%s,'%s')",seq, user);
    jt.execute(sqlStmt);
    }

    public List<Map<String, Object>> maxSeqSelect(){
        String sqlStmt="select max(seq) as seq from demo";
        return jt.queryForList(sqlStmt);
    }

    public List<Map<String, Object>> totalCount(){
        String sqlStmt="select count(*) as cnt from domo";
        return jt.queryForList(sqlStmt);
    }

}
