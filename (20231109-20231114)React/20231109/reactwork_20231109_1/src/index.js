import React from 'react';  //자바스크립트 파일react.js임.
import ReactDOM from 'react-dom/client';
import './index.css';  //.은 내 폴더안에서 쓰겠다.
import App from './App';  //.은 내 폴더안에서 App.js라는 파일을 만들어 쓰겠다는 뜻.
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root')); //ReactDOM.createRoot는 리액트v프레임워크(스크립트)안에 있는 함수(펑션)임. 루트라는 도큐먼트 오브젝트를 만듬.
root.render(   //render함수는 그림을 그려줌. App이라는 js파일로 그림을 그려줌.
  <React.StrictMode>
    <App /> 
  </React.StrictMode>
);
//서버의 엔트리포인트는 indexe.html임. div id=root를 보고 index.js를 찾아가고, 빌드를 하면 빌드한 파일을 찾아감.
//<App /> //<!--/*App이라는 js파일을 찾아감.*/-->
reportWebVitals();
