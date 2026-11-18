
import GoBackButton from "../../../components/GoBackButton.jsx";
import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import "../design/PropertyListing.css";
import Message from "../../../components/Message.jsx";

const ApartmentLandlord = () => {
    // vars for api
    const [picture1, setPicture1] = useState(null);
    const [picture2, setPicture2] = useState(null);
    const [picture3, setPicture3] = useState(null);
    const [picture4, setPicture4] = useState(null);
    const [picture5, setPicture5] = useState(null);
    const [district, setDistrict] = useState(null);
    const [address, setAddress] = useState("");
    const [exactArea, setExactArea] = useState(null);
    const [bedroomNumber, setBedroomNumber] = useState(null);
    const [floor, setFloor] = useState(null);
    const [totalFloors, setTotalFloors] = useState(null);
    const [yearBuilt, setYearBuilt] = useState(null);
    const [exactDeposit, setExactDeposit] = useState(null);
    const [exactMonthlyRent, setExactMonthlyRent] = useState(null);
    const [minDeposit, setMinDeposit] = useState(null);
    const [maxDeposit, setMaxDeposit] = useState(null);
    const [minMonthlyRent, setMinMonthlyRent] = useState(null);
    const [maxMonthlyRent, setMaxMonthlyRent] = useState(null);
    const [isConvertible, setIsConvertible] = useState(false);
    const [hasElevator, setHasElevator] = useState(false);
    const [hasParking, setHasParking] = useState(false);
    const [hasStorage, setHasStorage] = useState(false);
    const [hasBalcony, setHasBalcony] = useState(false);
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
            const response = await fetch("http://127.0.0.1:8000/requests/lease-apartment/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    picture_1: picture1,
                    picture_2: picture2,
                    picture_3: picture3,
                    picture_4: picture4,
                    picture_5: picture5,
                    district: district,
                    address: address,
                    exact_area: exactArea,
                    bedrooms: bedroomNumber,
                    floor: floor,
                    total_floors: totalFloors,
                    year_built: yearBuilt,
                    exact_deposit: exactDeposit,
                    exact_monthly_rent: exactMonthlyRent,
                    min_deposit: minDeposit,
                    max_deposit: maxDeposit,
                    min_monthly_rent: minMonthlyRent,
                    max_monthly_rent: maxMonthlyRent,
                    is_convertible: isConvertible,
                    has_elevator: hasElevator,
                    has_parking: hasParking,
                    has_storage: hasStorage,
                    has_balcony: hasBalcony,
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

    console.log(bedroomNumber);
    return (
        <>
            <Message message={message} visibility={display} />
            <GoBackButton />
            <div className="addition-page">
                {/* image input */}
                <p><label htmlFor="picture_1">Picture 1:</label> <input id="picture_1" name="picture_1" type="file" accept="image/*" onChange={(e) => setPicture1(e.target.files?.[0] ?? null)} /></p>
                <p><label htmlFor="picture_2">Picture 2:</label> <input id="picture_2" name="picture_2" type="file" accept="image/*" onChange={(e) => setPicture2(e.target.files?.[0] ?? null)} /></p>
                <p><label htmlFor="picture_3">Picture 3:</label> <input id="picture_3" name="picture_3" type="file" accept="image/*" onChange={(e) => setPicture3(e.target.files?.[0] ?? null)} /></p>
                <p><label htmlFor="picture_4">Picture 4:</label> <input id="picture_4" name="picture_4" type="file" accept="image/*" onChange={(e) => setPicture4(e.target.files?.[0] ?? null)} /></p>
                <p><label htmlFor="picture_5">Picture 5:</label> <input id="picture_5" name="picture_5" type="file" accept="image/*" onChange={(e) => setPicture5(e.target.files?.[0] ?? null)} /></p>
                {/* //  */}
                <p><label htmlFor="district">District:</label> <input id="district" name="district" type="number" step={1} value={district ?? ""} onChange={(e) => setDistrict(Number(e.target.value))} /></p>
                <p><label htmlFor="address">Address:</label> <input id="address" name="address" type="text" value={address} onChange={(e) => setAddress(e.target.value)} /></p>
                <p><label htmlFor="exact_area">Exact area:</label> <input id="exact_area" name="exact_area" type="number" step={1} value={exactArea ?? ""} onChange={(e) => setExactArea(Number(e.target.value))} /> meter</p>
                <p><label htmlFor="bedrooms">Bedrooms:</label> <input
                    id="bedrooms" name="bedrooms"
                    max={15} min={0} step={1}
                    type="number"
                    value={bedroomNumber}
                    onChange={(e) => (setBedroomNumber(e.target.value))} />
                </p>
                <p><label htmlFor="floor">Floor:</label> <input id="floor" name="floor" type="number" step={1} value={floor ?? ""} onChange={(e) => setFloor(Number(e.target.value))} /></p>
                <p><label htmlFor="total_floors">Total floors:</label> <input id="total_floors" name="total_floors" type="number" step={1} value={totalFloors ?? ""} onChange={(e) => setTotalFloors(Number(e.target.value))} /></p>
                <p><label htmlFor="year_built">Year built:</label> <input id="year_built" name="year_built" type="number" step={1} value={yearBuilt ?? ""} onChange={(e) => setYearBuilt(Number(e.target.value))} /></p>
                <p><label htmlFor="exact_deposit">Exact deposit:</label> <input id="exact_deposit" name="exact_deposit" type="number" step={0.1} value={exactDeposit ?? ""} onChange={(e) => setExactDeposit(Number(e.target.value))} /></p>
                <p><label htmlFor="exact_monthly_rent">Exact monthly rent:</label> <input id="exact_monthly_rent" name="exact_monthly_rent" type="number" step={0.1} value={exactMonthlyRent ?? ""} onChange={(e) => setExactMonthlyRent(Number(e.target.value))} /></p>
                <p><label htmlFor="min_deposit">Minimum deposit:</label> <input id="min_deposit" name="min_deposit" type="number" step={0.1} value={minDeposit ?? ""} onChange={(e) => setMinDeposit(Number(e.target.value))} /></p>
                <p><label htmlFor="max_deposit">Maximum deposit:</label> <input id="max_deposit" name="max_deposit" type="number" step={0.1} value={maxDeposit ?? ""} onChange={(e) => setMaxDeposit(Number(e.target.value))} /></p>
                <p><label htmlFor="min_monthly_rent">Minimum monthly rent:</label> <input id="min_monthly_rent" name="min_monthly_rent" type="number" step={0.1} value={minMonthlyRent ?? ""} onChange={(e) => setMinMonthlyRent(Number(e.target.value))} /></p>
                <p><label htmlFor="max_monthly_rent">Maximum monthly rent:</label> <input id="max_monthly_rent" name="max_monthly_rent" type="number" step={0.1} value={maxMonthlyRent ?? ""} onChange={(e) => setMaxMonthlyRent(Number(e.target.value))} /></p>
                <p><label htmlFor="is_convertible">Is convertible?</label> <input id="is_convertible" name="is_convertible" type="checkbox" checked={isConvertible} onChange={(e) => setIsConvertible(e.target.checked)} /></p>
                <p><label htmlFor="has_parking">Parking?</label> <input id="has_parking" name="has_parking" type="checkbox" checked={hasParking} onChange={(e) => setHasParking(e.target.checked)} /></p>
                <p><label htmlFor="has_elevator">Elevator?</label> <input id="has_elevator" name="has_elevator" type="checkbox" checked={hasElevator} onChange={(e) => setHasElevator(e.target.checked)} /></p>
                <p><label htmlFor="has_balcony">Balcony?</label> <input id="has_balcony" name="has_balcony" type="checkbox" checked={hasBalcony} onChange={(e) => setHasBalcony(e.target.checked)} /></p>
                <p><label htmlFor="has_storage">Storage?</label> <input id="has_storage" name="has_storage" type="checkbox" checked={hasStorage} onChange={(e) => setHasStorage(e.target.checked)} /></p>
                <p><label htmlFor="description">Description:</label> <textarea id="description" name="description" value={description} onChange={(e) => setDescription(e.target.value)} /></p>
                <input value={"Add?"} onClick={() => (AdditionButton())} type="button" />
            </div>
        </>
    );
};

export default ApartmentLandlord;
