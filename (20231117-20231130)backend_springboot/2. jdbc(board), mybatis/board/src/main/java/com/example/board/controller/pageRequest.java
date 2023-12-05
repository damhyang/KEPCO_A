package com.example.board.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class pageRequest {
    @GetMapping("/")
    public String home(){
        return "/html/index";  //src/main/resources/templetes가 최상위 위치이다.
    }  //.html. htm확장자 파일은 이름만 적어도 인식 가능->tymleaf, mustache
}
