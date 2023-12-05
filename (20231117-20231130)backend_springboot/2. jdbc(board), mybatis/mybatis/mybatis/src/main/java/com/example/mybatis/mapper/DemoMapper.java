package com.example.mybatis.mapper;

import java.util.*;

import org.apache.ibatis.annotations.Mapper;

//인터페이스
@Mapper //mapper이라고 해야 mapper.xml에서 스캔이 가능.
public interface DemoMapper {
    public List<Map<String, Object>> select();
    public List<Map<String, Object>> selectById(String seq);
    public void insert(String seq, String user);
    public void update(String seq, String user);
    public void delete(String seq);
//select()메소드는 mapper.xml에서 id로 찾아가.ㅁ
}