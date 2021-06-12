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
    <div className="h-full">
      <Suspense fallback={<div>Loading...</div>}>
        <BrowserRouter history={createBrowserHistory()}>
          <div className="flex lg:flex-row flex-col h-full">
            <div className="w-full lg:w-1/4">
              <Navigation />
            </div>
            <div className="w-full lg:w-3/4">
              <Route path="/" exact component={Cards}></Route>
              <Route path="/people" component={People}></Route>
              <Route path="/transactions" component={Transactions}></Route>
            </div>
          </div>
        </BrowserRouter>
      </Suspense>
    </div>
  );
};

export default App;
