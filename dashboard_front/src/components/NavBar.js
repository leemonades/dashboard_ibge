import React from 'react';
import logo from '../assets/images/logo.png';
import './NavBar.css';

const Navbar = () => {
    return (
        <nav className="navbar">
            <div className="navbar-logo">
                <img src={logo} alt="Logo" />
            </div>
            <ul className="navbar-menu">
                <li><a href="/">Dashboard</a></li>
                <li><a href="/sobre">Sobre</a></li>
            </ul>
        </nav>
    );
}

export default Navbar;