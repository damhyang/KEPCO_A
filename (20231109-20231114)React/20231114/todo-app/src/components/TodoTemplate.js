import React from "react";
import '../css/TodoTemplate.css';

const TodoTemplate=({children})=>{ //밖(App.js)에서 불러다쓰기 위해서 TodoTemplate이라는 변수를 지정
    return(
        <div className="TodoTemplate">
            <div className="app-title">일정관리</div>
            <div className="content">{children}</div>
        </div>
    )
}

export default TodoTemplate;