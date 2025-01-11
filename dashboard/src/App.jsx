import { useState } from 'react'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
function Home() {
  return <h1>Home Page</h1>;
}

function About() {
  return <h1>About Page</h1>;
}


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
  <BrowserRouter>
      <nav>
        <Link to="/">Home</Link> | <Link to="/about">About</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </BrowserRouter>
    </>
  )
}

export default App
