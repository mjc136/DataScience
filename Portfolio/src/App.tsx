import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from './layout';
import Home from './Pages/home.tsx'

function App() {
    return (
        <BrowserRouter>
            <Layout>
                <Routes>
                    <Route path="/" element={<Home/>} />
                </Routes>
            </Layout>
        </BrowserRouter>
    );
}

export default App;
