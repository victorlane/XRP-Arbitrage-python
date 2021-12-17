import './App.css';
import Header from "./components/header/Header";
import DataGroup from "./components/DataGroup/DataGroup";
import axios from "axios";
import React, { useEffect, useState } from "react";

const MINUTE_MS = 100000;

function App() {
  const [isLoading, setLoading] = useState(true); 
  const [prices, setData] = useState();

  useEffect(() => {
    const interval = setInterval(() => {
      axios.get("http://192.168.2.6:5000/api/v2/arbitrage").then(response => {
        setData(response.data);
        setLoading(false);
      })
    }, MINUTE_MS);
    return () => clearInterval(interval);
  });

  if (isLoading) {
    return <div className="app-loading">LOADING DATA</div>;
  }

  return (
    <div>
      <Header/>
      <DataGroup data={prices}/>
    </div>
  );
}

export default App;
