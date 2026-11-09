import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
// import SearchFilter from '../SearchFilter';
import { useState, useEffect } from 'react';
import './design/Home.css';

const ApiListResposnse = () => {

    const [list, setList] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null)
    const apiIsEmpty = list.length === 0;

    const fetchUsers = async () => {
            try {
                const response = await fetch('http://localhost:8000/realEstates', {method:"GET"});

                if (!response.ok) {
                    throw new Error('Failed to fetch list');
                }

                const RealEstates = await response.json();
                setList(RealEstates);
                console.log(list);
                console.log('type:', typeof list);
                console.log(Array.isArray(list));

            } catch (err) {
                setError(err.message);

            } finally {
                setLoading(false);
            } 
    };


    useEffect(() => {
        fetchUsers();

    },[])

    if (loading) {
        return <h2>Loading...</h2>;
    }
    if (error) {
        return <h2>Error: {error}</h2>;
    }
    if(apiIsEmpty) {
        return <h2>an error has occured.</h2>
    }
    return (
        <>
        {list.map((item, index) => (
            <Link to={`/Home/${item.id}`} key={item.id} >
                <div className='Holder' key={index}>
                    <img src={item.img1} alt="Real estate item" className='home-list-picture'/>
                    <p className='Price-Tag'>Price: {item.price}</p>
                </div>
            </Link>
        ))}
        </>
    )
}

const Home = () => {

    const Name = "Barbod"
    const Navigate = useNavigate();

    return(
        <div className="homePage">
            <h1 className="name-header">Hello {Name}</h1>
            <button className='addition-button' onClick={() => (Navigate("/Home/Addition"))}>+</button>
            <ApiListResposnse />
        </div>
    )
}


export default Home;