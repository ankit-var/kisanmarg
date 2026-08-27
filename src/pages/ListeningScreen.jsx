import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function ListeningScreen({ language = "हिंदी", onLanguageToggle }) {
  const navigate = useNavigate();
  const [transcript, setTranscript] = useState("टमाटर कहाँ बेचूँ?");
  const [autoAdvanceTimer, setAutoAdvanceTimer] = useState(null);

  // Simulate speech recognition completing after 3.5s automatically, or user can click Stop
  useEffect(() => {
    const timer = setTimeout(() => {
      // Auto transition to district query
      navigate('/district');
    }, 4500);
    setAutoAdvanceTimer(timer);

    return () => clearTimeout(timer);
  }, [navigate]);

  const handleCancel = () => {
    if (autoAdvanceTimer) clearTimeout(autoAdvanceTimer);
    navigate('/');
  };

  const handleStop = () => {
    if (autoAdvanceTimer) clearTimeout(autoAdvanceTimer);
    navigate('/district');
  };

  const handleManualInput = () => {
    if (autoAdvanceTimer) clearTimeout(autoAdvanceTimer);
    navigate('/district');
  };

  return (
    <div className="min-h-screen text-on-surface font-body-lg flex flex-col items-center justify-between bg-gradient-to-b from-surface-bright to-surface-container overflow-x-hidden">
      {/* Top Header */}
      <header className="w-full flex justify-center items-center py-6 px-gutter md:px-margin-desktop bg-transparent z-10">
        <div className="w-full max-w-2xl flex justify-between items-center">
          <button
            onClick={handleCancel}
            className="flex items-center gap-2 text-primary font-label-lg px-4 py-2 rounded-full hover:bg-surface-container-low transition-colors"
          >
            <span className="material-symbols-outlined">arrow_back</span>
            <span>वापस</span>
          </button>
          
          <button
            type="button"
            onClick={onLanguageToggle}
            className="flex items-center space-x-2 px-4 py-2 rounded-full border border-outline-variant bg-surface-container-lowest text-on-surface-variant font-label-lg text-label-lg hover:bg-surface-container-low transition-all duration-200"
          >
            <span>{language}</span>
            <span className="material-symbols-outlined text-[20px]">arrow_drop_down</span>
          </button>
        </div>
      </header>

      {/* Main Canvas: Listening State */}
      <main className="flex-1 w-full max-w-2xl flex flex-col items-center justify-center px-gutter md:px-margin-desktop z-10 relative">
        {/* Status Text */}
        <h1 className="text-primary font-headline-xl text-headline-xl text-center mb-14 tracking-tight drop-shadow-sm font-bold animate-pulse">
          सुन रहा हूँ...
        </h1>

        {/* Animated Waveform Container */}
        <div className="relative w-full h-48 flex items-center justify-center mb-14">
          {/* Background Pulse effect */}
          <div className="pulse-ring"></div>
          
          {/* Waveform Bars */}
          <div className="flex items-center space-x-2.5 md:space-x-3.5 z-10 h-full">
            <div className="wave-bar"></div>
            <div className="wave-bar"></div>
            <div className="wave-bar !bg-primary !shadow-primary-fixed" style={{ animation: 'wave 1.2s infinite ease-in-out', animationDelay: '-0.6s' }}></div>
            <div className="wave-bar !bg-primary !shadow-primary-fixed" style={{ animation: 'wave 1.2s infinite ease-in-out', animationDelay: '-0.4s' }}></div>
            <div className="wave-bar"></div>
            <div className="wave-bar"></div>
          </div>
        </div>

        {/* Live Transcript Feedback */}
        <div className="bg-surface-container-highest/60 backdrop-blur-md rounded-2xl p-6 w-full text-center border border-outline-variant/40 shadow-sm transition-all duration-300 min-h-[100px] flex items-center justify-center">
          <p className="font-headline-lg-mobile text-headline-lg-mobile text-on-surface opacity-90 font-medium">
            "{transcript}"
          </p>
        </div>
      </main>

      {/* Bottom Actions: Fallback & Controls */}
      <div className="w-full max-w-md px-gutter mb-3 text-center">
        <button
          type="button"
          onClick={handleManualInput}
          className="w-full py-3 px-4 rounded-full border border-outline-variant/40 bg-surface-container-low/70 text-on-surface-variant font-label-lg text-label-lg hover:bg-surface-container-low transition-all duration-200 flex items-center justify-center space-x-2 shadow-sm"
        >
          <span>आवाज़ समझ नहीं आई?</span>
          <span className="flex items-center text-primary font-bold">
            <span className="material-symbols-outlined mr-1 text-[20px]">keyboard</span>
            <span>नंबर या जिला लिखें</span>
          </span>
        </button>
      </div>

      <footer className="w-full max-w-md px-gutter pb-8 pt-2 flex space-x-4 z-10">
        {/* Cancel Action */}
        <button
          type="button"
          onClick={handleCancel}
          className="flex-1 h-touch-target-min flex items-center justify-center rounded-full border-2 border-outline-variant text-on-surface-variant bg-surface-container-lowest font-label-lg text-label-lg hover:bg-surface-container-low active:scale-95 transition-all duration-200"
        >
          <span className="material-symbols-outlined mr-2">close</span>
          रद्द करें
        </button>

        {/* Stop Action (Proceed immediately) */}
        <button
          type="button"
          onClick={handleStop}
          className="flex-1 h-touch-target-min flex items-center justify-center rounded-full bg-primary text-on-primary shadow-md font-label-lg text-label-lg hover:bg-primary-container active:scale-95 transition-all duration-200 font-semibold"
        >
          <span className="material-symbols-outlined mr-2 fill">stop_circle</span>
          आगे बढ़ें
        </button>
      </footer>
    </div>
  );
}
