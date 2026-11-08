import { useParams } from "react-router-dom";
import { useEffect,useState } from "react";

const Detail = () => {
    return <ApiDetailResposnse/>
}

const ApiDetailResposnse = () => {

    const { id } = useParams();
    const [list, setList] = useState([]);
    const property = list.find((item) => item.id === Number(id));
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null)
    const fetchUsers = async () => {
            try {
                const response = await fetch('http://localhost:8001/RealEtateList');

                if (!response.ok) {
                    throw new Error('Failed to fetch users');
                }

                const RealEstates = await response.json();
                setList(RealEstates);

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
    // if(property) {
        return(       
            <div className='Detail-page'>
                <img className='picture' src={`/${property.img}`} alt="Real estate item"></img>
                <img className='picture' src={`/${property.img2}`} alt="Real estate item"></img>
                <img className='picture' src={`/${property.img3}`} alt="Real estate item"></img>
                <h2 className='Price'>{property.price}</h2>
                {property.elavator ? <p className='Ckeck-P'>elavator:true</p> : <p className='Ckeck-P'>elavator:false</p>}
                {property.parking ? <p className='Ckeck-P'>parking:true</p> : <p className='Ckeck-P'>parking:false</p>}
            </div>
        )
    // }
    // else {
    //     return <h2>property not found!</h2>
    // }
}

export default Detail;