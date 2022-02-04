import { useRef, useState } from 'react';
import './style.css';

function Image() {
  const inputRef = useRef(null);
  const [responseData, setResponseData] = useState('');

  function handleClick() {
    if (inputRef && inputRef.current) {
      const formData = new FormData();
      const img = inputRef.current.files[0];
      formData.append('imagefile', img);
      const options = {
        method: 'POST',
        body: formData,
      };
      fetch('http://localhost:5000/imageProcess/v1.0/findPose', options)
        .then((response) => response.json())
        .then((response) => setResponseData(response.result));
    }
  }

  function handleClear() {
    setResponseData('');
    inputRef.current.value = '';
  }

  return (
    <>
      <div className="video-container">
        {inputRef && inputRef.current && inputRef.current.value && (
          <img
            className="image"
            src={URL.createObjectURL(inputRef.current.files[0])}
            alt="driver"
          />
        )}
        <input
          type="file"
          id="img"
          name="img"
          accept="image/*"
          ref={inputRef}
        />
        <div>
          <button onClick={handleClick}>submit</button>
          <button onClick={handleClear}>clear</button>
        </div>
        {responseData && (
          <div className="caption">
            <span>Current behavior:</span>
            &nbsp; &nbsp; &nbsp;
            <span>
              <strong>{responseData.result}</strong>
            </span>
          </div>
        )}
      </div>
    </>
  );
}

export default Image;
