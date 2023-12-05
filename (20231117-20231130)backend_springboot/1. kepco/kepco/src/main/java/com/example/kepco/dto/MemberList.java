package com.example.kepco.dto;

public class MemberList {
    public String name;
    public String userId;
    public String userPassword;

    public MemberList(String name, String userId, String userPassword){
        this.name=name;
        this.userId=userId;
        this.userPassword=userPassword;
    }
}
