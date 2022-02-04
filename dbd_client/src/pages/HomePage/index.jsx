import { Link } from 'react-router-dom';

import './styles.css';

function Home() {
  return (
    <div className="container">
      <p className="title">
        <strong>D</strong>river's <strong>B</strong>ehavior <strong>D</strong>
        etection
      </p>
      <p>You can upload image or open webcam then see the result</p>
      <div className="uploads">
        <div className="image">
          <Link to="image">
            <button>upload image</button>
          </Link>
        </div>
        <div className="divider" />
        <div className="video">
          <Link to="video">
            <button>stream video</button>
          </Link>
        </div>
      </div>
    </div>
  );
}

export default Home;
