package com.example.blog.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
//import org.springframework.web.bind.annotation.RequestParam;

import com.example.blog.model.Member;
import com.example.blog.repository.MemberRepository;
import com.example.blog.util.GetDateTime;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpSession;

@Controller
public class LogInSignUpController {
    @Autowired
    MemberRepository memberRepository;

    @GetMapping("/")
    public String logInSignUp(){
        return "/html/initial";
    }

    @PostMapping("/")
    public String logInSignUpPost(HttpSession session
                                 ,HttpServletRequest logInSignUprequest
                                 ,Model model){
        String logInMemberId =logInSignUprequest.getParameter("logInMemberId");
        String logInMemberPw=logInSignUprequest.getParameter("logInMemberPw");
        String signUpMemberId=logInSignUprequest.getParameter("signUpMemberId");
        String signUpMemberPw=logInSignUprequest.getParameter("signUpMemberPw");
        String signUpMemberName=logInSignUprequest.getParameter("signUpMemberName");
        String signUpMemberPwConfirm=logInSignUprequest.getParameter("signUpMemberPwConfirm");
        String logInSingUpCheckBox=logInSignUprequest.getParameter("CheckBox");
        String result;
        if(logInSingUpCheckBox==null){
            List<Member> logInMember;
            logInMember=memberRepository.findByMemberIdAndMemberPw(logInMemberId, logInMemberPw);
            session.setAttribute("memberId", logInMemberId);
            session.setAttribute("memberPw", logInMemberPw);
            int logCount=logInMember.size();
            if(logCount==1){
                result = "/html/test1";
            }else{
                String message = "Your ID&Password doesn't exist.";
                model.addAttribute("message", message);
                result = "/html/initial";
            }
        }else{
            int cnt = memberRepository.findByMemberId(signUpMemberId).size();
            if(cnt>0){
                String message ="Your ID already exist.";
                model.addAttribute("message", message);
                result = "/html/initial";

            }else{
                System.out.println(GetDateTime.getTime());
                if(signUpMemberPw.equals(signUpMemberPwConfirm)){
                    Member signUpMember=new Member();
                    signUpMember.setMemberId(signUpMemberId);
                    signUpMember.setMemberName(signUpMemberName);
                    signUpMember.setMemberPw(signUpMemberPw);
                    String signUpDate=GetDateTime.getTime();
                    signUpMember.setSignUpDate(signUpDate);
                    memberRepository.save(signUpMember);
                    String message ="Resister Success.please Log In.";
                    model.addAttribute("message", message);
                    result = "/html/initial"; 
                }else{ 
                    String message ="Password confirm doesn't match.";
                    model.addAttribute("message", message);
                    result = "/html/initial";
                }

            }
        }
        return result;
    }
}

