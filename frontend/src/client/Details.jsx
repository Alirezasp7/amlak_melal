import { useParams } from "react-router-dom";
import { useEffect,useState } from "react";
import GoBackButton from "../components/GoBackButton";

const Details = () => {
    return(
        <>
            <GoBackButton/>
            <ApiDetailResposnse />
        </>
    )
}

const ApiDetailResposnse = () => {

    const { id } = useParams();
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [property, setProperty] = useState(null);

    const fetchUsers = async () => {
            try {
                const response = await fetch(`http://localhost:8000/api/v1/public-filings`, {method:"GET"});

                if (!response.ok) {
                    throw new Error('Failed to fetch details');
                }

                const RealEstate = await response.json();
                const selectedEstate = RealEstate.find(item => String(item.id) === id);
                setProperty(selectedEstate);
                console.log(id);


            } catch (err) {
                setError(err.message);

            } finally {
                setLoading(false);
            }
        };


    useEffect(() => {
        fetchUsers();
    },[id])

    if (loading) {
        return <h2>Loading...</h2>;
    }
    if (error) {
        return <h2>Error: {error}</h2>;
    }
    if(property) {
        return(       
            <div className='Detail-page'>
                <img className='picture' src={`/${property.img1}`} alt="Real estate item"></img>
                <h2 className='Price'>{property.price}</h2>
                {/* {property.elavator ? <p className='Ckeck-P'>elavator:true</p> : <p className='Ckeck-P'>elavator:false</p>}
                {property.parking ? <p className='Ckeck-P'>parking:true</p> : <p className='Ckeck-P'>parking:false</p>} */}
            </div>
        )
    }
    else {
        return <h2>property not found!</h2>
    }
}

export default Details;
