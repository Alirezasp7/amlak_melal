import './App.css';
import {
  Routes,
  Route,
 BrowserRouter as Router
  } from 'react-router-dom';
import Home from './client/Home';
import Navbar from './components/Navbar';
import About from './About'
import Details from './client/Details';
import Addition from './client/Addition';


function App() {
  return (
    <Router>
      <div className='app'>
        <Navbar />
        <Routes>
          <Route path='/About' element={<About/>} />
          <Route path='/' element={<Home/>} />
          <Route path="/Home/:id" element={<Details/>} />
          <Route path='/Home/Addition' element={<Addition/>} />
          {/* <Route path='/Consultant' element={<Consultant/>} />
          <Route path='/Consultant/Dashboard' element={<Dashboard/>} />
          <Route path='/Consultant/Dashboard/:id' element={<ConsultantAffirmation/>}/>
          <Route path='/SignIn' element={<SignIn/>} />
          <Route path='/Favorites' element={<Favorites/>} />
          <Route path='/BookMarks' element={<BookMarks/>} />
          <Route path="/Favorites/:id" element={<Details/>} />
          <Route path='/BookMarks/:id' element={<ConsultantAffirmation/>}/>
          <Route path='/Consultant/Notes' element={<Notes/>}/>
          <Route path='/Home/Addition' element={<Addition/>}/> */}
        </Routes>
      </div>
    </Router>
  );
}


export default App;