import './style.css';

function Image() {
  return (
    <div className="video-container">
      <input type="file" id="img" name="img" accept="image/*" />
    </div>
  );
}

export default Image;
