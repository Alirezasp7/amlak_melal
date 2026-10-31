import { Link } from 'react-router-dom';
import './Navbar.css';


const Navbar = () => {
    return(
        <ul className='navbar'>
            <li className='navbar-button'>
                <Link className='Navbar-Link' to="/">Home</Link>
            </li>
            <li className='navbar-button'>
               <Link className='Navbar-Link' to="/About">About</Link> 
            </li>

            {/* <li className='navbar-button'>
                <Link className='Navbar-Link' to="/Consultant">consultant</Link>
            </li>
            <li className='navbar-button'>
                <Link className='Navbar-Link' to="/SignIn">SignIn</Link>
            </li>
            <li className='navbar-button'>
                <Link className='Navbar-Link' to="/Favorites">Favorites</Link>
            </li>
            <li className='navbar-button'>
                <Link className='Navbar-Link' to="/BookMarks">BookMarks</Link>
            </li> */}
        </ul>
    )
}
export default Navbar;

