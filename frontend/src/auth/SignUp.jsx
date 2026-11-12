import { useState } from "react";
import '../auth/design/auth.css';

const SignUp = () => {
    const [phoneNumber, setPhoneNumber] = useState('0916...');
    const [password, setPassword] = useState('0');
    return(
        <div className="auth-page">
            <h2>Sign Up</h2>
            <div className="container">
                <p>Phone number:<input  type="text" value={phoneNumber} onChange={(e) => (setPhoneNumber(e.target.value))}/></p>
                <p>password:<input type="password" value={password} onChange={(e) => (setPassword(e.target.value))}/></p>
                <button className="sign-up-button">Confirm</button>
            </div>
        </div>
    )
}

export default SignUp;