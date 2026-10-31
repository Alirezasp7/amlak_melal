import './App.css';
import {
  Routes,
  Route,
 BrowserRouter as Router
  } from 'react-router-dom';
// import About from './client/About.js';
import Home from './client/Home';
import Navbar from './functions/Navbar';
import About from './About'
// import Details from './client/Details.js';
// import Consultant from '../src/consultant/Consultant.js'
// import Dashboard from './consultant/Dashboard.js';
// import SignIn from './signin/SignIn.js';
// import ConsultantAffirmation from './consultant/ConsultantAffirmation.js';
// import Favorites from './client/Favorites.js';
// import BookMarks from './consultant/BookMarks.js';
// import Notes from './consultant/Notes.js';
// import Addition from './client/Addition.js';


function App() {
  return (
    <Router>
      <div className='app'>
        <Navbar />
        <Routes>
          <Route path='/About' element={<About/>} />
          <Route path='/' element={<Home/>} />
          {/* <Route path="/Home/:id" element={<Details/>} />
          <Route path='/Consultant' element={<Consultant/>} />
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