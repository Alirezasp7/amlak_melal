import ConsultantInfo from "../components/ConsultantInfo";
import { useState } from "react";
import './design/ConsultantHome.css'

const ConsultantHome = () => {
    const myDoneProjects = [{name:'A', price:'10', type:'rent'},{name:'b', price:'3', type:'rent'},
        {name:'c', price:'20', type:'rent'},{name:'d', price:'25', type:'rent'},{name:'e', price:'106', type:'rent'},
        {name:'f', price:'23', type:'rent'},{name:'g', price:'56', type:'rent'}];

    const [openItems, setOpenItems] = useState([]);

    const toggle = (name) =>
      setOpenItems((prev) =>
        prev.includes(name) ? prev.filter((n) => n !== name) : [...prev, name]
      );

return (
    <div className="consultant-home">
        <ConsultantInfo />

        <div className="project-list">
            <div className="my-done-projects">

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
                            </div>
                        </div>
                    );
                })}

            </div>
        </div>
    </div>
);
}

export default ConsultantHome;