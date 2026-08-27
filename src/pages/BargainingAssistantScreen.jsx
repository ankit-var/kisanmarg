import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import TopAppBar from '../components/TopAppBar';
import BottomNavBar from '../components/BottomNavBar';
import WaveformPlayer from '../components/WaveformPlayer';

export default function BargainingAssistantScreen({ language = "हिंदी", onLanguageToggle }) {
  const navigate = useNavigate();
  const location = useLocation();
  const targetPrice = location.state?.targetPrice || 16;

  return (
    <div className="bg-background text-on-background min-h-screen flex flex-col font-body-lg overflow-x-hidden antialiased">
      {/* TopAppBar */}
      <TopAppBar
        title="Kisaan Marg"
        showBack={true}
        language={language}
        onLanguageToggle={onLanguageToggle}
      />

      {/* Main Canvas */}
      <main className="flex-grow flex flex-col px-margin-mobile md:px-margin-desktop pt-6 pb-28 w-full max-w-lg mx-auto">
        
        {/* Screen Title & Handshake Icon */}
        <div className="flex flex-col items-center justify-center mb-6 text-center">
          <div className="w-24 h-24 bg-surface-container-high rounded-full flex items-center justify-center mb-3 shadow-sm border border-outline-variant">
            <span className="material-symbols-outlined text-5xl text-tertiary-container fill">
              handshake
            </span>
          </div>
          <h2 className="font-headline-xl text-headline-xl text-on-surface mb-1 font-bold">
            मोलभाव में मदद
          </h2>
          <p className="font-body-lg text-body-lg text-on-surface-variant">
            बाजार की जानकारी और बातचीत की सलाह
          </p>
        </div>

        {/* Audio Response Bento Card */}
        <section className="bg-surface-container-lowest rounded-3xl p-6 shadow-[0_4px_16px_rgba(0,0,0,0.06)] mb-6 relative overflow-hidden border border-surface-variant">
          {/* Decorative Accent Strip */}
          <div className="absolute top-0 left-0 w-2.5 h-full bg-secondary"></div>
          
          <div className="flex flex-col h-full pl-2">
            <div className="flex items-center mb-3 text-secondary">
              <span className="material-symbols-outlined mr-2 fill text-2xl">record_voice_over</span>
              <span className="font-label-lg text-label-lg uppercase tracking-wider font-bold">व्यापारी से कहें</span>
            </div>

            <p className="font-body-xl text-body-xl text-on-surface mb-6 leading-relaxed font-medium">
              "पास की मंडी में भाव अधिक है। मुझे कम-से-कम ₹{targetPrice} से ₹{targetPrice + 2} प्रति किलो मिलना चाहिए।"
            </p>

            {/* Audio Playback Component */}
            <WaveformPlayer initialPlaying={true} duration={12} barColor="bg-tertiary-container" />
          </div>
        </section>

        {/* Actions Container */}
        <div className="mt-auto flex flex-col items-center gap-4">
          {/* Extra Large Ask Again Button */}
          <button
            type="button"
            onClick={() => navigate('/listening')}
            aria-label="Replay or Ask again"
            className="w-24 h-24 bg-surface-container-lowest text-primary rounded-full flex flex-col items-center justify-center shadow-[0_8px_20px_rgba(255,152,0,0.25)] border-2 border-outline-variant pulse-effect hover:bg-surface-container transition-all active:scale-95"
          >
            <span className="material-symbols-outlined text-4xl mb-0.5 text-[#FF9800] fill">
              mic
            </span>
            <span className="font-label-lg text-[13px] leading-tight text-on-surface-variant font-bold">
              पूछें
            </span>
          </button>

          {/* Check New Price Button */}
          <button
            type="button"
            onClick={() => navigate('/district')}
            className="w-full h-touch-target-min bg-surface-container-high text-on-surface border border-outline rounded-2xl flex items-center justify-center gap-2 hover:bg-surface-variant transition-all shadow-sm active:scale-[0.98] font-semibold"
          >
            <span className="material-symbols-outlined">search</span>
            <span className="font-label-lg text-label-lg">नई कीमत जाँचें</span>
          </button>

          {/* Daily Alert Shortcut */}
          <button
            type="button"
            onClick={() => navigate('/daily-alert')}
            className="w-full h-touch-target-min bg-primary text-on-primary rounded-2xl flex items-center justify-center gap-2 hover:bg-primary-container transition-all shadow-md active:scale-[0.98] font-semibold"
          >
            <span className="material-symbols-outlined">notifications_active</span>
            <span className="font-label-lg text-label-lg">रोज़ का अलर्ट लगाएँ</span>
          </button>
        </div>
      </main>

      {/* Mobile Bottom Nav */}
      <BottomNavBar />
    </div>
  );
}
