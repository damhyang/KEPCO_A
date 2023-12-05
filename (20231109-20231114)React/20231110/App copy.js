import React, {Component} from "react"; //import는 node모듈에 react.js가 있음. React는 ???이다.
import Subject from './Subject'; //Subject.js파일이 다음 경로에 있고, 라는 클래스 이름은 무조건 Subject이다.


class App extends Component{ //Component를 상속됨.
  
  
  
  render(){                         //Component클래스 안에 render()함수가 있고 render함수는 HTML에 그림을 그려주는 함수 기능이다. 이 기능을 바꾸려면 오버라이팅
    return(
      <div className="App">       {/*<div>로 묶는 것은 이 리액트의 약속이다.*/}
        <Subject h1="Welcome" h2="Welcome React"></Subject>               {/*//외부경로에서 가져오려면 import를 해줘야함.*/}      
        <content></content>
      </div>
    );
  }
}

export default App;