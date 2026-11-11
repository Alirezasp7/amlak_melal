import './design/Message.css';

const Message = ({message, visibility}) => {
    return  <div className='container' style={{display:`${visibility}`}}>
                <div className="message-box">{message}</div>
            </div>
}
export default Message;