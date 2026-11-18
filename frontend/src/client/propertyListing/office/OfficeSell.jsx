import GoBackButton from "../../../components/GoBackButton.jsx";
import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import "../design/PropertyListing.css";
import Message from "../../../components/Message.jsx";

const OfficSell = () => {
    // vars for api
    const [picture1, setPicture1] = useState(null);
    const [picture2, setPicture2] = useState(null);
    const [picture3, setPicture3] = useState(null);
    const [picture4, setPicture4] = useState(null);
    const [picture5, setPicture5] = useState(null);
    const [district, setDistrict] = useState(null);
    const [address, setAddress] = useState("");
    const [exactArea, setExactArea] = useState(null);
    const [rooms, setRooms] = useState(null);
    const [yearBuilt, setYearBuilt] = useState(null);
    const [unitsPerFloor, setUnitsPerFloor] = useState(null);
    const [floor, setFloor] = useState(null);
    const [totalFloors, setTotalFloors] = useState(null);
    const [exactPrice, setExactPrice] = useState(null);
    const [deedStatus, setDeedStatus] = useState(null);
    const [hasElevator, setHasElevator] = useState(false);
    const [hasStorage, setHasStorage] = useState(false);
    const [hasParking, setHasParking] = useState(false);
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
            const response = await fetch("http://127.0.0.1:8000/requests/sell-office/", {
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
                    rooms: rooms,
                    year_built: yearBuilt,
                    units_per_floor: unitsPerFloor,
                    floor: floor,
                    total_floors: totalFloors,
                    exact_price: exactPrice,
                    deed_status: deedStatus,
                    has_elevator: hasElevator,
                    has_storage: hasStorage,
                    has_parking: hasParking,
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
                <p><label htmlFor="picture_1">Picture 1:</label> <input id="picture_1" name="picture_1" type="file" onChange={(e) => setPicture1(e.target.files[0])} /></p>
                <p><label htmlFor="picture_2">Picture 2:</label> <input id="picture_2" name="picture_2" type="file" onChange={(e) => setPicture2(e.target.files[0])} /></p>
                <p><label htmlFor="picture_3">Picture 3:</label> <input id="picture_3" name="picture_3" type="file" onChange={(e) => setPicture3(e.target.files[0])} /></p>
                <p><label htmlFor="picture_4">Picture 4:</label> <input id="picture_4" name="picture_4" type="file" onChange={(e) => setPicture4(e.target.files[0])} /></p>
                <p><label htmlFor="picture_5">Picture 5:</label> <input id="picture_5" name="picture_5" type="file" onChange={(e) => setPicture5(e.target.files[0])} /></p>
                <p><label htmlFor="district">District:</label> <input id="district" name="district" type="number" step={1} value={district ?? ""} onChange={(e) => setDistrict(Number(e.target.value))} /></p>
                <p><label htmlFor="address">Address:</label> <input id="address" name="address" type="text" value={address} onChange={(e) => setAddress(e.target.value)} /></p>
                <p><label htmlFor="exact_area">Exact area:</label> <input id="exact_area" name="exact_area" type="number" step={1} value={exactArea ?? ""} onChange={(e) => setExactArea(Number(e.target.value))} /> meter</p>
                <p><label htmlFor="rooms">Rooms:</label> <input
                    id="rooms" name="rooms"
                    max={15} min={0} step={1}
                    type="number"
                    value={rooms ?? ""}
                    onChange={(e) => (setRooms(Number(e.target.value)))} />
                </p>
                <p><label htmlFor="year_built">Year built:</label> <input id="year_built" name="year_built" type="number" step={1} value={yearBuilt ?? ""} onChange={(e) => setYearBuilt(Number(e.target.value))} /></p>
                <p><label htmlFor="units_per_floor">Units per floor:</label> <input id="units_per_floor" name="units_per_floor" type="number" step={1} value={unitsPerFloor ?? ""} onChange={(e) => setUnitsPerFloor(Number(e.target.value))} /></p>
                <p><label htmlFor="floor">Floor:</label> <input id="floor" name="floor" type="number" step={1} value={floor ?? ""} onChange={(e) => setFloor(Number(e.target.value))} /></p>
                <p><label htmlFor="total_floors">Total floors:</label> <input id="total_floors" name="total_floors" type="number" step={1} value={totalFloors ?? ""} onChange={(e) => setTotalFloors(Number(e.target.value))} /></p>
                <p><label htmlFor="exact_price">Exact price:</label> <input id="exact_price" name="exact_price" type="number" step={1} value={exactPrice ?? ""} onChange={(e) => setExactPrice(Number(e.target.value))} /></p>
                <p><label htmlFor="deed_status">Deed status:</label> <input id="deed_status" name="deed_status" type="number" value={deedStatus ?? ""} onChange={(e) => setDeedStatus(Number(e.target.value))} /></p>
                <p><label htmlFor="has_parking">Parking?</label> <input id="has_parking" name="has_parking" type="checkbox" checked={hasParking} onChange={(e) => setHasParking(e.target.checked)} /></p>
                <p><label htmlFor="has_elevator">Elevator?</label> <input id="has_elevator" name="has_elevator" type="checkbox" checked={hasElevator} onChange={(e) => setHasElevator(e.target.checked)} /></p>
                <p><label htmlFor="has_storage">Storage?</label> <input id="has_storage" name="has_storage" type="checkbox" checked={hasStorage} onChange={(e) => setHasStorage(e.target.checked)} /></p>
                <p><label htmlFor="description">Description:</label> <textarea id="description" name="description" value={description} onChange={(e) => setDescription(e.target.value)} /></p>
                <input value={"Add?"} onClick={() => (AdditionButton())} type="button" />
            </div>
        </>
    );
};

export default OfficSell;