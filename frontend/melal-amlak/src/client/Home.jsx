// import RealState from "../data/REALSTATELIST.json";
import { Link } from 'react-router-dom';
// import 'Home.css';
import { useNavigate } from 'react-router-dom';
// import SearchFilter from '../SearchFilter';

import './Home.css';

const Home = async () => {

    
    const response = await fetch(`http://127.0.0.1:8000/api/schema/`);
    const RealEstate = response.json();
    

    const Name = "Barbod"
    const Navigate = useNavigate();

    return(
        <div className="homePage">
            <h1 className="name-header">Hello {Name}</h1>
            <button className='addition-button' onClick={() => (Navigate("/Home/Addition"))}>+</button>
                {RealEstate.map((item, index) => (
                    <Link to={`/Home/${item.id}`} key={item.id} >
                    <div className='Holder' key={index}>
                        {/* Use 'item.' instead of 'RealState.' */}
                        <img src={item.img} alt="Real estate item" className='home-list-picture'/>
                        <p className='Price-Tag'>Price: {item.price}</p>
                    </div>
                    </Link>
                ))}
            </div>
        // <h2>Hallo</h2>
    )
}

export default Home;