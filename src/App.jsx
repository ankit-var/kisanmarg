import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';

// Pages
import HomeScreen from './pages/HomeScreen';
import ListeningScreen from './pages/ListeningScreen';
import DistrictQueryScreen from './pages/DistrictQueryScreen';
import QuantityQueryScreen from './pages/QuantityQueryScreen';
import AdviceResultScreen from './pages/AdviceResultScreen';
import TraderOfferScreen from './pages/TraderOfferScreen';
import BargainingAssistantScreen from './pages/BargainingAssistantScreen';
import DailyAlertScreen from './pages/DailyAlertScreen';
import CompletionSummaryScreen from './pages/CompletionSummaryScreen';
import AIPresentationScreen from './pages/AIPresentationScreen';

// Components
import DemoNavigator from './components/DemoNavigator';

export default function App() {
  const [language, setLanguage] = useState("हिंदी");

  const toggleLanguage = () => {
    setLanguage((prev) => (prev === "हिंदी" ? "English" : "हिंदी"));
  };

  return (
    <Router>
      <div className="min-h-screen bg-background text-on-background">
        {/* Floating Quick Demo Navigator for SIH Evaluation */}
        <DemoNavigator />

        {/* Route Definitions */}
        <Routes>
          <Route 
            path="/" 
            element={<HomeScreen language={language} onLanguageToggle={toggleLanguage} />} 
          />
          <Route 
            path="/listening" 
            element={<ListeningScreen language={language} onLanguageToggle={toggleLanguage} />} 
          />
          <Route 
            path="/district" 
            element={<DistrictQueryScreen language={language} onLanguageToggle={toggleLanguage} />} 
          />
          <Route 
            path="/quantity" 
            element={<QuantityQueryScreen language={language} onLanguageToggle={toggleLanguage} />} 
          />
          <Route 
            path="/advice" 
            element={<AdviceResultScreen language={language} onLanguageToggle={toggleLanguage} />} 
          />
          <Route 
            path="/trader-offer" 
            element={<TraderOfferScreen language={language} onLanguageToggle={toggleLanguage} />} 
          />
          <Route 
            path="/bargaining" 
            element={<BargainingAssistantScreen language={language} onLanguageToggle={toggleLanguage} />} 
          />
          <Route 
            path="/daily-alert" 
            element={<DailyAlertScreen language={language} onLanguageToggle={toggleLanguage} />} 
          />
          <Route 
            path="/completion" 
            element={<CompletionSummaryScreen language={language} onLanguageToggle={toggleLanguage} />} 
          />
          <Route 
            path="/presentation" 
            element={<AIPresentationScreen language={language} onLanguageToggle={toggleLanguage} />} 
          />
          <Route 
            path="/how-it-works" 
            element={<AIPresentationScreen language={language} onLanguageToggle={toggleLanguage} />} 
          />
          {/* Catch-all redirect */}
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </div>
    </Router>
  );
}
