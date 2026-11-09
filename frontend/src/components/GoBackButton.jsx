import { useNavigate } from "react-router-dom";
import './design/GoBackButton.css';
const GoBackButton = () => {
    const Navigate = useNavigate();
    
    return <button className="B" onClick={() => (Navigate(-1))}>Go Back</button>
}

export default GoBackButton;