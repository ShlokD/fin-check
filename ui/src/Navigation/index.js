import React from "react";
import { Link } from "react-router-dom";
import creditcard from "../images/credit-card.png";
import group from "../images/group.png";
import transaction from "../images/transaction.png";
import money from "../images/money.png";

const Navigation = () => {
  return (
    <div className="border-r-2 border-gray-200 w-full h-full p-6">
      <div className="flex items-center lg:justify-start justify-center border-b-2 border-gray-200 p-6">
        <img alt="Fin Check Logo" height={100} width={100} src={money}></img>
        <h1 className="text-3xl font-bold p-4">Fin Check</h1>
      </div>

      <nav className="text-2xl font-bold w-full h-full my-6">
        <ul className="w-full h-full flex flex-col md:flex-row lg:flex-col items-center md:items-start md:justify-center lg:justify-start">
          <li className="p-4">
            <Link className="flex items-center w-full" to="/">
              <img
                alt="Credit Cards"
                src={creditcard}
                height={50}
                width={50}
              ></img>
              <p className="p-4">Cards</p>
            </Link>
          </li>
          <li className="p-4">
            <Link className="flex items-center w-full" to="/people">
              <img alt="People" src={group} height={50} width={50}></img>
              <p className="p-4">People</p>
            </Link>
          </li>
          <li className="p-4">
            <Link className="flex items-center w-full" to="/transactions">
              <img
                alt="Transactions"
                src={transaction}
                height={50}
                width={50}
              ></img>
              <p className="p-4">Transactions</p>
            </Link>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Navigation;
