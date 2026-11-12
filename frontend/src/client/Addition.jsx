import { useState } from "react";
import '../client/design/Addition.css'
import GoBackButton from '../components/GoBackButton';
import { useNavigate } from "react-router-dom";


const Addition = () => {


    const [propertyType, setPropertyType] = useState('office');
    const [ClientType, setClientType] = useState('buyer');

    const RoutingButton = ()=> {
        //office
        if(propertyType == 'office' && ClientType == 'buyer'){
            console.log(propertyType," ",ClientType);
        }
        if(propertyType == 'office' && ClientType == 'seller'){
            console.log(propertyType," ",ClientType);
        }
        if(propertyType == 'office' && ClientType == 'tenant'){
            console.log(propertyType," ",ClientType);
        }
        if(propertyType == 'office' && ClientType == 'landlord'){
            console.log(propertyType," ",ClientType);
        }
        //apartment
        if(propertyType == 'apartment' && ClientType == 'buyer'){
            console.log(propertyType," ",ClientType);
        }
        if(propertyType == 'apartment' && ClientType == 'seller'){
            console.log(propertyType," ",ClientType);
        }
        if(propertyType == 'apartment' && ClientType == 'tenant'){
            console.log(propertyType," ",ClientType);
        }
        if(propertyType == 'apartment' && ClientType == 'landlord'){
            console.log(propertyType," ",ClientType);
        }
        //commercial
        if(propertyType == 'commercial' && ClientType == 'buyer'){
            console.log(propertyType," ",ClientType);
        }
        if(propertyType == 'commercial' && ClientType == 'seller'){
            console.log(propertyType," ",ClientType);
        }
        if(propertyType == 'commercial' && ClientType == 'tenant'){
            console.log(propertyType," ",ClientType);
        }
        if(propertyType == 'commercial' && ClientType == ''){
            console.log(propertyType," ",ClientType);
        }
        // کلنگی
        if(propertyType == 'کلنگی' && ClientType == 'buyer'){
            console.log(propertyType," ",ClientType);
        }
        if(propertyType == 'کلنگی' && ClientType == 'seller'){
            console.log(propertyType," ",ClientType);
        }
        if(propertyType == 'کلنگی' && ClientType == 'tenant'){
            alert("this isn't acceptable");
        }
        if(propertyType == 'کلنگی' && ClientType == 'landlord'){
            alert("this isn't acceptable");
        }
        // checkup
        if(propertyType == '' || ClientType == ''){
            alert('Feilds cannot be empty');
        }
    }


    return(
        <>
        <GoBackButton />
        <div className="addition-page">
            <div className="listing-type-container">
                <p> Listing type:
                    <select className="select-form" value={propertyType} onChange={(e) => setPropertyType(e.target.value)}>
                        <option value="office">Office</option>
                        <option value="apartment">Apartment</option>
                        <option value="commercial">Commercial</option>
                        <option value="کلنگی">کلنگی</option>
                    </select>
                </p>
            </div>
            <div className="listing-type-container">
                <p>Client:
                    <select className="select-form" value={ClientType} onChange={(e) => setClientType(e.target.value)}>
                        <option value="buyer">Buyer</option>
                        <option value="seller">Seller</option>
                        <option value="landLord">Landlord</option>
                        <option value="tenant">Tenant</option>
                    </select>
                </p>
            </div>
            <button onClick={()=> (RoutingButton())}>Confirm</button>
        </div>
        </>
    )
}
export default Addition;