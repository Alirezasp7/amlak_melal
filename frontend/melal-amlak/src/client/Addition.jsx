import NavigateBackButton from "../NavigationButton";
import { useNavigate } from "react-router-dom";

const Addition = () => {

const AdditionButton = () => {
    Navigate(-1);
    console.log('added');
}

const Navigate = useNavigate();

    return(
        <div className="addition-page">

            <p>Picture1:<input type="file"></input></p>
            <p>Picture2:<input type="file"></input></p>
            <p>Picture3:<input type="file"></input></p>
            <p>Price:<input type="number"></input></p>
            <p>Add?<input onClick={() => (AdditionButton())} type="button"></input></p>
        </div>
    )
}

export default Addition;