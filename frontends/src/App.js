
import './App.css';
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import MortgageForm from "./components/MortgageForm.jsx";
import MortgageList from './components/MortgageList.jsx';
import Header from './components/Header.jsx';


function App() {
  return (

    <Router>
      <div className="min-h-screen bg-gray-100 p-6">
        <Header />
        <Routes>
          <Route path="/" element={<MortgageForm />} />
          <Route path="/list" element={<MortgageList />} />
        </Routes>
      </div>
    </Router>
    
  );
}

export default App;
