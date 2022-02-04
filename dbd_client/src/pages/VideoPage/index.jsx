import React, { useState } from 'react';
import Webcam from 'react-webcam';
import CaptureIcon from '../../assets/icons/CaptureIcon';
import './style.css';

const videoConstraints = {
  width: 720,
  height: 480,
  facingMode: 'user',
};

function Video() {
  const [image, setImage] = useState('');
  const webcamRef = React.useRef(null);

  const capture = React.useCallback(() => {
    const imageSrc = webcamRef.current.getScreenshot();
    setImage(imageSrc);
  }, [webcamRef]);

  return (
    <div>
      <div className="webcamContainer">
        <div class="overlay">
          <div class="overlay-element top-left"></div>
          <div class="overlay-element top-right"></div>
          <div class="overlay-element bottom-left"></div>
          <div class="overlay-element bottom-right"></div>
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
      <div className="captureContainer">
        <button className="capture" onClick={capture}>
          <CaptureIcon />
        </button>
      </div>
      {image.length ? (
        <div className="imageContainer">
          <img src={image} alt="user" />
        </div>
      ) : null}
    </div>
  );
}

export default Video;
