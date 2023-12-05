import React, {Component} from 'react';
import './App.css';
import Header from './js/Header'; 
import Section from './js/Section'; 
import Article from './js/Article'; 
import Footer from './js/Footer'; 

class App extends Component{
  constructor(props) {
    super(props);
    
    this.state={
      footerContent:[
        {id:1,con:"" }
        ,{id:2,con:""}
        ,{id:3,con:""}
        ,{id:4,con:""}
        ,{id:5,con:""}
      ]
    }
  }


  render() {
    return(
      <div className="App">
        <Header/>
        <Section/>
        <Article/>
        <Footer footerContent={this.state.footerContent}></Footer><Footer/>
      </div>
    );
  }
}


// function App() {
//   return (
//     <div className="App">
//       <Header></Header>
//       <Section></Section>
//       <Article></Article>
//       <Footer></Footer>
//     </div>
//   );
// }

export default App;
