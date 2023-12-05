package com.example.mybatis.config;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.context.annotation.Configuration;

//마이바티스만 가져다 쓰는 클래스
@Configuration //bean생성하는 어노테이션 스프링에서 가져옴.
@MapperScan(basePackages = "com.example.mybatis.mapper") //mybatis에서 가져다 쓰는 어노테이션
//위 경로에서의 폴더(패키지)를 스캔해 이 패키지 내에 있는 것을 다 가져와 쓰겠다.
public class MyBatisConfig {
    
}
