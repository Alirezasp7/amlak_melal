import GoBackButton from "../../../components/GoBackButton.jsx";
import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import "../design/PropertyListing.css";
import Message from "../../../components/Message.jsx";

const CommercialTenant = () => {
    // vars for api
    const [district, setDistrict] = useState(null);
    const [minArea, setMinArea] = useState(null);
    const [maxArea, setMaxArea] = useState(null);
    const [rooms, setRooms] = useState(null);
    const [yearBuilt, setYearBuilt] = useState(null);
    const [minDeposit, setMinDeposit] = useState(null);
    const [maxDeposit, setMaxDeposit] = useState(null);
    const [minMonthlyRent, setMinMonthlyRent] = useState(null);
    const [maxMonthlyRent, setMaxMonthlyRent] = useState(null);
    const [hasElevator, setHasElevator] = useState(false);
    const [hasParking, setHasParking] = useState(false);
    const [hasStorage, setHasStorage] = useState(false);
    const [description, setDescription] = useState("");
    //navigation
    const Navigate = useNavigate();
    //send data function vars
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
            const response = await fetch("http://127.0.0.1:8000/requests/rent-commercial/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    district: district,
                    min_area: minArea,
                    max_area: maxArea,
                    rooms: rooms,
                    year_built: yearBuilt,
                    min_deposit: minDeposit,
                    max_deposit: maxDeposit,
                    min_monthly_rent: minMonthlyRent,
                    max_monthly_rent: maxMonthlyRent,
                    has_elevator: hasElevator,
                    has_parking: hasParking,
                    has_storage: hasStorage,
                    description: description

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
            setMessage(`Error: ${error}`);
        } finally {
            setIsSending(false);
        }
    };

    const AdditionButton = () => {
        sendData();
    };

    useEffect(() => {
        if (!isSending) {
            const timer = setTimeout(() => {
                setDisplay('none');
            }, 3000);

        return () => clearTimeout(timer);
        }
    }, [isSending]);

    useEffect(() => {
        if (!added) {
            return;
        }

        const timeoutId = setTimeout(() => {
            Navigate(-1);
        }, 4000);

        return () => clearTimeout(timeoutId);
    }, [added, Navigate]);

    console.log(rooms);
    return (
        <>
            <Message message={message} visibility={display} />
            <GoBackButton />
            <div className="addition-page">
                <p><label htmlFor="district">District:</label> <input id="district" name="district" type="number" step={1} value={district ?? ""} onChange={(e) => setDistrict(Number(e.target.value))} /></p>
                <p><label htmlFor="min_area">Minimum area:</label> <input id="min_area" name="min_area" type="number" step={0.1} value={minArea ?? ""} onChange={(e) => setMinArea(Number(e.target.value))} /> meter</p>
                <p><label htmlFor="max_area">Maximum area:</label> <input id="max_area" name="max_area" type="number" step={0.1} value={maxArea ?? ""} onChange={(e) => setMaxArea(Number(e.target.value))} /> meter</p>
                <p><label htmlFor="rooms">Rooms:</label> <input
                    id="rooms" name="rooms"
                    max={15} min={0} step={1}
                    type="number"
                    value={rooms ?? ""}
                    onChange={(e) => (setRooms(Number(e.target.value)))} />
                </p>
                <p><label htmlFor="year_built">Year built:</label> <input id="year_built" name="year_built" type="number" step={1} value={yearBuilt ?? ""} onChange={(e) => setYearBuilt(Number(e.target.value))} /></p>
                <p><label htmlFor="min_deposit">Minimum deposit:</label> <input id="min_deposit" name="min_deposit" type="number" step={1} value={minDeposit ?? ""} onChange={(e) => setMinDeposit(Number(e.target.value))} /></p>
                <p><label htmlFor="max_deposit">Maximum deposit:</label> <input id="max_deposit" name="max_deposit" type="number" step={1} value={maxDeposit ?? ""} onChange={(e) => setMaxDeposit(Number(e.target.value))} /></p>
                <p><label htmlFor="min_monthly_rent">Minimum monthly rent:</label> <input id="min_monthly_rent" name="min_monthly_rent" type="number" step={1} value={minMonthlyRent ?? ""} onChange={(e) => setMinMonthlyRent(Number(e.target.value))} /></p>
                <p><label htmlFor="max_monthly_rent">Maximum monthly rent:</label> <input id="max_monthly_rent" name="max_monthly_rent" type="number" step={1} value={maxMonthlyRent ?? ""} onChange={(e) => setMaxMonthlyRent(Number(e.target.value))} /></p>
                <p><label htmlFor="has_elevator">Elevator?</label> <input id="has_elevator" name="has_elevator" type="checkbox" checked={hasElevator} onChange={(e) => setHasElevator(e.target.checked)} /></p>
                <p><label htmlFor="has_parking">Parking?</label> <input id="has_parking" name="has_parking" type="checkbox" checked={hasParking} onChange={(e) => setHasParking(e.target.checked)} /></p>
                <p><label htmlFor="has_storage">Storage?</label> <input id="has_storage" name="has_storage" type="checkbox" checked={hasStorage} onChange={(e) => setHasStorage(e.target.checked)} /></p>
                <p><label htmlFor="description">Description:</label> <textarea id="description" name="description" value={description} onChange={(e) => setDescription(e.target.value)} /></p>
                <input value={"Add?"} onClick={() => (AdditionButton())} type="button" />
            </div>
        </>
    );
};

export default CommercialTenant;