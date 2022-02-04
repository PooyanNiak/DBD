import React, { useEffect, useState } from 'react';
import Webcam from 'react-webcam';
import './style.css';

const videoConstraints = {
  width: 720,
  height: 480,
  facingMode: 'user',
};

function urltoFile(url, filename, mimeType) {
  return fetch(url)
    .then(function (res) {
      return res.arrayBuffer();
    })
    .then(function (buf) {
      return new File([buf], filename, { type: mimeType });
    });
}

function Video() {
  const [responseData, setResponseData] = useState('');
  const webcamRef = React.useRef(null);

  const capture = React.useCallback(() => {
    const formData = new FormData();
    const imageSrc = webcamRef.current.getScreenshot();
    urltoFile(imageSrc, 'image.jpg', 'image/jpeg').then((file) => {
      formData.append('imagefile', file);
      const options = {
        method: 'POST',
        body: formData,
      };
      fetch('http://localhost:5000/imageProcess/v1.0/findPose', options)
        .then((response) => response.json())
        .then((response) => setResponseData(response.result));
    });
  }, [webcamRef]);

  useEffect(() => {
    const intervalId = setInterval(capture, 3000);
    return () => clearInterval(intervalId);
  }, []);

  return (
    <div>
      <div className="webcamContainer">
        <div className="overlay">
          <div className="overlay-element top-left"></div>
          <div className="overlay-element top-right"></div>
          <div className="overlay-element bottom-left"></div>
          <div className="overlay-element bottom-right"></div>
          <Webcam
            className="webcam"
            audio={false}
            height={480}
            ref={webcamRef}
            screenshotFormat="image/jpeg"
            width={720}
            videoConstraints={videoConstraints}
          />
        </div>
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
  );
}

export default Video;
