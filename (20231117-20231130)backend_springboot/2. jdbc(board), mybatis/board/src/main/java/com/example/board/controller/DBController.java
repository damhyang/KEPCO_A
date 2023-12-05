package com.example.board.controller;

import java.util.*;
import org.springframework.web.bind.annotation.*;

import org.springframework.beans.factory.annotation.Autowired;

import com.example.board.dao.BoardDao;

import jakarta.servlet.http.HttpServletRequest;




@RestController  //html페이지를 생성하지 않아도 스트링으로 보여줌.단순히 DB와 연결
public class DBController {
    @Autowired //BoardDao클래스를 주입하고자쓰는 클래스어노테이션
    BoardDao boardDao;

    // @GetMapping("/board/list1")
    // public List<Map<String,Object>> BoardList1(){
    //     return boardDao.listSelect();
    // }

    @GetMapping("/board/insert")
    public String boardInsert(
        @RequestParam("title") String title,
        @RequestParam("content") String content,
        @RequestParam("writer") String writer
        ){
            boardDao.insert(title, content, writer);
            return writer+"님의 글이 잘 저장되었습니다.";
        }

    // @GetMapping("/board/list2")
    // public String BoardList2(){
    //     String result = boardDao.listSelect().toString();
    //     String html="<h1>" + result + "</h1>";
    //     return html;
    // }

    // @GetMapping("/board/list3")
    // public String BoardList3(){
    //     List<Map<String,Object>> qrtSet=boardDao.listSelect();
    //     String title=qrtSet.get(0).get("title").toString();
    //     String writer=qrtSet.get(0).get("writer").toString();
    //     return title + writer;
    // }

    @GetMapping("/board/list")
    public String BoardList(){
        List<Map<String, Object>> qrySet = boardDao.listSelect();
        String title = null;
        String writer = null;
        String seq = null;
        String href = null;
        String deleteButton = null;
        String updateButton = null;
        String searchCount = null;
        String no;
        String html = """
                       <html>
                         <body>
                          <table border="1">
                            <th>번호</th>
                            <th>제목</th>
                            <th>작성자</th>
                            <th>삭제</th>
                            <th>수정</th>
                            <th>조회수</th>
                       """;
        for (int i = 0; i < qrySet.size(); i++){
            no = Integer.toString(i+1);
            seq = qrySet.get(i).get("seq").toString();
            title = qrySet.get(i).get("title").toString();
            writer = qrySet.get(i).get("writer").toString();
            searchCount = qrySet.get(i).get("search_count").toString();
            href = String.format("<a href='/board/detail?seq=%s'>",seq);
            deleteButton = String.format("<a href='/board/delete?seq=%s'>삭제",seq);
            updateButton = String.format("<a href='/board/update?seq=%s'>수정</a>",seq);
            html += "<tr>";
            html += "<td>"+no+"번"+"</td>";
            html += "<td>"+href+title+"</a></td>";
            html += "<td>"+writer+"</td>";
            html += "<td>"+deleteButton+"</a></td>";
            html += "<td>"+updateButton+"</td>";
            html += "<td>"+searchCount+"</td>";
            html += "</tr>";
        }
        String form = """
                </table>
                <hr>
                <a href="/"><button type="submit">글쓰기</button></a>
                """;
        html += form+"</html>";
        return html;
    }

    @GetMapping("/board/detail")
    public String boardDetail(HttpServletRequest request){
        String seq=request.getParameter("seq");
        String qrySet = boardDao.detailSelect(seq).get(0).get("content").toString();
        String searchCount=boardDao.detailSelect(seq).get(0).get("search_count").toString();
        searchCount=Integer.toString(Integer.parseInt((searchCount)+1));
        boardDao.updateSearchCount(seq, searchCount);
        int count = boardDao.getCountAnswer(seq).size();
        List<Map<String, Object>> answerQrySet = boardDao.getCountAnswer(seq);
        String html = "<div border='1'>"+qrySet+"</div>";
        if (count > 0){
            for (int i = 0; i < count; i++){
               html += "<li>"+answerQrySet.get(i).get("answer").toString()+"</li>";   
            } 
        } else {
            html += "<br>달린 답글이 없습니다<br>";
        }
        html += "<a href='/board/list'><button type='submit'>목록보기</button></a>";
        html += String.format("<a href='/board/answer?seq=%s'><button type='submit'>답글달기</button></a>",seq);
        return html;
    }

    @GetMapping("/board/delete")
    public String boardDelete(
        @RequestParam("seq") String seq
    ){
        String title=boardDao.detailSelect(seq).get(0).get("title").toString();
        boardDao.delete(seq);
        return seq+" " +title+"글이 삭제되었습니다.";
    }

    @GetMapping("/board/update")
    public String boardUpdate(String seq){
        String title=boardDao.detailSelect(seq).get(0).get("title").toString();
        String content=boardDao.detailSelect(seq).get(0).get("content").toString();
        String html="<form action='/board/update/excute' method='get'>";
        html+=String.format("<input type='hidden' name='seq' values=%s>",seq);
        html+=String.format("제목  :<input type='text' name='title' value=%s><br>",title);
        html+=String.format("내용  :<textarea name='content'>%s</textarea><br>",content);
        html+="전송 : <button type='submit'>글수정</button></form>";
        return html;
    }

    @GetMapping("/board/update/excute")
    public String boardUpdateExcute(
        @RequestParam("title") String title,
        @RequestParam("content") String content,
        @RequestParam("seq") String seq){
        boardDao.update(title, content,seq);
        String html="<html><body>";
        html+=title+"글이 수정되었습니다.<br>";
        html+="<a href='/board/list'><button>목록으로</button></a></body></html>";
        return html;
    }
    @GetMapping("board/answer")
    public String boardAnswer(@RequestParam("seq") String seq){
        String html = "";
        html += "<form action='/board/answer/execute' method='get'>";
        html += String.format("<input type='hidden' name='seq' value=%s>",seq);
        html += "<textarea name='answer'></textarea><br>";
        html += "<button type='submit'>답글 등록</button>";
        html += "</form>";
        return html;
    }

    @GetMapping("board/answer/execute")
    public String boardAnswerInsert(
        @RequestParam("seq") String seq,
        @RequestParam("answer") String answer){
            boardDao.insertAnswer(seq, answer);
        return "답글이 등록되었습니다";
    }
}
