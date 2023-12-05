import './App.css';
import {BrowserRouter, Routes, Route, Link, NavLink, Outlet, useParams} from 'react-router-dom';

function Home() {
  return (
    <div>
      <h2>Home</h2>
      Home...
    </div>
  );
}

const contents = [
  {id: 1, title: 'HTML', description: 'HTML is ...'},
  {id: 2, title: 'JS', description: 'JS is ...'},
  {id: 3, title: 'React', description: 'React is ...'}
];

function Topics(){
  const lists=[];
    for(let i=0;i<contents.length;i++){
      lists.push(
        <li key={contents[i].id}>
          <NavLink to={`/topics/${contents[i].id}`}>{contents[i].title}</NavLink>
        </li>
      )
    }
  return(
    <div>
      <h2>Topics</h2>
      Topics...
      <ul>
        {/* <li><NavLink to="/topics/1">HTML</NavLink></li>
        <li><NavLink to="/topics/2">JS</NavLink></li>
        <li><NavLink to="/topics/3">React</NavLink></li> */}
        {lists}
      </ul>
      <Outlet></Outlet>
  </div>
  )
}


  

function Topic(){
  const {id}=useParams();
  let selected_topic={
    title: 'Sorry'
    ,description: 'Not Found'
  }

  for(const topic of contents){
    if(topic.id===Number(id)){
      selected_topic=topic;
      break;
    }
  }

  return(
    <div>
      <h3>{selected_topic.title}</h3>
      <h5>{selected_topic.desc}</h5>
    </div>
  )
}

function Contact() {
  return (
    <div>
      <h2>Contact</h2>
      Contact...
    </div>
  )
}
  

function App(){
  return(
    // <div className='App'>
    //   <Home/> //component이다.
    //   <Topics/>  //component이다.
    //   <Contact/>  //component이다.
    // </div>

    // <div className='App'>
    //   <ul>
    //     <li><a href="/Home">Home</a></li>
    //     <li><a href="/Topics">Topics</a></li>
    //     <li><a href="/Contact">Contact</a></li>
    //   </ul>
    //   </div>

    <BrowserRouter>
      <div className='App'>
        <h1>React Router DOM Example</h1>
        <ul>
          {/* <li><a href="/Home">Home</a></li>
          <li><a href="/Topics">Topics</a></li>
          <li><a href="/Contact">Contact</a></li> */}
          {/* <li><Link to="/">Home</Link></li>
          <li><Link to="/Topics">Topics</Link></li>
          <li><Link to="/Contact">Contact</Link></li> */}
          <li><NavLink to="/">Home</NavLink></li>
          <li><NavLink to="/topics">Topics</NavLink></li>
          <li><NavLink to="/contact">Contact</NavLink></li>
        </ul>
        <Routes>
          <Route path='/' element={<Home/>}/>
          <Route path='/contact/' element={<Contact/>}/>
          <Route path='/topics/' element={<Topics/>}/>
            <Route path=':id' element={<Topic/>}/>
            {/* <Route path='1' element={<Topic/>}/>
            <Route path='2' element={<Topic/>}/>
            <Route path='3' element={<Topic/>}/> */}
        </Routes>
      </div>
    </BrowserRouter>
  )
}

export default App;

