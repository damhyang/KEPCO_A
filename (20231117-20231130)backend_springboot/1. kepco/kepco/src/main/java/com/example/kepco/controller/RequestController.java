package com.example.kepco.controller;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.example.kepco.dao.DemoDao;

import jakarta.servlet.http.HttpServletRequest;   //jakarta은 이전에 다른 버전에서는 이름이 달랐으나 3.0스프링 부트에서는 jakarta이다.

@Controller   //컨트롤러라고 어노테이션을 줘야 스프링부트에서 가져다 쓴다. 방법은 빈을 쓰거나 컨트롤러를 쓴다.
@RestController
public class RequestController {
    @Autowired
    DemoDao demoDao;


    @GetMapping("res/http")
    public String httpResponse(HttpServletRequest request){  //함수명 http는 아무렇게나 바꿔도 된다. 주소인 req.http로 찾아가지 때문에
        String name = request.getParameter("name");  //request에는 getParameter이라는 요소가 있음.  보통 form태그<action="보내는 곳" methon="get/post"> 그 하위의 input태그에 네임, select태그 옵션에 벨류 타입를 통해 request를 보낸다.
        String pageNum = request.getParameter("pagenum"); //getParameter은 소문자를 받도록 하자.
        String age = request.getParameter("age");
        return "name:"+name+"/n"+"pageNum:"+pageNum+"/n"+"age:"+age+"/n";
    }

    @GetMapping("req/param1")
    public String param1(
        @RequestParam("key1") String key1,
        @RequestParam("key2") String key2
        ){
            return key1 + ", " + key2;
        }


//map은 파이썬의 딕셔너리와 유사하여 키와 벨루가 필요하고 그 키와 벨류의 타입의 선언을 <String, Object>함.
//primitive float, int,doubledms stack에 저장된다. String a=""는 길이(length)를 가짐.
// String arr [] 형태로 arr로 선언하는데 변수이기 때문에 값을 변경할 수가 없다. 다른 변수만들어서 카피해서 쓰는 방법만 있음.
//데이터를 다룰 때는 콜렉션타입을 쓰게된다. 자바는 Map, List가 있다.
//map (key,value)  Map<String, Object>  //key와 value의 변수타입을 선언함.Object는 최상위 타입이다.(길이, 이즈이콜)
//list(array)     List<String>

//인터페이스                   객체
//Map<String, Object> map2 = new HashMap()


//RequestParam Map<String, Object>에서 String을 name, Object를 value로 받아들인다.
    @GetMapping("req/param2")
    public String param2(
        @RequestParam Map<String, Object> map
    ){return map.toString();}

    @GetMapping("req/path/{path1}/{path2}")
    public  String path(
        @PathVariable("path1") String path1, 
        @PathVariable("path2") String path2
    ){return path1 + ", " + path2;}
    //이것을 주로 쓰기로는 일정관리나 신문사가 있다. 매일매일 새페이지를 생성하는 것이 아니라 페이지틀은 그대로 select 값만 바꿔서 사용한다.

    @GetMapping("req/data")
    public Map<String, Object> reqData(   //return타입을 map타입으로 해주면 된다.
        @RequestParam Map<String, Object> data
    ){return data;}

    // @GetMapping("jdbc/demo/insert")
    // public String jdbcInsert(HttpServletRequest request){
    //     String seq = request.getParameter("seq");
    //     String user = request.getParameter("user");
    //     demoDao.insert(seq,user);
    //     return user+"가 저장되었습니다.";
    // }
}
