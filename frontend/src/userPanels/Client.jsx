import './design/Client.css';
import { Routes, Route, BrowserRouter as Router } from 'react-router-dom';
import Home from '../client/Home';
import Navbar from '../components/Navbar';
import About from '../Client/About';
import Details from '../client/Details';
import Addition from '../client/Addition';
import SignUp from '../auth/SignUp';
import ClientDashboard from '../client/ClientDashboard';
import Favorites from '../client/Favorites';
import EditProperty from '../client/EditProperty';
//property listing
import ApartmentBuy from '../client/propertyListing/apartment/ApartmentBuy';
import ApartmentSell from '../client/propertyListing/apartment/ApartmentSell';
import ApartmentTenant from '../client/propertyListing/apartment/ApartmentTenant';
import ApartmentLandlord from '../client/propertyListing/apartment/ApartmentLandlord';
//
import OfficeSell from '../client/propertyListing/office/OfficeSell';
import OfficeBuy from '../client/propertyListing/office/OfficeBuy';
import OfficeTenant from '../client/propertyListing/office/OfficeTenant';
import OfficeLandlord from '../client/propertyListing/office/OfficeLandlord';
//
import CommercialSell from '../client/propertyListing/commercial/CommercialSell';
import CommercialBuy from '../client/propertyListing/commercial/CommercialBuy';
import CommercialTenant from '../client/propertyListing/commercial/CommercialTenant';
import CommercialLandlord from '../client/propertyListing/commercial/CommercialLandlord';
//
import DemolitionBuy from '../client/propertyListing/demolition/DemolitionBuy';
import DemolitionSell from '../client/propertyListing/demolition/DemolitionSell';

function Client() {
  return (
    <Router>
      <div className='Client'>
        <Navbar />
        <Routes>
          <Route path='/About' element={<About/>}/>
          <Route path='/' element={<Home/>}/>
          <Route path="/Home/:id" element={<Details/>}/>
          <Route path='/Home/Addition' element={<Addition/>}/>
          <Route path='/SignUp' element={<SignUp/>}/>
          <Route path='/ClientDashboard' element={<ClientDashboard/>}/>
          <Route path='/ClientDashboard/:id' element={<EditProperty/>}/>
          <Route path='/Favorites' element={<Favorites/>}/>
          <Route path='/Favorites/:id' element={<Details/>}/>
          {/* property listing */}
            {/* apartment */}
          <Route path='/Home/Addition/ApartmentBuy' element={<ApartmentBuy />}/>
          <Route path='/Home/Addition/ApartmentSell' element={<ApartmentSell />}/>
          <Route path='/Home/Addition/ApartmentTenant' element={<ApartmentTenant />}/>
          <Route path='/Home/Addition/ApartmentLandlord' element={<ApartmentLandlord />}/>
            {/* office */}
          <Route path='/Home/Addition/OfficeBuy' element={<OfficeBuy />}/>
          <Route path='/Home/Addition/OfficeSell' element={<OfficeSell />}/>
          <Route path='/Home/Addition/OfficeTenant' element={<OfficeTenant />}/>
          <Route path='/Home/Addition/OfficeLandlord' element={<OfficeLandlord />}/>
            {/* commercial */}
          <Route path='/Home/Addition/CommercialBuy' element={<CommercialBuy />}/>
          <Route path='/Home/Addition/CommercialSell' element={<CommercialSell />}/>
          <Route path='/Home/Addition/CommercialTenant' element={<CommercialTenant />}/>
          <Route path='/Home/Addition/CommercialLandlord' element={<CommercialLandlord />}/>
            {/* demolition */}
          <Route path='/Home/Addition/DemolitionBuy' element={<DemolitionBuy />}/>
          <Route path='/Home/Addition/DemolitionSell' element={<DemolitionSell />}/>
        </Routes>
      </div>
    </Router>
  );
}


export default Client;