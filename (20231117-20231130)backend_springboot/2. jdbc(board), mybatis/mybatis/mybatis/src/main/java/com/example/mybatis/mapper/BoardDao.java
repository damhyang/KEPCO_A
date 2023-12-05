package com.example.mybatis.mapper;

import java.util.*;

import org.apache.ibatis.annotations.Mapper;

@Mapper
//메소드들만 적어주면 됨
public interface BoardDao {
    public List<Map<String,Object>> selectList();
    public List<Map<String,Object>> selectDetail(String seq);
    public void insertBoard(String title, String content, String writer, String writeDate);
    public void updateBoard(String seq, String title, String content, String writeDate);
}
