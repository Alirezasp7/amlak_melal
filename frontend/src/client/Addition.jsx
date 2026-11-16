import { useState } from "react";
import '../client/design/Addition.css'
import GoBackButton from '../components/GoBackButton';
import { useNavigate } from "react-router-dom";


const Addition = () => {

    const Navigate = useNavigate();

    const [propertyType, setPropertyType] = useState('office');
    const [ClientType, setClientType] = useState('buyer');

    const RoutingButton = () => {
        //office
        if(propertyType == 'office' && ClientType == 'buyer'){
            Navigate('/Home/Addition/OfficeBuy');
        }
        if(propertyType == 'office' && ClientType == 'seller'){
            Navigate('/Home/Addition/OfficeSell');
        }
        if(propertyType == 'office' && ClientType == 'tenant'){
            Navigate('/Home/Addition/OfficeTenant');
        }
        if(propertyType == 'office' && ClientType == 'landlord'){
            Navigate('/Home/Addition/OfficeLandlord');
        }
        //apartment
        if(propertyType == 'apartment' && ClientType == 'buyer'){
            Navigate('/Home/Addition/ApartmentBuy');
        }
        if(propertyType == 'apartment' && ClientType == 'seller'){
            Navigate('/Home/Addition/ApartmentSell');
        }
        if(propertyType == 'apartment' && ClientType == 'tenant'){
            Navigate('/Home/Addition/ApartmentTenant');
        }
        if(propertyType == 'apartment' && ClientType == 'landlord'){
            Navigate('/Home/Addition/Apartmentlandlord');
        }
        //commercial
        if(propertyType == 'commercial' && ClientType == 'buyer'){
            Navigate('/Home/Addition/CommercialBuy');
        }
        if(propertyType == 'commercial' && ClientType == 'seller'){
            Navigate('/Home/Addition/CommercialSell');
        }
        if(propertyType == 'commercial' && ClientType == 'tenant'){
            Navigate('/Home/Addition/CommercialTenant');
        }
        if(propertyType == 'commercial' && ClientType == 'landlord'){
            Navigate('/Home/Addition/CommercialLandlord');
        }
        // کلنگی
        if(propertyType == 'کلنگی' && ClientType == 'buyer'){
            Navigate('/Home/Addition/DemolitionBuy');
        }
        if(propertyType == 'کلنگی' && ClientType == 'seller'){
            Navigate('/Home/Addition/DemolitionSell');
        }
        if(propertyType == 'کلنگی' && ClientType == 'tenant'){
            alert("this isn't acceptable");
        }
        if(propertyType == 'کلنگی' && ClientType == 'landlord'){
            alert("this isn't acceptable");
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