import { useState } from "react";
import '../auth/design/auth.css';

const LogIn = () => {
    const [phoneNumber, setPhoneNumber] = useState('0916...');
    const [password, setPassword] = useState('');
    return(
        <div className="auth-page">
            <h3>Sign In</h3>
            <div className="container">
                <p>Phone number:<input  type="text" value={phoneNumber} onChange={(e) => (setPhoneNumber(e.target.value))}/></p>
                <p>password:<input type="password" value={password} onChange={(e) => (setPassword(e.target.value))}/></p>
                <button>Confirm</button>
            </div>
        </div>
    )
}

export default LogIn;