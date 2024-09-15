import './App.css';
// import About from './components/About';
import Navbar from './components/Navbar';
import TextForm from './components/TextForms';
import React, { useState } from 'react';
import Alert from './components/Alert';
// import {
//   BrowserRouter as Router,
//   Switch,
//   Route,
//   // Link
// } from "react-router-dom";


function App() {
  const [mode, setMode] = useState('light'); //whether dark mode is enabled or not
  const [modeText, setmodeText] = useState("Enable Dark Mode");
  const [alert, setAlert] = useState(null);

  const showAlert = (message, type) => {
    setAlert({
      msg: message,
      type: type,
    })
    setTimeout(() => {
      setAlert(null);
    }, 2000);
  }

  const toggleModef = () => {
    if (mode === 'light') {
      setMode("dark");
      setmodeText("Enable Light Mode");
      document.body.style.backgroundColor = "grey";
      document.body.style.color = "white";
      showAlert("Dark mode has been enabled", "success");
      document.title = "TextUtils - Dark Mode";
      setInterval(() => {
        document.title = "install textutils app";
      }, 2000);
      setInterval(() => {
        document.title = "textutils is best text manuplator";
      }, 1500);
    }
    else {
      setMode("light");
      setmodeText("Enable Dark Mode");
      document.body.style.backgroundColor = "white";
      document.body.style.color = "black";
      showAlert("Light mode has been enabled", "success");
      document.title = "TextUtils - Light Mode";
    }
  }
  return (
    <>
      {/* <Router> */}
        <Navbar title="Textutils" abouttext="about us" mode={mode} toggleMode={toggleModef} modeText={modeText}></Navbar>
        <Alert alert={alert}></Alert>
        {/* <Switch>
          <Route exact path="/about"> */}
            {/* <About></About> */}
          {/* </Route>
          <Route exact path="/"> */}
            <TextForm heading="Enter the text to analyze below" showAlert={showAlert}></TextForm>
          {/* </Route>
        </Switch> */}
        {/* <TextForm heading="Enter the text to analyze below" showAlert={showAlert}></TextForm>
      <About></About> */}
      {/* </Router> */}
    </>
  );
}
export default App;