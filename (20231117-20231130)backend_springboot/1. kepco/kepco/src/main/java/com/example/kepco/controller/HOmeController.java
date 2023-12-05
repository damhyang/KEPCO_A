package com.example.kepco.controller;

import java.util.HashMap;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.bind.annotation.GetMapping;

import com.example.kepco.dto.Member;


@Controller
public class HOmeController {
    @RequestMapping("/")  //접속할 주소설정
    public String home(){  //접속할 주소의 페이지 정보 페이지 정보를 스트링으로 줌,.
        return "/Html/String"; //경로에 대해서는 대소문자 구분을 하지 않음./Html/String
    }

    @GetMapping("/html/void")  //접속할 주소이면서 페이지 정보를 동시에 줌.
    public void htmlVoid() {
    }

    // Map중 HashMap으로 html에 전달 가능.
    @GetMapping("/html/map")
        public Map<String, Object> htmlMap(Map<String, Object> map) {
            Map<String, Object> map2 = new HashMap<String, Object>();
            return map2;
        }


    @GetMapping("/html/model")
    public Model htmlModel(Model model) {   //스프링프레임워크의 모델
        return model;
    }

    @GetMapping("html/model_and_view")
    public ModelAndView htmlModel() {
        ModelAndView mav = new ModelAndView();
        mav.setViewName("html/model_and_view");
        return mav;
    }

    @GetMapping("html/object")
    public Member htmlObject() {
        Member member = new Member();
        member.setName("kim");
        member.setAge(34);
        return member;
    }

    //연습문제
    @RequestMapping("/html/exam")
    public void htmlExam() {
    }

    @GetMapping("req/http")
    public String httpReq(){
        return "/html/request";
    }

    @Autowired
    @GetMapping("jdbc/html")
    public String jdbchtml(){
        return "html/demo";
    }
}
            