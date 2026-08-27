import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import TopAppBar from '../components/TopAppBar';

const districts = [
  { name: "Nashik", icon: "location_on" },
  { name: "Pune", icon: "location_on" },
  { name: "Ahmednagar", icon: "location_on" },
  { name: "Solapur", icon: "location_on" },
];

export default function DistrictQueryScreen({ language = "हिंदी", onLanguageToggle }) {
  const navigate = useNavigate();
  const [selectedDistrict, setSelectedDistrict] = useState("Nashik");
  const [isListening, setIsListening] = useState(false);
  const [isPlayingAudio, setIsPlayingAudio] = useState(false);

  const handleConfirm = (district) => {
    const chosen = district || selectedDistrict;
    navigate('/quantity', { state: { district: chosen } });
  };

  const handleMicToggle = () => {
    setIsListening(!isListening);
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
      <main className="flex-grow flex flex-col px-margin-mobile md:px-margin-desktop py-section-gap max-w-[800px] mx-auto w-full pt-6 md:pt-10 pb-36">
        
        {/* Progress Tracker */}
        <div aria-label="Progress: Step 1 of 2" className="w-full mb-6">
          <div className="flex gap-2 h-3 rounded-full overflow-hidden bg-surface-container-highest">
            <div className="w-1/2 bg-secondary rounded-full"></div>
            <div className="w-1/2 bg-transparent rounded-full"></div>
          </div>
          <p className="font-label-lg text-label-lg text-on-surface-variant mt-2 text-right font-semibold">
            Step 1 of 2
          </p>
        </div>

        {/* Question Section */}
        <div className="flex flex-col items-center text-center mb-8 gap-stack-gap bg-surface-container-lowest p-6 md:p-8 rounded-2xl shadow-[0_4px_16px_rgba(0,0,0,0.06)] border border-surface-container-highest">
          <button
            type="button"
            onClick={() => setIsPlayingAudio(!isPlayingAudio)}
            aria-label="Play question audio"
            className={`w-16 h-16 rounded-full flex items-center justify-center transition-all shadow-sm ${
              isPlayingAudio
                ? 'bg-secondary-container text-on-secondary-container scale-105'
                : 'bg-surface-container-low text-primary hover:bg-surface-container'
            }`}
          >
            <span className="material-symbols-outlined text-4xl fill">volume_up</span>
          </button>
          <h2 className="font-headline-xl text-headline-xl text-primary-container font-bold">
            आपका जिला कौन सा है?
          </h2>
          <p className="font-body-xl text-body-xl text-on-surface-variant">
            (Which is your district?)
          </p>
        </div>

        {/* Spoken Voice Confirmation Card */}
        <div className="flex flex-col items-center gap-4 mb-8">
          <div className="flex items-center gap-2 text-primary font-headline-lg-mobile font-semibold">
            <span className="material-symbols-outlined text-3xl">mic</span>
            <span>अपना जिला बोलें</span>
          </div>
          <div className="w-full bg-surface-container-low p-6 rounded-2xl border-2 border-dashed border-primary/30 flex flex-col items-center gap-4 shadow-sm">
            <p className="text-on-surface-variant font-body-lg">आपने कहा:</p>
            <p className="text-headline-xl font-headline-xl text-primary font-bold">{selectedDistrict}</p>
            <div className="flex gap-4 w-full mt-2">
              <button
                type="button"
                onClick={() => handleConfirm(selectedDistrict)}
                className="flex-grow bg-secondary text-on-secondary font-label-lg py-4 rounded-full shadow-sm hover:opacity-90 transition-all active:scale-95 font-semibold text-center"
              >
                हाँ, यही है (Next)
              </button>
              <button
                type="button"
                onClick={() => setSelectedDistrict("")}
                className="flex-grow border-2 border-outline text-on-surface font-label-lg py-4 rounded-full hover:bg-surface-container-lowest transition-all active:scale-95 font-semibold text-center"
              >
                दूसरा जिला
              </button>
            </div>
          </div>
        </div>

        {/* District List Options */}
        <p className="font-label-lg text-label-lg text-on-surface-variant mb-3 px-2 font-semibold">
          या सूची में से चुनें:
        </p>
        <div className="flex flex-col gap-3.5 w-full">
          {districts.map((d) => (
            <button
              key={d.name}
              type="button"
              onClick={() => handleConfirm(d.name)}
              className="flex items-center gap-4 bg-surface-container-lowest hover:bg-surface-container-low p-4 rounded-2xl shadow-[0_2px_8px_rgba(0,0,0,0.04)] border border-surface-container-highest transition-all duration-200 active:scale-[0.99] h-[76px] w-full text-left group"
            >
              <div className="w-12 h-12 bg-secondary-container rounded-full flex items-center justify-center text-on-secondary-container group-hover:bg-primary-container group-hover:text-on-primary transition-colors">
                <span className="material-symbols-outlined text-2xl">{d.icon}</span>
              </div>
              <span className="font-body-xl text-body-xl text-on-surface flex-grow font-semibold">
                {d.name}
              </span>
              <span className="material-symbols-outlined text-outline-variant group-hover:text-primary transition-colors">
                arrow_forward_ios
              </span>
            </button>
          ))}
        </div>
      </main>

      {/* Voice Input Floating Action Button */}
      <div className="fixed bottom-0 left-0 w-full p-6 md:p-8 flex justify-center pb-safe z-40 bg-gradient-to-t from-background via-background/90 to-transparent pointer-events-none">
        <div className="relative pointer-events-auto">
          <div className={`absolute inset-0 bg-[#FF9800] rounded-full transition-opacity duration-300 ${isListening ? 'pulse-effect opacity-80' : 'opacity-0'}`}></div>
          <button
            type="button"
            onClick={handleMicToggle}
            aria-label="Tap to speak"
            className={`relative z-10 w-[88px] h-[88px] rounded-full flex items-center justify-center shadow-[0_8px_24px_rgba(255,152,0,0.35)] transition-all duration-300 hover:scale-105 active:scale-95 ${
              isListening ? 'bg-[#FF9800] text-white' : 'bg-primary-container text-on-primary'
            }`}
          >
            <span className="material-symbols-outlined text-4xl fill">mic</span>
          </button>
        </div>
      </div>
    </div>
  );
}
