import { useState } from "react";

const Filter = () => {

    const testArray = [{name:'A', price:'10', clientType:'rent', propertyType:'office'}];

    const filtered = testArray.filter(testArray.propertyType == `${propertyTypeFilter}` 
        && testArray.clientType == `${clientTypeFilter}`
        && Number(testArray.price) > maxPrice && Number(testArray.price) < minPrice);

    const [minPrice, setMinPrice] = useState(null);
    const [maxPrice, setMaxPrice] = useState(null);
    const [propertyTypeFilter, setPropertyTypeFilter] = useState('');
    const [clientTypeFilter, setClientTypeFilter] = useState('');

    console.log('client:', clientTypeFilter);
    console.log('property:', propertyTypeFilter);
    return(
        <div>
            <div>
                <p> property type:
                    <select className="select-form" value={propertyTypeFilter} onChange={(e) => setPropertyTypeFilter(e.target.value)}>
                        <option value='all'>all</option>
                        <option value='apartment'>apartment</option>
                        <option value='office'>office</option>
                        <option value='comercial'>comercial</option>
                        <option value='demolition'>demolition</option>
                    </select>
                </p>
            </div>
            <div>
                <p> Client type:
                    <select className="select-form" value={clientTypeFilter} onChange={(e) => setClientTypeFilter(e.target.value)}>
                        <option value='seller'>seller</option>
                        <option value='all'>all</option>
                        <option value='buyer'>buyer</option>
                        <option value='tenant'>tenant</option>
                        <option value='landlord'>landlord</option>
                    </select>
                </p>
            </div>
            <div>
                <p>min: <input value={minPrice} type="number" onChange={(e) => setMinPrice(e.target.value)} />billion</p>
                <p>max: <input value={maxPrice} type="number" onChange={(e) => setMaxPrice(e.target.value)}/>billion</p>
            </div>
        </div>
    )
}
export default Filter;