import React from 'react'
import { useNavigate } from "react-router-dom";

function Header() {
    const navigate = useNavigate();

  return (
    <div>
        <nav class="navbar navbar-light bg-light">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">
                  <b>Mortgage App</b>
                </a>
                <div class=" d-flex gap-3">
                <button className="btn btn-outline-success" onClick={() => navigate("/")}>
                    Add Mortgage
                </button>
                <button className="btn btn-outline-success" onClick={() => navigate("/list")}>
                    View Mortgages
                </button>
                </div>
            </div>
        </nav>
    </div>
  )
}

export default Header