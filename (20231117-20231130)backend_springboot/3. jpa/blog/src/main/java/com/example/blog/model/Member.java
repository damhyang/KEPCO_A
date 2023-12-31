package com.example.blog.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.Data;

@Entity
@Data
public class Member {
    @Id
    private String memberId;
    private String memberPw;
    private String memberName;
    private String signUpDate;
}
