import { useEffect, useState, Suspense, lazy } from "react";
import { BrowserRouter, Route } from "react-router-dom";
import { createBrowserHistory } from "history";
import Navigation from "./Navigation";
import Cards from "./Cards";

import "./App.css";

const People = lazy(() => import("./People"));
const Transactions = lazy(() => import("./Transactions"));

const App = () => {
  return (
    <div className="App">
      <Suspense fallback={<div>Loading...</div>}>
        <BrowserRouter history={createBrowserHistory()}>
          <Navigation />
          <Route path="/" exact component={Cards}></Route>
          <Route path="/people" component={People}></Route>
          <Route path="/transactions" component={Transactions}></Route>
        </BrowserRouter>
      </Suspense>
    </div>
  );
};

export default App;
