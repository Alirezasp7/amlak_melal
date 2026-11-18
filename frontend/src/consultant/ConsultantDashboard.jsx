import './design/ConsultantHome.css'
import { useState } from 'react';
import Filter from '../components/Filter';

const ConsultantDashboard = () => {

    const myDoneProjects = [{name:'A', price:'10', type:'rent'},{name:'b', price:'3', type:'rent'},
        {name:'c', price:'20', type:'rent'},{name:'d', price:'25', type:'rent'},{name:'e', price:'106', type:'rent'},
        {name:'f', price:'23', type:'rent'},{name:'g', price:'56', type:'rent'}];

        const [openItems, setOpenItems] = useState([]);
    
    const toggle = (name) =>
        setOpenItems((prev) =>
          prev.includes(name) ? prev.filter((n) => n !== name) : [...prev, name]
        );
    
    return (
        <div>
            {myDoneProjects.map((item, index) => {
                const isOpen = openItems.includes(item.name);

                return (
                    <div className={`project-holder ${isOpen ? "open" : ""}`} key={index}>
                        <div className="top-holder">
                            <p className="project-title">{item.name}</p>
                            <p className="price">price: {item.price}</p>
                            <button
                                className="more-info-b"
                                aria-expanded={isOpen}
                                onClick={() => toggle(item.name)}
                            >
                                {isOpen ? 'show less' : 'show more'}
                            </button>
                        </div>
                        <div className="secondry-holder">
                            <p>Type: {item.type}</p>
                            <button>Enter</button>
                        </div>
                    </div>
                );
            })}        
        </div>
    )
}
export default ConsultantDashboard