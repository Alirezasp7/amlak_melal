import { Link } from 'react-router-dom';
import './design/ConsultantNavbar.css';


const Navbar = () => {
    return(
        <ul className='navbar'>
            <li className='navbar-button'>
                <Link className='Navbar-Link' to="/">Home</Link>
            </li>
            <li className='navbar-button'>
               <Link className='Navbar-Link' to="/ConsultantList">Consultants</Link> 
            </li>
            <li className='navbar-button'>
               <Link className='Navbar-Link' to="/SignUp">Account</Link> 
            </li>
            <li className='navbar-button'>
               <Link className='Navbar-Link' to="/ConsultantDashboard">Dashboard</Link> 
            </li>
        </ul>
    )
}
export default Navbar;

