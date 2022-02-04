import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/HomePage';
import Image from './pages/ImagePage';
import Video from './pages/VideoPage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="image" element={<Image />} />
        <Route path="video" element={<Video />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
