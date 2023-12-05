import './App.css';
import TodoTemplate from './components/TodoTemplate';
import TodoInsert from './components/TodoInsert';
import TodoList from './components/TodoList';
import React,{useCallback, useSet, useState, useRef} from 'react';

function App() {
  const [todos, setTodos]=useState([
    {id:1, text:"리액트 기초 알아보기", checked:true, date:new Date().toString().substring(8,24)}
    ,{id:2, text:"컴포넌트 스타일 해보기", checked:false, date:new Date().toString().substring(8,24)}
    ,{id:3, text:"일정관리App만들어 보기", checked:false, date:new Date().toString().substring(8,24)}
    ,{id:4, text:"리액트 함수형과 클래스형 비교", checked:false,date:new Date().toString().substring(8,24)}
  ]);

  const nextId=useRef(todos.length+1);

  const onInsert=useCallback(
    (text)=>{
      const todo={
        id:nextId.current, text:text, checked:false, date:new Date().toString().substring(8,24)
      };
      setTodos(todos.concat(todo));
      nextId.current+=1;
    },[todos]
    )

  const onRemove=useCallback(
    (id)=>{
      setTodos(todos=>todos.filter((todo) => todo.id !== id));
    },[todos]
  )
//map함수, filter함수 for문 대신으로 map은 모두 가져오기, filter은 알맞는 것만 가져오기.
//map(함수, [array]), filter(값, 조건)
//duck typing(testing) 
  const onToggle=useCallback((id)=>setTodos(todos.map((todo)=>todo.id===id? {...todo, checked:!todo.checked}: todo)),[todos])

  return (
    <TodoTemplate>
      <TodoInsert onInsert={onInsert}/>
      <TodoList todos={todos} onRemove={onRemove} onToggle={onToggle}/>
    </TodoTemplate>
  );
}

export default App;
