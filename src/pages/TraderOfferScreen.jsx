import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import TopAppBar from '../components/TopAppBar';
import BottomNavBar from '../components/BottomNavBar';

export default function TraderOfferScreen({ language = "हिंदी", onLanguageToggle }) {
  const navigate = useNavigate();
  const [offerPrice, setOfferPrice] = useState(14);
  const [isListening, setIsListening] = useState(false);
  const [isPlayingAudio, setIsPlayingAudio] = useState(false);

  const handleMicToggle = () => {
    setIsListening(!isListening);
  };

  const handleHearBargainingAdvice = () => {
    navigate('/bargaining', { state: { offerPrice, targetPrice: 16 } });
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

      {/* Main Content */}
      <main className="flex-grow px-margin-mobile md:px-margin-desktop py-section-gap flex flex-col gap-5 max-w-[800px] mx-auto w-full mb-[90px]">
        {/* Heading */}
        <h2 className="font-headline-lg-mobile text-headline-lg-mobile md:font-headline-lg md:text-headline-lg text-on-surface text-center mb-2 font-bold">
          व्यापारी का भाव
        </h2>

        {/* Audio Prompt Card */}
        <div className="bg-surface-container-low rounded-2xl p-6 shadow-sm flex flex-col items-center text-center gap-4 border border-outline-variant/40">
          <p className="font-body-xl text-body-xl text-on-surface font-medium">
            व्यापारी कितने रुपये प्रति किलो दे रहा है?
          </p>
          <button
            type="button"
            onClick={() => setIsPlayingAudio(!isPlayingAudio)}
            className={`w-[64px] h-[64px] rounded-full flex items-center justify-center shadow-md transition-all ${
              isPlayingAudio ? 'bg-secondary text-on-secondary scale-105' : 'bg-primary-container text-on-primary-container hover:opacity-90'
            }`}
          >
            <span className="material-symbols-outlined text-3xl fill">
              {isPlayingAudio ? 'pause' : 'play_arrow'}
            </span>
          </button>
        </div>

        {/* Microphone Interaction Area */}
        <div className="flex flex-col items-center justify-center py-6 gap-5 relative">
          <div className="relative w-[120px] h-[120px] flex items-center justify-center">
            <button
              type="button"
              onClick={handleMicToggle}
              className={`w-[92px] h-[92px] rounded-full flex items-center justify-center shadow-md border-2 border-primary hover:bg-surface-variant transition-all z-10 ${
                isListening ? 'bg-[#FF9800] text-white pulse-effect' : 'bg-surface text-on-surface glow-pulse'
              }`}
            >
              <span className="material-symbols-outlined text-[44px] text-primary">mic</span>
            </button>
          </div>
          <div className="bg-surface-container rounded-2xl px-6 py-3 border border-outline-variant border-dashed flex items-center gap-3">
            <span className="font-body-lg text-body-lg text-on-surface-variant italic font-semibold">
              "₹{offerPrice} प्रति किलो"
            </span>
            <div className="flex items-center gap-1 border-l pl-3 border-outline-variant">
              <button 
                onClick={() => setOfferPrice(Math.max(10, offerPrice - 1))}
                className="w-7 h-7 rounded-full bg-surface-container-high flex items-center justify-center text-primary font-bold"
              >
                -
              </button>
              <button 
                onClick={() => setOfferPrice(offerPrice + 1)}
                className="w-7 h-7 rounded-full bg-surface-container-high flex items-center justify-center text-primary font-bold"
              >
                +
              </button>
            </div>
          </div>
        </div>

        {/* Voice Result / Warning Display */}
        <div className="bg-error-container text-on-error-container rounded-2xl p-6 shadow-sm flex flex-col gap-3 border border-error/30">
          <div className="flex items-center gap-3">
            <span className="material-symbols-outlined text-error text-3xl fill">warning</span>
            <h3 className="font-headline-lg-mobile text-headline-lg-mobile md:font-headline-xl md:text-headline-xl text-error font-bold">
              कम भाव
            </h3>
          </div>
          <p className="font-body-xl text-body-xl leading-relaxed">
            ₹{offerPrice} प्रति किलो कम है. व्यापारी से कम-से-कम <span className="font-bold underline">₹16</span> माँगिए.
          </p>
        </div>

        {/* Action Button */}
        <button
          type="button"
          onClick={handleHearBargainingAdvice}
          className="w-full h-touch-target-min bg-primary text-on-primary rounded-2xl font-label-lg text-label-lg shadow-md hover:bg-primary-container active:scale-95 transition-all flex items-center justify-center gap-2 mt-2 font-semibold"
        >
          <span className="material-symbols-outlined">tips_and_updates</span>
          बात करने के लिए सुझाव सुनें (Bargaining Assistant)
        </button>
      </main>

      {/* Mobile Bottom Nav */}
      <BottomNavBar />
    </div>
  );
}
