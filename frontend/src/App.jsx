import './App.css';
import Client from './userPanels/Client';
import Consultant from './userPanels/Consultant';

function App() {

  const userType = 'consultant';

  if(userType == 'client') {
    return <Client/>
  }
  if(userType == 'consultant') {
    return <Consultant/>
  }
  else {
    return <h1>Error</h1>
  }
}

export default App;