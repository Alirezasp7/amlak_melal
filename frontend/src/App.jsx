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
import SignUp from './auth/SignUp';
import ApartmentBuy from '../src/client/propertyListing/apartment/ApartmentBuy';

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
          <Route path='/SignUp' element={<SignUp/>} />
          {/* property listing */}
          <Route path='/Home/Addition/ApartmentBuy' element={<ApartmentBuy />}/>
        </Routes>
      </div>
    </Router>
  );
}


export default App;