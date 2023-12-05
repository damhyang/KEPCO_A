import React,{Component} from "react";
import Subject from './components/Subject.js';
import TOC from './components/TOC.js';
import ReadContent from './components/ReadContent.js';
import Control from './components/Control.js';
import CreateContent from './components/CreateContent.js';
import UpdateContent from './components/UpdateContent.js';

class App extends Component{
  constructor(props){
    super(props);
    this.state={
      subject:{title:"WEB", sub:"Wolrd Wide Web"}
      ,mode:"welcome" 
      ,welcome:{title:"WEB", desc:"Hello React"}
      ,contents:[{id:1, title:"HTML", desc:"HTML is for information"}, {id:2, title:"CSS", desc:"CSS is for design"}, {id:3, title:"JavaScript", desc:"JavaScript is for interactive"}]
      ,selected_content_id:1
    }
  }

  findContentById(id){
    let content;
    for(let i=0; i<this.state.contents.length;i++){
      if(id===this.state.contents[i].id){
        content=this.state.contents[i];
        break;
      }
    }
    return content;
  }

  render(){
    // console.log(this.state.selected_content_id);
    // console.log(this.findContentById(this.state.selected_content_id));
    console.log(this.state.mode, this.state.selected_content_id);
    let title, desc, article;  //변수선언

    if(this.state.mode==="welcome" ){
      title=this.state.subject.title;
      desc=this.state.subject.desc;
    }else if(this.state.mode==="read"){
      const content=this.findContentById(this.state.selected_content_id);
      title=content.title;
      desc=content.desc;
    }else if(this.state.mode==="create"){
      article=<CreateContent onSubmit={
        function(title,desc){
          this.state.contents.push({id:this.state.contents.length+1, title:title, desc:desc})
          this.setState({contents:this.state.contents})
        }.bind(this)
      }/>
    }else if (this.state.mode==="update"){
      const content=this.findContentById(this.state.selected_content_id);
      title=content.title;
      desc=content.desc;
      article=<UpdateContent 
        title={title}
        desc={desc}
        onSubmit={
          function(title,desc){
            content.title=title;
            desc.content=desc;
            this.setState({mode:"read"});
          }.bind(this)
        }
      />
    }
    return(
      <div className="App">
        <Subject 
          title={this.state.subject.title} 
          sub={this.state.subject.sub} 
          onChangePage={
            function(){
              this.setState({mode:"welcome"})
            }.bind(this)
          }
          />
        <TOC 
          contents={this.state.contents} 
          onSelect={
            function(id){
              this.setState({mode:"read", selected_content_id:id})
            }.bind(this)
          }
        />
        <Control onChangemode={
          function(mode){
            if(mode==="delete"){
              let contents=this.state.contents;
              if(window.confirm("Are you sure")){
                for(let i=0; i<contents.length; i++){
                  if(contents[i].id===this.state.selected_content_id){
                    contents.splice(i,1);
                  }
                }
              }
            this.setState({mode:"welcome", contents:contents});       
            }else{this.setState({mode:mode})}
          }.bind(this)
        }/>
        <ReadContent title={title} desc={desc}/>
        {article}
      </div>
    )
  }
}
export default App;