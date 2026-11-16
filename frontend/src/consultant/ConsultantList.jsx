import './design/ConsultantList.css';

const ConsultantList = () => {
    const myCosultants = [{name:'barbod', porjectNumber: '1003'},{name:'alireza', porjectNumber: '852'},
        {name:'sirus', porjectNumber: '1'},{name:'ahmad', porjectNumber: '10'},
    ]

    return(
        <div className="consultant-list">
            {myCosultants.map((item) => (
                <div className="container" key={item.name}>
                    <img src="/h" alt="consultant picture" />
                    <p className="name"><label htmlFor="name-">Name: </label>{item.name}</p>
                    <p className="project-number"><label htmlFor="project-number-">Number of done projects: </label>{item.porjectNumber}</p>
                </div>
            ))}
        </div>
    )
}
export default ConsultantList;