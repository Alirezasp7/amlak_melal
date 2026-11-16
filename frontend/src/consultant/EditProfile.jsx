import GoBackButton from '../components/GoBackButton'
import './design/EditProfile.css';

const EditProfile = () => {
    return(
        <>
            <GoBackButton/>
            <div className='e'>
                <p>Name<input type="text" /></p>
            <button>change</button>
        </div>

        </>
    )
}
export default EditProfile;