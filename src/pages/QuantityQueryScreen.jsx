import React, { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import TopAppBar from '../components/TopAppBar';

const quickQuantities = ["50 Kg", "100 Kg", "500 Kg", "1000 Kg"];

export default function QuantityQueryScreen({ language = "हिंदी", onLanguageToggle }) {
  const navigate = useNavigate();
  const location = useLocation();
  const district = location.state?.district || "Nashik";

  const [quantity, setQuantity] = useState("500 Kg");
  const [isListening, setIsListening] = useState(false);
  const [isPlayingAudio, setIsPlayingAudio] = useState(false);

  const handleNext = () => {
    navigate('/advice', { state: { district, quantity } });
  };

  const handleSelectQuantity = (q) => {
    setQuantity(q);
  };

  const handleMicToggle = () => {
    setIsListening(!isListening);
    if (!isListening) {
      setTimeout(() => {
        setQuantity("500 Kg");
        setIsListening(false);
      }, 1800);
    }
  };

  return (
    <div className="bg-background text-on-background min-h-screen flex flex-col font-body-lg antialiased">
      {/* TopAppBar */}
      <TopAppBar
        title="Kisaan Marg"
        showBack={true}
        language={language}
        onLanguageToggle={onLanguageToggle}
      />

      {/* Main Content Canvas */}
      <main className="flex-grow flex flex-col items-center justify-center px-gutter pt-6 pb-[130px] max-w-[800px] mx-auto w-full relative">
        
        {/* Progress Indicator */}
        <div className="w-full max-w-md mb-6 flex justify-between items-center gap-2">
          <div className="h-2.5 flex-1 bg-secondary rounded-full"></div>
          <div className="h-2.5 flex-1 bg-secondary rounded-full"></div>
        </div>

        {/* Question Section */}
        <div className="w-full bg-surface-container-lowest rounded-2xl p-6 md:p-8 shadow-sm border border-surface-container mb-stack-gap text-center relative overflow-hidden">
          <div className="relative z-10 flex flex-col items-center">
            <button
              type="button"
              onClick={() => setIsPlayingAudio(!isPlayingAudio)}
              aria-label="Play question audio"
              className={`mb-4 w-16 h-16 rounded-full flex items-center justify-center mx-auto transition-colors shadow-sm ${
                isPlayingAudio ? 'bg-secondary-container text-on-secondary-container' : 'bg-surface-container text-primary hover:bg-surface-container-high'
              }`}
            >
              <span className="material-symbols-outlined text-4xl fill">volume_up</span>
            </button>
            <h2 className="font-headline-lg-mobile text-headline-lg-mobile md:font-headline-xl md:text-headline-xl text-on-surface mb-2 font-bold">
              आपके पास कितने किलो टमाटर हैं?
            </h2>
            <p className="font-body-xl text-body-xl text-on-surface-variant">
              How many kilos of tomatoes do you have?
            </p>
          </div>
        </div>

        {/* Input & Confirmation Section */}
        <div className="w-full max-w-md flex flex-col items-center gap-stack-gap mt-4">
          
          {/* Visual Confirmation Display */}
          <div className="w-full bg-surface-container-lowest border-2 border-primary/40 rounded-2xl p-5 flex items-center justify-between shadow-sm min-h-[76px]">
            <span className="font-body-xl text-body-xl text-on-surface font-bold">
              {quantity ? (
                <span className="flex items-center gap-2 text-primary text-2xl font-headline-lg-mobile">
                  <span className="material-symbols-outlined fill text-secondary">check_circle</span>
                  {quantity}
                </span>
              ) : (
                <span className="text-outline italic">यहाँ मात्रा दिखाई देगी...</span>
              )}
            </span>
            {quantity && (
              <button
                type="button"
                onClick={() => setQuantity("")}
                className="text-on-surface-variant hover:text-error text-sm font-semibold p-1"
              >
                बदलें
              </button>
            )}
          </div>

          {/* Contextual Chips */}
          <div className="flex flex-wrap justify-center gap-3 w-full mt-2">
            <button
              type="button"
              onClick={handleMicToggle}
              className="bg-primary-container text-on-primary-container border border-primary rounded-full px-6 py-3.5 flex items-center gap-2 shadow-sm hover:bg-primary hover:text-on-primary active:scale-95 transition-all w-full justify-center mb-1 font-semibold"
            >
              <span className="material-symbols-outlined fill">mic</span>
              <span className="font-label-lg">मात्रा बोलकर बताएं</span>
            </button>

            {quickQuantities.map((q) => (
              <button
                key={q}
                type="button"
                onClick={() => handleSelectQuantity(q)}
                className={`border rounded-full px-6 py-3 flex items-center gap-2 shadow-sm active:scale-95 transition-all font-semibold ${
                  quantity === q
                    ? 'bg-secondary text-on-secondary border-secondary shadow-md'
                    : 'bg-surface-container-lowest border-outline-variant text-on-surface hover:bg-surface-container-high'
                }`}
              >
                <span className="font-body-xl text-body-xl">{q}</span>
              </button>
            ))}
          </div>

          {/* Primary Microphone Action */}
          <div className="mt-8 mb-6 relative flex flex-col items-center justify-center w-full">
            <button
              type="button"
              onClick={handleMicToggle}
              aria-label="Tap to speak quantity"
              className={`w-24 h-24 rounded-full shadow-[0_6px_24px_rgba(255,152,0,0.3)] flex items-center justify-center transition-all hover:scale-105 active:scale-95 z-20 ${
                isListening ? 'bg-[#FF9800] text-white pulse-effect' : 'bg-primary text-on-primary'
              }`}
            >
              <span className="material-symbols-outlined text-5xl fill">mic</span>
            </button>
            <div className="mt-3 text-on-surface-variant font-label-lg text-label-lg font-medium">
              {isListening ? 'सुन रहा हूँ...' : 'Tap to speak'}
            </div>
          </div>
        </div>
      </main>

      {/* Bottom Action Footer */}
      <footer className="fixed bottom-0 w-full bg-surface border-t border-surface-container p-4 pb-safe flex justify-between items-center z-40 shadow-[0_-4px_16px_rgba(0,0,0,0.06)]">
        <button
          type="button"
          onClick={() => navigate(-1)}
          aria-label="Go back"
          className="flex items-center gap-2 text-primary px-4 py-2.5 rounded-xl hover:bg-surface-container-low transition-colors font-label-lg text-label-lg font-semibold"
        >
          <span className="material-symbols-outlined">arrow_back</span>
          Back
        </button>

        <div className="font-label-lg text-label-lg text-on-surface-variant bg-surface-container px-4 py-2 rounded-full font-semibold">
          Step 2 of 2
        </div>

        <button
          type="button"
          onClick={handleNext}
          disabled={!quantity}
          aria-label="Confirm quantity and view advice"
          className="bg-primary text-on-primary px-6 py-3 rounded-xl font-label-lg text-label-lg shadow-md hover:bg-primary-container active:scale-95 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2 font-semibold"
        >
          Next (सलाह देखें)
          <span className="material-symbols-outlined">arrow_forward</span>
        </button>
      </footer>
    </div>
  );
}
