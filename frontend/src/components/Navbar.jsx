import { Link } from 'react-router-dom';
import './design/Navbar.css';


const Navbar = () => {
    return(
        <ul className='navbar'>
            <li className='navbar-button'>
                <Link className='Navbar-Link' to="/">Home</Link>
            </li>
            <li className='navbar-button'>
               <Link className='Navbar-Link' to="/About">About</Link> 
            </li>
            <li className='navbar-button'>
               <Link className='Navbar-Link' to="/SignUp">Account</Link> 
            </li>
            <li className='navbar-button'>
               <Link className='Navbar-Link' to="/ClientDashboard">Client Dashboard</Link> 
            </li>
            <li className='navbar-button'>
               <Link className='Navbar-Link' to="/Favorites">Favorites</Link> 
            </li>
        </ul>
    )
}
export default Navbar;

