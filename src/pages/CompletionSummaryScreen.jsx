import React from 'react';
import { useNavigate } from 'react-router-dom';
import TopAppBar from '../components/TopAppBar';
import BottomNavBar from '../components/BottomNavBar';

export default function CompletionSummaryScreen({ language = "हिंदी", onLanguageToggle }) {
  const navigate = useNavigate();

  return (
    <div className="bg-surface text-on-surface min-h-screen flex flex-col font-body-lg antialiased">
      {/* TopAppBar */}
      <TopAppBar
        title="Kisaan Marg"
        showBack={false}
        language={language}
        onLanguageToggle={onLanguageToggle}
      />

      {/* Main Content Area */}
      <main className="flex-1 flex flex-col w-full max-w-[800px] mx-auto px-margin-mobile md:px-margin-desktop py-6 md:py-10 relative overflow-hidden pb-28">
        
        {/* Decorative Background Element */}
        <div className="absolute top-0 left-0 w-full h-56 bg-gradient-to-b from-secondary-container/30 to-transparent -z-10 rounded-b-[4rem]"></div>

        {/* Success Header */}
        <div className="flex flex-col items-center justify-center mt-2">
          <div className="w-28 h-28 md:w-32 md:h-32 rounded-full border-4 border-surface shadow-level-1 relative mb-4 overflow-hidden bg-surface-container-lowest flex items-center justify-center">
            {/* Farmer Avatar Graphic */}
            <div className="w-full h-full bg-primary/10 flex flex-col items-center justify-center text-primary">
              <span className="material-symbols-outlined text-6xl">person_pin</span>
            </div>
            <div className="absolute bottom-0 right-0 bg-secondary text-on-secondary w-9 h-9 rounded-full flex items-center justify-center border-2 border-surface shadow-sm">
              <span className="material-symbols-outlined text-xl font-bold">check</span>
            </div>
          </div>

          <h1 className="font-headline-lg-mobile text-headline-lg-mobile md:font-headline-lg md:text-headline-lg text-primary text-center font-bold">
            आपका आज का विकल्प
          </h1>
          <p className="text-on-surface-variant font-medium mt-1">
            Today's Recommended Market Route
          </p>
        </div>

        {/* Voice Text Bubble */}
        <div className="mt-stack-gap bg-surface-container-lowest rounded-2xl shadow-level-1 border border-outline-variant/30 p-5 flex gap-4 items-start relative">
          <div className="flex-shrink-0 w-12 h-12 bg-surface-container-highest rounded-full flex items-center justify-center text-primary">
            <span className="material-symbols-outlined fill text-2xl">record_voice_over</span>
          </div>
          <div>
            <p className="font-body-lg text-body-lg text-on-surface-variant leading-relaxed font-medium">
              "लासलगाँव मंडी आपका सबसे अच्छा विकल्प है. आपको पास की मंडी की तुलना में ₹5/kg अधिक मिल सकता है."
            </p>
          </div>
          <div className="absolute -top-3 left-8 w-px h-6 bg-outline-variant"></div>
        </div>

        {/* Visual Summary Card */}
        <div className="mt-stack-gap bg-surface-container-lowest rounded-2xl shadow-level-1 border-2 border-primary/15 overflow-hidden">
          <div className="bg-primary/5 px-6 py-4 border-b border-primary/10 flex justify-between items-center">
            <div className="flex items-center gap-3">
              <span className="material-symbols-outlined text-primary text-3xl fill">storefront</span>
              <h2 className="font-headline-lg-mobile text-2xl text-primary font-bold">
                Lasalgaon Mandi (लासलगाँव)
              </h2>
            </div>
            <span className="material-symbols-outlined text-secondary text-2xl fill" title="Verified Mandi">
              verified
            </span>
          </div>

          <div className="p-6 flex flex-col md:flex-row gap-6">
            {/* Highlight Metric */}
            <div className="flex-1 bg-secondary-container/40 rounded-2xl p-5 flex flex-col items-center justify-center border border-secondary-container">
              <span className="font-label-lg text-label-lg text-on-surface-variant mb-1 font-semibold">
                Expected Net Gain (अतिरिक्त मुनाफा)
              </span>
              <div className="flex items-center gap-2">
                <span className="material-symbols-outlined text-secondary text-4xl font-bold">trending_up</span>
                <span className="font-headline-lg-mobile text-3xl md:text-4xl text-secondary font-bold">
                  + ₹5/kg
                </span>
              </div>
            </div>

            {/* Secondary Metrics */}
            <div className="flex-1 flex flex-col gap-3 justify-center">
              <div className="flex items-center gap-4 bg-surface-container-low p-3.5 rounded-xl border border-outline-variant/20">
                <div className="w-10 h-10 rounded-full bg-surface-container-highest flex items-center justify-center text-on-surface-variant">
                  <span className="material-symbols-outlined text-2xl">local_shipping</span>
                </div>
                <div>
                  <p className="text-xs text-outline font-bold uppercase tracking-wider">Distance (दूरी)</p>
                  <p className="font-body-lg text-body-lg text-on-surface font-semibold">12 km</p>
                </div>
              </div>

              <div className="flex items-center gap-4 bg-surface-container-low p-3.5 rounded-xl border border-outline-variant/20">
                <div className="w-10 h-10 rounded-full bg-surface-container-highest flex items-center justify-center text-on-surface-variant">
                  <span className="material-symbols-outlined text-2xl">eco</span>
                </div>
                <div>
                  <p className="text-xs text-outline font-bold uppercase tracking-wider">Commodity (फसल)</p>
                  <p className="font-body-lg text-body-lg text-on-surface font-semibold">Tomato (Grade A)</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Bottom Action Area */}
        <div className="mt-8 flex flex-col gap-3.5">
          <button
            type="button"
            onClick={() => navigate('/')}
            className="w-full h-touch-target-min bg-primary text-on-primary font-label-lg text-label-lg rounded-2xl flex items-center justify-center gap-3 transition-transform active:scale-95 shadow-md font-semibold"
          >
            <span className="material-symbols-outlined fill">home</span>
            <span>होम पर जाएँ (Go to Home)</span>
          </button>

          <button
            type="button"
            onClick={() => navigate('/listening')}
            className="w-full h-touch-target-min bg-surface-container-high text-on-surface font-label-lg text-label-lg rounded-2xl flex items-center justify-center gap-3 transition-colors hover:bg-surface-container-highest active:scale-95 border border-outline-variant font-semibold"
          >
            <span className="material-symbols-outlined fill text-[#FF9800]">mic</span>
            <span>फिर से पूछें (Ask Another Question)</span>
          </button>
        </div>
      </main>

      {/* Mobile Bottom Nav */}
      <BottomNavBar />
    </div>
  );
}
