import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import TopAppBar from '../components/TopAppBar';
import BottomNavBar from '../components/BottomNavBar';

export default function DailyAlertScreen({ language = "हिंदी", onLanguageToggle }) {
  const navigate = useNavigate();
  const [choice, setChoice] = useState(null); // 'yes' | 'no' | null

  const handleChoice = (selectedChoice) => {
    setChoice(selectedChoice);
  };

  const handleFinish = () => {
    navigate('/completion');
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
      <main className="flex-grow flex flex-col items-center justify-center px-margin-mobile md:px-margin-desktop py-section-gap max-w-[800px] mx-auto w-full pb-28">
        
        {/* Voice Interaction Area */}
        <div className="bg-surface-container-low rounded-3xl p-8 md:p-12 w-full flex flex-col items-center text-center shadow-[0_4px_16px_rgba(0,0,0,0.06)] mb-section-gap relative overflow-hidden border border-outline-variant/30">
          
          <div className="bg-primary-container text-on-primary-container rounded-full p-6 mb-stack-gap animate-pulse relative z-10 flex items-center justify-center w-24 h-24 shadow-[0_4px_20px_rgba(255,152,0,0.25)]">
            <span className="material-symbols-outlined text-4xl fill">
              record_voice_over
            </span>
          </div>

          <h2 className="font-headline-lg-mobile text-headline-lg-mobile md:font-headline-xl md:text-headline-xl text-primary mb-3 relative z-10 font-bold">
            क्या आप रोज़ टमाटर का भाव सुनना चाहते हैं?
          </h2>

          <p className="font-body-xl text-body-xl text-on-surface-variant mb-6 relative z-10">
            Do you want to receive tomato market price updates daily?
          </p>

          {/* Audio Waveform Visualization */}
          <div className="flex items-center gap-1.5 h-10 mb-2 opacity-80">
            <div className="w-2 h-4 bg-primary rounded-full animate-bounce"></div>
            <div className="w-2 h-8 bg-primary rounded-full animate-bounce" style={{ animationDelay: '0.1s' }}></div>
            <div className="w-2 h-10 bg-primary rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
            <div className="w-2 h-6 bg-primary rounded-full animate-bounce" style={{ animationDelay: '0.3s' }}></div>
            <div className="w-2 h-9 bg-primary rounded-full animate-bounce" style={{ animationDelay: '0.4s' }}></div>
            <div className="w-2 h-5 bg-primary rounded-full animate-bounce" style={{ animationDelay: '0.5s' }}></div>
            <div className="w-2 h-8 bg-primary rounded-full animate-bounce" style={{ animationDelay: '0.6s' }}></div>
          </div>
        </div>

        {/* Action Choices */}
        {!choice ? (
          <div className="w-full grid grid-cols-1 md:grid-cols-2 gap-stack-gap mb-section-gap">
            <button
              type="button"
              onClick={() => handleChoice('yes')}
              className="bg-primary text-on-primary rounded-2xl h-touch-target-min flex items-center justify-center gap-3 px-6 hover:bg-primary-container active:scale-95 transition-all shadow-md font-semibold"
            >
              <span className="material-symbols-outlined">notifications_active</span>
              <span className="font-label-lg text-label-lg">हाँ, रोज़ बताएँ (Yes, Daily)</span>
            </button>

            <button
              type="button"
              onClick={() => handleChoice('no')}
              className="bg-surface-container-high text-on-surface rounded-2xl h-touch-target-min flex items-center justify-center gap-3 px-6 hover:bg-surface-variant active:scale-95 transition-all border border-outline-variant font-semibold"
            >
              <span className="material-symbols-outlined">notifications_off</span>
              <span className="font-label-lg text-label-lg">नहीं, अभी नहीं (Not now)</span>
            </button>
          </div>
        ) : (
          <div className="w-full flex flex-col gap-4 mb-section-gap animate-fadeIn">
            {choice === 'yes' ? (
              <div className="bg-secondary-container text-on-secondary-container rounded-2xl p-6 w-full flex items-start gap-4 border border-secondary shadow-sm">
                <span className="material-symbols-outlined text-secondary text-3xl fill mt-0.5">
                  check_circle
                </span>
                <div>
                  <p className="font-headline-lg-mobile text-xl font-bold mb-1">
                    डेमो अलर्ट तैयार है!
                  </p>
                  <p className="font-body-lg text-on-secondary-fixed-variant">
                    सुबह 8:00 बजे आपको व्हाट्सएप और ऑडियो संदेश द्वारा मंडी के भाव भेजे जाएंगे।
                  </p>
                  <p className="text-xs opacity-70 mt-2">
                    (Demo alert ready. Real SMS/WhatsApp triggers will run via FastAPI backend.)
                  </p>
                </div>
              </div>
            ) : (
              <div className="bg-surface-container text-on-surface rounded-2xl p-6 w-full flex items-start gap-4 border border-outline shadow-sm">
                <span className="material-symbols-outlined text-on-surface-variant text-3xl mt-0.5">
                  cancel
                </span>
                <div>
                  <p className="font-headline-lg-mobile text-xl font-bold mb-1">
                    अलर्ट रद्द किया गया
                  </p>
                  <p className="font-body-lg text-on-surface-variant">
                    आप कभी भी होम स्क्रीन से रोज़ाना भाव का अलर्ट शुरू कर सकते हैं।
                  </p>
                </div>
              </div>
            )}

            <button
              type="button"
              onClick={handleFinish}
              className="w-full h-touch-target-min bg-primary text-on-primary rounded-2xl font-label-lg shadow-md hover:bg-primary-container active:scale-95 transition-all flex items-center justify-center gap-2 font-semibold"
            >
              <span>अंतिम सारांश देखें (View Summary)</span>
              <span className="material-symbols-outlined">arrow_forward</span>
            </button>
          </div>
        )}
      </main>

      {/* Mobile Bottom Nav */}
      <BottomNavBar />
    </div>
  );
}
