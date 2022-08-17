import React from "react";
import "./App.css";
import { BrowserRouter } from "react-router-dom";
import Routes from "./Routes";

const App = () => {
  return (
    <div>
      <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/icon?family=Material+Icons"
      />
      <BrowserRouter>
        <Routes />
      </BrowserRouter>
    </div>
  );
};

export default App;
