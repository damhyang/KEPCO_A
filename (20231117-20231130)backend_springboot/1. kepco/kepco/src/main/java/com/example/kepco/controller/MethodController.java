package com.example.kepco.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;


//post는 에러남.
// @Controller
// @ResponseBody
// public class MethodController {
//     @PostMapping("req/post")       //post는 데이터가 넘어가야함. 넘어가는 데이터가 없어서 오류남.
//     public String get() {
//         return "GET";
//     }
// }



// @Controller
// @RestController
// public class MethodController {
//     @RequestMapping(value="req/get", method=RequestMethod.GET) 
//     public String get() {
//         return "GET";
//     }
// }

// @Controller
// @ResponseBody
// public class MethodController {
//     @GetMapping("req/get")
//     public String get() {
//         return "GET";
//     }
// }
