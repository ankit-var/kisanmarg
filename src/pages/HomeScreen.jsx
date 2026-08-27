import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import TopAppBar from '../components/TopAppBar';
import BottomNavBar from '../components/BottomNavBar';

const suggestions = [
  { text: "आज मेरे टमाटर का क्या भाव है?", icon: "trending_up", target: "/listening?q=tomato_price" },
  { text: "व्यापारी ने ₹20 बताया, क्या करूँ?", icon: "gavel", target: "/trader-offer" },
  { text: "आज कहाँ बेचूँ?", icon: "storefront", target: "/district" },
  { text: "क्या भाव बढ़ेगा?", icon: "insights", target: "/listening?q=price_trend" },
];

export default function HomeScreen({ language = "हिंदी", onLanguageToggle }) {
  const navigate = useNavigate();
  const [showTypeInput, setShowTypeInput] = useState(false);
  const [typedQuery, setTypedQuery] = useState("");
  const [isAudioGreetingPlaying, setIsAudioGreetingPlaying] = useState(false);

  const handleMicClick = () => {
    navigate('/listening');
  };

  const handleTypeSubmit = (e) => {
    e.preventDefault();
    if (typedQuery.trim()) {
      navigate('/district');
    }
  };

  const toggleAudioGreeting = () => {
    setIsAudioGreetingPlaying(!isAudioGreetingPlaying);
  };

  return (
    <div className="bg-background text-on-background min-h-screen flex flex-col antialiased">
      {/* Top Header */}
      <TopAppBar language={language} onLanguageToggle={onLanguageToggle} />

      {/* Main Canvas */}
      <main className="flex-grow flex flex-col items-center justify-center px-gutter pt-8 pb-32 max-w-[800px] mx-auto w-full gap-section-gap">
        
        {/* Greeting Area */}
        <section className="text-center w-full max-w-lg bg-surface-container-lowest p-6 rounded-2xl shadow-[0_4px_16px_rgba(0,0,0,0.06)] border border-surface-container flex flex-col items-center gap-4">
          <div className="flex items-center gap-3">
            <h1 className="font-headline-lg-mobile text-headline-lg-mobile md:font-headline-lg md:text-headline-lg text-primary font-bold">
              बोलकर पूछें
            </h1>
            <button
              type="button"
              onClick={toggleAudioGreeting}
              aria-label="Play greeting audio"
              className={`w-12 h-12 rounded-full flex items-center justify-center transition-all shrink-0 ${
                isAudioGreetingPlaying
                  ? 'bg-secondary-container text-on-secondary-container scale-105'
                  : 'bg-surface-container text-primary hover:bg-surface-container-high'
              }`}
            >
              <span className="material-symbols-outlined text-3xl fill">
                {isAudioGreetingPlaying ? 'volume_up' : 'volume_down'}
              </span>
            </button>
          </div>
          <p className="font-body-lg text-body-lg text-on-surface-variant">
            टमाटर, प्याज, या किसी भी मंडी के भाव जानने के लिए माइक दबाएँ
          </p>
        </section>

        {/* Voice Interaction Hub */}
        <section className="flex flex-col items-center justify-center gap-6 py-6">
          <button
            type="button"
            onClick={handleMicClick}
            aria-label="Start Voice Recording"
            className="pulse-effect bg-primary text-on-primary w-28 h-28 md:w-36 md:h-36 rounded-full flex items-center justify-center shadow-[0_8px_28px_rgba(255,152,0,0.35)] hover:scale-105 active:scale-95 transition-all duration-300 group"
          >
            <span className="material-symbols-outlined text-[52px] md:text-[68px] fill group-hover:scale-110 transition-transform">
              mic
            </span>
          </button>
          <span className="font-label-lg text-label-lg text-on-surface-variant font-semibold">
            माइक दबाकर बोलें
          </span>
        </section>

        {/* Suggestion Chips Grid */}
        <section className="w-full grid grid-cols-1 md:grid-cols-2 gap-stack-gap">
          {suggestions.map((item, idx) => (
            <button
              key={idx}
              type="button"
              onClick={() => navigate(item.target)}
              className="bg-surface-container-lowest border border-outline-variant/60 rounded-2xl py-4 px-6 flex items-center gap-3.5 hover:bg-surface-container-low hover:border-primary/40 active:scale-[0.98] transition-all shadow-sm w-full text-left min-h-touch-target-min group"
            >
              <div className="w-10 h-10 rounded-full bg-surface-container flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-on-primary transition-colors shrink-0">
                <span className="material-symbols-outlined text-2xl">{item.icon}</span>
              </div>
              <span className="font-label-lg text-label-lg text-on-surface font-semibold flex-1">
                {item.text}
              </span>
              <span className="material-symbols-outlined text-outline-variant group-hover:text-primary transition-colors">
                chevron_right
              </span>
            </button>
          ))}
        </section>

        {/* Type Option & Info Footer */}
        <footer className="mt-auto pt-6 text-center w-full flex flex-col items-center gap-3">
          {showTypeInput ? (
            <form onSubmit={handleTypeSubmit} className="w-full max-w-md flex gap-2">
              <input
                type="text"
                value={typedQuery}
                onChange={(e) => setTypedQuery(e.target.value)}
                placeholder="यहाँ अपनी समस्या या फसल लिखें..."
                className="flex-1 bg-surface-container-lowest border border-outline-variant rounded-full px-5 py-3 font-body-lg text-on-surface focus:outline-none focus:border-primary"
                autoFocus
              />
              <button
                type="submit"
                className="bg-primary text-on-primary px-6 py-3 rounded-full font-label-lg shadow-sm hover:bg-primary-container"
              >
                खोजें
              </button>
            </form>
          ) : (
            <button
              type="button"
              onClick={() => setShowTypeInput(true)}
              className="inline-flex items-center gap-2 font-label-lg text-label-lg text-primary hover:underline hover:opacity-85 py-2 px-4 rounded-full transition-all"
            >
              <span>⌨️</span>
              <span>टाइप करें (Type instead)</span>
            </button>
          )}

          <div className="flex items-center gap-4 text-sm text-on-surface-variant/70">
            <span>Demo with mock mandi data</span>
            <span>•</span>
            <button 
              onClick={() => navigate('/presentation')}
              className="underline text-primary font-semibold hover:text-primary-container"
            >
              कैसे काम करता है? (How it works)
            </button>
          </div>
        </footer>
      </main>

      {/* Mobile Bottom Nav */}
      <BottomNavBar />
    </div>
  );
}
