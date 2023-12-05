package com.example.blog.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.example.blog.model.Member;
import java.util.List;


@Repository
public interface MemberRepository extends JpaRepository<Member, String>{
    List<Member> findByMemberIdAndMemberPw(String memberId, String memberPw);
    List<Member> findByMemberId(String memberId);
}

