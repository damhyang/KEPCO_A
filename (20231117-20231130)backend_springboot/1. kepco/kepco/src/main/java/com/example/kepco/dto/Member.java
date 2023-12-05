package com.example.kepco.dto;

public class Member {
    public String name;

    // public Member(String name){
    //     this.name=name;
    // }

    public int age;

    public String setName(String name){
        this.name=name;
        return this.name;
    }
    
    public int setAge(int age){
        this.age=age;
        return this.age;
    }
}
