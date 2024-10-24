import '../Styles/footer.scss';

const Footer: React.FC = () => {
    return (
        <div className="container.fluid mt-5 p-0" >
            <footer className="py-5">
                <div className="row">
                    <div className="col-6 col-md-2 mb-3">
                        <h4>Sections</h4>
                        <ul className="nav flex-column">
                            <li className="nav-item mb-2"><a href="#" className="nav-link p-0 link-light">Home</a></li>
                            <li className="nav-item mb-2"><a href="#" className="nav-link p-0 link-light">Features</a></li>
                            <li className="nav-item mb-2"><a href="#" className="nav-link p-0 link-light">Pricing</a></li>
                            <li className="nav-item mb-2"><a href="#" className="nav-link p-0 link-light">FAQs</a></li>
                            <li className="nav-item mb-2"><a href="#" className="nav-link p-0 link-light">About</a></li>
                        </ul>
                    </div>

                    <div className="col-md-5 offset-md-1 mb-3">
                        <form>
                            <h5>Subscribe to our newsletter</h5>
                            <p>Monthly digest of what's new and exciting from us.</p>
                            <div className="d-flex flex-column flex-sm-row w-100 gap-2">
                                <label htmlFor="newsletter1" className="visually-hidden">Email address</label>
                                <input id="newsletter1" type="text" className="form-control" placeholder="Email address" />
                                <button className="btn btn-success" type="button">Subscribe</button>
                            </div>
                        </form>
                    </div>
                </div>

                <div className="d-flex flex-column flex-sm-row justify-content-between py-4 my-4 border-top">
                    <p>&copy; 2024 Company, Inc. All rights reserved.</p>
                    <ul className="list-unstyled d-flex">
                        <li className="ms-3"><a className="link-body-emphasis link-light" href="#"><svg className="bi" width="24" height="24"><use xlinkHref="#twitter" /></svg></a></li>
                        <li className="ms-3"><a className="link-body-emphasis" href="#"><svg className="bi" width="24" height="24"><use xlinkHref="#instagram" /></svg></a></li>
                        <li className="ms-3"><a className="link-body-emphasis" href="#"><svg className="bi" width="24" height="24"><use xlinkHref="#facebook" /></svg></a></li>
                    </ul>
                </div>
            </footer>
        </div>
    );
}

export default Footer;