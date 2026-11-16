import { useState, useEffect } from "react";
import './design/ClientDashboard.css';

const ClientDashboard = () => {

    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [list, setList] = useState([]);
    const apiIsEmpty = list.length === 0;

    const fetchClientList = async () => {
        
        try {
            const response = await fetch('http://localhost:8000/api/', {method:"GET"});

            if (!response.ok) {
                throw new Error('Failed to fetch list');
            }

            const DashboardList = await response.json();
            setList(DashboardList);

        } catch (err) {
            setError(err.message);

        } finally {
            setLoading(false);
        } 
    }


    useEffect(() => {
        fetchClientList();
    },[])



    if (loading) {
        return <h2>Loading...</h2>;
    }
    if (error) {
        return <h2>Error: {error}</h2>;
    }
    if(apiIsEmpty) {
        return <h2>Error: List is empty.</h2>
    }
    return (
        <div className='placement'>
        {list.map((item, index) => (
            <Link to={`/ClientDashboard/${item.id}`} key={item.id} >
                <div className='Holder' key={index}>
                    <img src={item.img1} alt="Real estate item" className='list-picture'/>
                    <p className='real-estate-title'>{item.title}</p>
                    <p className='Price-Tag'>Price: {item.price}</p> 
                    <p className='real-estate-district'>{item.district}</p>
                    <p className='real-estate-listing-type'>{item.listing_type}</p>
                    
                </div>
            </Link>
        ))}
        </div>
    )
}

export default ClientDashboard;