package com.example.kepco.controller;

import com.example.kepco.dto.Member;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;



@Controller
@ResponseBody  //html페이지를 따로 생성할 필요가 없을 때는 이 @ResponseBody을 쓴다. //리턴이 주소대신에 html문자열로 보내는 어노테이션임.
public class Json1Controller {
    @GetMapping("/json/string")  //사용자가 요청하는 주소
    public String json() {
        return "<h1>json/string<h1><h5>json/string<h5>";   //내가 정한 주소이었으나 @ResponseBody을 하면 리턴 값이 body가 됨.//html 문자열// 태그 안에 스타일 주기는 먹지 않음.
    }
        
    @GetMapping("/json/map")
    public Map<String, Object> jsonMap(Map<String, Object> map){
        Map<String, Object> map2=new HashMap<String, Object>();
        map2.put("key1","value");
        map2.put("key2",12345);
        map2.put("key3", true);
        System.out.println(map2.get("key1"));
        System.out.println(map2.toString());
        return map2;
    }

    @GetMapping("/json/object")
    public Member jsonObject(){
        Member member=new Member();
        member.setName("Kim");
        member.setAge(34);
        return member;
    }

    @GetMapping("/json2/list")
    public List<String> jsonList(){
        List<String> list = new ArrayList<>();
        for(int i=1; i<=3;i++){
            String a=Integer.toString(i);   //string만 들어가므로 형태 변환을 시킴.  ch)parseint
            list.add(a);
        }
        return list;
    }
    //연습문제(1차풀이)
    // @GetMapping("/json/exam")
    // public Map<String,Object> jsonexam(Map<String,Object> map){
    //     Map<String,Object> map2=new HashMap<String,Object>();
    //     map2.put("count",2);
    //     HashMap<String, Object> personMap1 = new HashMap<String, Object>();
    //     personMap1.put("name", "가");
    //     personMap1.put("userId", "A");
    //     personMap1.put("userPassword","1");
    //     HashMap<String, Object> personMap2 = new HashMap<String, Object>();
    //     personMap2.put("name", "나");
    //     personMap2.put("userId", "B");
    //     personMap2.put("userPassword","2");
    //     return personMap2;
    // }
    //연습문제(교수님풀이)
    
}
 