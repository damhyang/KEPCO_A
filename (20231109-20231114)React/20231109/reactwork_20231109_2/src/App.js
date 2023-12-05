import './App.css';
import React, {Component} from 'react';
import Child from './Child';


class App extends Component {
    constructor(props){
        //react의 component클래스의 내용을 상속받아 씀.
        super(props);
        this.state = {
          Child :{a:'1', b:'2'}    //척
        }
        //자기자신(self)가 아니라 찍어내서 나온 이것(this, 구현체)임
    }   //생성자
    render() {
      return (
        <div className="App">
          {/* <Child></Child> */}
          <Child a='1' b='2'></Child>

        
        </div>
      );
    }
  }
export default App;
