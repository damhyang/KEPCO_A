package com.example.mybatis.controller;

import java.time.LocalDate;
import java.time.LocalTime;
import java.util.*;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.mybatis.mapper.BoardDao; //heap영역에 있는 것을 static영역으로 불러옴.
// import com.example.mybatis.mapper.DemoMapper;

@RestController //화면에 뿌려줘. 클래스어노테이션
public class DBController {
    // @Autowired
    // DemoMapper demoMapper;
    @Autowired //스프링에 주입, 빈으로 넣는 것.
    BoardDao boardDao;

    // @GetMapping("/mybatis/demo")
    // public List<Map<String,Object>> mybatisDemo(){
    //     return demoMapper.select();
    // }

    // @GetMapping("/mybatis/demoid")
    // public List<Map<String,Object>> mybatisDemoId(){
    //     return demoMapper.selectById("1");
    // }

    // @GetMapping("/mybatis/demoinsert")
    // public String mybatisInsert(){
    //     demoMapper.insert("3", "CCC");
    //     return "잘 저장되었습니다.";
    // }

    // @GetMapping("/mybatis/demoupdate")
    // public String mybatisUpdate(){
    //     demoMapper.update("3", "abc");
    //     return "수정되었습니다.";
    // }

    // @GetMapping("/mybatis/demodelete")
    // public String mybatisDelete(){
    //     demoMapper.delete("3");
    //     return "제거되었습니다.";
    // }

//  아래 주소(/board/list)가 들어오면 DB에 있는 데이터를 가지고 보여줘.
    @GetMapping("/board/list") //메소드 어노테이션 
    public List<Map<String,Object>> boardList(){
        return boardDao.selectList();
    }

    @GetMapping("/board/detail") 
    public List<Map<String,Object>> boardDetail(){
        String seq="9";
        return boardDao.selectDetail(seq);
    }

    @GetMapping("/board/insert") 
    public String boardInsert(){
        String date=LocalDate.now().toString(); //static이라서 new필요없음.
        String time=LocalTime.now().toString().substring(0,5);
        
        String title="오늘 아침 기온";
        String content="매우 추웠음.,. 특히 광주는";
        String writer="이강욱";
        String writeDate=String.format("%s %s",date,time);
        boardDao.insertBoard(title, content, writer, writeDate);
        return writeDate+"  입력한 글이 저장되었습니다.";
    }

    @GetMapping("/board/update") 
    public String boardUpdate(){
        String date=LocalDate.now().toString();
        String time=LocalTime.now().toString().substring(0,5);

        String seq="10";
        String title="수정 아침 기온";
        String content="수정매우 추웠음.,. 특히 광주는";
        String writeDate=String.format("%s %s",date,time);
        boardDao.updateBoard(seq, title, content, writeDate);
        return writeDate+"  입력한 글이 업데이트되었습니다.";

    }

} 
