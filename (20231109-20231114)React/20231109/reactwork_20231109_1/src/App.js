//<Subject></Subject>  ->  <Subject/>
//<TOC></TOC>  ->  <TOC/>
import './App.css';
import React, { Component } from 'react'; 
import Subject from './Subject';
import TOC from './TOC';
import Content from './Content';

class App extends Component{
  render(){
    return(
      <div className='App'>
          <Subject title='WEB' sub='World Wide Web!'></Subject>
          <TOC/>
          <Content title='HTML' desc='HTML is HyperText Markup Language.'></Content>
          <MyComponent data='Data!' number='2324'></MyComponent>
          <MyComponent data='Data!!' number='2324'></MyComponent>
      </div>    
    );
  }
}

class MyComponent extends Component {
  render() {
    return (
      <div>
        {/* String[] data=;
        int number=; */}
        {/* 자바의 게터세터와 유사
          get(data){
          this.data=data
        }
        get(data){
          this.data=data
        } */}
        <h1>{this.props.data}</h1>
        <h1>{this.props.number}</h1>
      </div>
    );
  }
}


// class Subject extends Component {
//   render() {
//     return (
//       <header>
//         <h1>{this.props.title}</h1>
//         {this.props.sub}
//       </header>
//     );
//   }
// }

// class TOC extends Component {
//   render() {
//     return (
//       <nav>
//         <ul>
//           <li><a href="1.html">HTML</a></li>
//           <li><a href="2.html">CSS</a></li>
//           <li><a href="3.html">JavaScript</a></li>
//         </ul>
//       </nav>
//     )
//   }
// }
    
// class Content extends Component {
//   render() {
//     return (
//       <article>
//         <h2>{this.props.title}</h2>
//         {this.props.desc}
//       </article>
//     );
//   }
// }
      
  
export default App;
