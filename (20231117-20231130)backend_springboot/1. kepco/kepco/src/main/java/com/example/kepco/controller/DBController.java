package com.example.kepco.controller;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
//import java.util.HashMap;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.kepco.dao.DemoDao;

import jakarta.servlet.http.HttpServletRequest;

@RestController  //그냥 보여줄 때 쓰는 어노테이션
public class DBController {
    @Autowired
    DemoDao demoDao;

    @GetMapping("/jdbc/demo")
    public List<Map<String,Object>> jdbcDemo(){
        return demoDao.select();
    }

    // @GetMapping("/jdbc/demo/insert")
    // public String jdbcDemoInsert(){
    //     DemoDao.insert();
    //     return "잘 저장되었습니다.";
    // }

    @GetMapping("jdbc/demo/insert")
    public String jdbcTest(HttpServletRequest request){
        List<Map<String,Object>> value = demoDao.maxSeqSelect();
        //Map<String,Object> result = value.get(0);
        Map<String,Object> result = new HashMap<String,Object>();
        result = value.get(0);
        String maxSeq = result.get("seq").toString();
        int maxSeq1=Integer.parseInt(maxSeq);
        int seq=maxSeq1+1;
        String seq1=Integer.toString(seq);
        String user=request.getParameter("user");
        demoDao.insert(seq1,user);
        
        List<Map<String,Object>>totalCnt=demoDao.totalCount();
        Map<String,Object>totalCntHash=new HashMap<String,Object>();
        totalCntHash = totalCnt.get(0);
        String cnt=totalCntHash.get("cnt").toString();
        String message = String.format("%s 님이 저장되었습니다. 총 %d 의 회원이 있습니다.",seq,cnt);
        return message;
    }

}
