import './App.css';
import { Component, useState } from 'react';

class ClassComp extends Component {   //class는 꼭 props를 써야함. class내의 props와 state라는 객체를 쓰는 것임.
  state={
    number:this.props.initNumber
    , date:new Date().toString()
  }//state는 먼저 생성되어 있어야함.
  render() {
    const number=this.state.initNumber; //this.props.initNumber;
    return (
      <div className="container">
        <h2>Class Style Component</h2>
        <p>Number : { this.state.number }</p>
        <p>{this.state.date}</p>
        <button type="button" onClick={(e)=>this.setState({number:Math.random()})}>Random 선택</button>
      </div>
    )  
  }
}

  function FunctionComp(props) {
    const numberState=useState(props.initNumber);
    const number =numberState[0];
    const setNumber=numberState[1];
    const setDate=dataS
    console.log(numberState);
    console.log(number);
  return (
    <div className="container">
      <h2>Function Style Component</h2>
      <p>Number : { number }</p>
      <button type='button' onClick={(e)=>set()}>Random선택</button>
    </div>
  )
}

function App() {
  return (
    <div className="container">
      <h1>Hello World</h1>      
      <ClassComp initNumber={10}/>
      <FunctionComp initNumber={2}/>
    </div>
  );
}

export default App;
  
