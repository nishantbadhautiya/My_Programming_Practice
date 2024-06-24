import React, { useState } from 'react'

export default function TextForms(props) {
    const [text, setText] = useState("");
    // text = "ssdld";
    // setText("sddsddl");

    const handleUpClick = () => {
        // console.log("uppercase was clicked" + text);
        // setText("You have clocked on handleupclick");
        let newtext = text.toUpperCase();
        setText(newtext);
        props.showAlert("converted to uppercase ", "success");
    }
    const handleOnChange = (event) => {
        // console.log("text got changed");
        setText(event.target.value);
    }
    const handleLowClick = () => {
        setText(text.toLowerCase());
        props.showAlert("converted to lowercase ", "success");
    }
    const handleClearClick = () => {
        setText("");
        props.showAlert("Text cleared", "success");
    }
    const handleCopy = () => {
        console.log("I am copy");
        let text = document.getElementById("mybox");
        text.select();
        text.setSelectionRange(0, 9999);
        navigator.clipboard.writeText(text.value);
        props.showAlert("Text copied", "success");
    }
    const handleExtraSpaces = () => {
        let newText = text.split(/[ ]+/);
        setText(newText.join(" "));
        props.showAlert("Extran space removed ", "success");
    }
    return (
        <>
            <div className="container my-3">
                <h1>{props.heading}</h1>
                <div className="mb-3">
                    <textarea className="form-control" id="mybox" rows="4" value={text} onChange={handleOnChange} placeholder="Enter text here" style={{ backgroundColor: props.mode === 'dark' ? 'grey' : 'white', color: props.mode === 'dark' ? 'white' : 'black', }}></textarea>
                </div>
                <button type="button" className="btn btn-primary" onClick={handleUpClick}>Convert to UpperCase</button>
                <button type="button" className="btn btn-primary mx-2" onClick={handleLowClick}>Convert to LowerCase</button>
                <button type="button" className="btn btn-primary mx-2" onClick={handleClearClick}>Clear Text</button>
                <button type="button" className="btn btn-primary mx-2" onClick={handleCopy}>Copy Text</button>
                <button type="button" className="btn btn-primary mx-2" onClick={handleExtraSpaces} >Remove Extra Spaces</button>
            </div>
            <div className="container my-3">
                <h2>Your Text summery</h2>
                <p>{text.split(" ").length} words, {text.length} characters</p>
                <p>Total time to read these words = {text.split(" ").length * 0.008} minutes</p>

                <h2>Preview</h2>
                <p>{text.length > 0 ? text : "Enter something to preview it here"}</p>
            </div>
        </>
    )
}