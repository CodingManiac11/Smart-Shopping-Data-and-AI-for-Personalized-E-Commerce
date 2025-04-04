import React, { useState } from "react";
import axios from "axios";

const Home = () => {
  const [products, setProducts] = useState([]);
  const [input, setInput] = useState("");

  const getRecommendations = async () => {
    const response = await axios.post("http://127.0.0.1:5000/recommend", {
      preferences: [input],
    });
    setProducts(response.data);
  };

  return (
    <div>
      <h1>AI Smart Shopping</h1>
      <input type="text" placeholder="Enter your preference" onChange={(e) => setInput(e.target.value)} />
      <button onClick={getRecommendations}>Get Recommendations</button>
      <ul>
        {products.map((p, index) => (
          <li key={index}>{p.name} - {p.category}</li>
        ))}
      </ul>
    </div>
  );
};

export default Home;
