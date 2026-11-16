import { Link } from "react-router-dom";
import './design/ConsultantInfo.css';

const ConsultantInfo = () => {

    const name = {name:'Alireza', lastName:'Sepandar'};
    const projectNumber = '30';
    const myProjectNumber = '10';
    const myDoneProjects = [{name:'A', price:'10'},{name:'b', price:'3'},
        {name:'c', price:'20'},{name:'d', price:'25'},{name:'e', price:'106'},];


    return (
        <div className="consultant-info">
            <h2 className="welcome-note">welcome {name.name}</h2>
            <img className="picture" src="/real-estate-logo.jpg" alt="my picture" />
            <h3 className="name">{name.name} {name.lastName}</h3>
            <p className="projects-number"><label htmlFor="">Projects: </label><span className="nuber">{projectNumber}</span></p>
            <p className="projects-number"><label htmlFor="">My Projects: </label><span className="nuber">{myProjectNumber}</span></p>
            <Link className="edit-button" to='/ConsultantInfo/EditProfile'>Edit Info</Link>
            <div className="my-done-projects">
                {myDoneProjects.map((item, index) => (
                    <div className="project-holder" key={index}>
                        <p className="project-title">{item.name}</p>
                        <p className="price">{item.price}</p>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default ConsultantInfo;