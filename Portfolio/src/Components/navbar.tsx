import React from 'react';
import { NavLink }from 'react-router-dom';
/*import { useLocation } from 'react-router-dom';*/
import '../styles/Navbar.scss';

const Navbar: React.FC = () => {
    //const location = useLocation();

    //// Function to map pathnames to user-friendly titles
    //const getPageTitle = (pathname: string) => {
    //    switch (pathname) {
    //        case '/':
    //            return 'Home';
    //        case '/contact':
    //            return 'Contact Us';
    //        case '/item':
    //            return 'Item 1';
    //        case '/item2':
    //            return 'Item 2';
    //        case '/item3':
    //            return 'Item 3';
    //        default:
    //            return 'Welcome';
    //    }
    //};

    return (
        <div>
            <nav className="navbar navbar-dark bg-dark fixed-top">
                <div className="container-fluid">
                    <NavLink className="navbar-brand" to="/">Michael Cullen</NavLink>
                    <button className="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasDarkNavbar" aria-controls="offcanvasDarkNavbar" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="offcanvas offcanvas-end text-bg-dark" tabIndex={-1} id="offcanvasDarkNavbar" aria-labelledby="offcanvasDarkNavbarLabel">
                        <div className="offcanvas-header">
                            <h5 className="offcanvas-title" id="offcanvasDarkNavbarLabel">Dark offcanvas</h5>
                            <button type="button" className="btn-close btn-close-white" data-bs-dismiss="offcanvas" aria-label="Close"></button>
                        </div>
                        <div className="offcanvas-body">
                            <ul className="navbar-nav justify-content-end flex-grow-1 pe-3">
                                <li className="nav-item">
                                    <NavLink
                                        className={({ isActive }) => `nav-link ${isActive ? 'active' : ''} text-white`}
                                        to="/"
                                        end
                                    >
                                        Home
                                    </NavLink>
                                </li>
                                <li className="nav-item">
                                    <NavLink
                                        className={({ isActive }) => `nav-link ${isActive ? 'active' : ''} text-white`}
                                        to="/contact"
                                    >
                                        Contact
                                    </NavLink>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </nav>
        </div>
    );
}

export default Navbar;
