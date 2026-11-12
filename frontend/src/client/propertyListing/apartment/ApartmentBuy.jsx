import GoBackButton from "../components/GoBackButton";
import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import "./design/ApartmentBuy.css";
import Message from "../components/Message";

const ApartmentBuy = () => {
    const [hasParking, setHasParking] = useState(false);
    const [hasElevator, setHasElevator] = useState(false);
    const [bedroomNumber, setBedroomNumber] = useState(0);
    const [propertyType, setPropertyType] = useState("");
    const Navigate = useNavigate();

    const [message, setMessage] = useState("Sending...");
    const [display, setDisplay] = useState("none");
    const [added, setAdded] = useState(false);
    const [error, setError] = useState(null);
    const [isSending, setIsSending] = useState(false);

    const sendData = async () => {
        if (isSending || added) {
            return;
        }

        setIsSending(true);
        setDisplay("block");
        setMessage("Sending...");
        setError(null);

        try {
            const response = await fetch("http://localhost:8001/realEstate", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    elevator:hasElevator
                }),
            });

            if (!response.ok) {
                throw new Error(`Request failed with status ${response.status}`);
            }

            setMessage("Added.");
            setAdded(true);
        } catch (err) {
            const errorMessage = err instanceof Error ? err.message : "An unknown error occurred";
            setError(errorMessage);
            setMessage("Failed to add.");
        } finally {
            setIsSending(false);
        }
    };

    const AdditionButton = () => {
        // if (bedroomNumber >= 10) {
        //     alert("bedroom number should be less than 10");
        // } else if (bedroomNumber <= 0) {
        //     alert("bedroom number should be higher or equal to 0");
        // }

        sendData();
    };

    useEffect(() => {
        if (error) {
            alert(`Error: ${error}`);
        }
    }, [error]);

    useEffect(() => {
        if (!added) {
            return;
        }

        const timeoutId = setTimeout(() => {
            Navigate(-1);
        }, 7000);

        return () => clearTimeout(timeoutId);
    }, [added, Navigate]);

    console.log(propertyType);
    console.log("Parking: ", hasParking);
    console.log("bedroom number", bedroomNumber);

    return (
        <>
            <Message message={message} visibility={display} />
            <GoBackButton />
            <div className="addition-page">
                <h3>Title: <input type="text" /></h3>
                <p>Picture1:<input type="file" accept="image/*"></input></p>
                <p>Picture2:<input type="file" accept="image/*"></input></p>
                <p>Picture3:<input type="file" accept="image/*"></input></p>
                <p>Picture4:<input type="file" accept="image/*"></input></p>
                <p>Picture5:<input type="file" accept="image/*"></input></p>
                <p>Price:<input type="number" min={0.5} max={100000}></input>billion</p>
                <p>type:
                    <select value={propertyType} onChange={(e) => setPropertyType(e.target.value)}>
                        <option value="Office">Office</option>
                        <option value="Apartment">Apartment</option>
                        <option value="Commercial">Commercial</option>
                        <option value="کلنگی">کلنگی</option>
                    </select>
                </p>
                <p>area: <input type="number" />meter</p>
                <p>bedroom: <input value={bedroomNumber} type="number" onChange={(e) => (setBedroomNumber(e.target.value))}/></p>
                <p>Parking? <input type="checkbox" checked={hasParking} onChange={(e) => (setHasParking(e.target.checked))}/></p>
                <p>Elevator? <input type="checkbox" checked={hasElevator} onChange={(e) => (setHasElevator(e.target.checked))}/></p>
                <p>Year built: <input type="number" /></p>
                <input value={"Add?"} onClick={() => (AdditionButton())} type="button" />
            </div>
        </>
    );
};

export default Addition;
