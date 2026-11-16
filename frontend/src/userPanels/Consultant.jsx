import './design/Consultant.css';
import { Routes, Route, BrowserRouter as Router } from 'react-router-dom';
import ConsultantHome from '../consultant/ConsultantHome';
import SignUp from '../auth/SignUp';
import ConsultantNavbar from '../components/ConsultantNavbar';
import ConsultantList from '../consultant/ConsultantList';
import EditProfile from '../consultant/EditProfile'

function Consultant() {
  return (
    <Router>
      <div className='consultant'>
        <ConsultantNavbar />
        <Routes>
          <Route path='/' element={<ConsultantHome/>}/>
          <Route path='/ConsultantList' element={<ConsultantList/>}/>
          <Route path='/SignUp' element={<SignUp/>}/>
          <Route path='/ConsultantInfo/EditProfile' element={<EditProfile/>}/>
        </Routes>
      </div>
    </Router>
  );
}

export default Consultant;
