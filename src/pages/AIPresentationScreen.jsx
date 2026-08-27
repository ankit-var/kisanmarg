import React from 'react';
import { useNavigate } from 'react-router-dom';
import TopAppBar from '../components/TopAppBar';
import BottomNavBar from '../components/BottomNavBar';

export default function AIPresentationScreen({ language = "हिंदी", onLanguageToggle }) {
  const navigate = useNavigate();

  const handleStartPrototype = () => {
    navigate('/');
  };

  return (
    <div className="bg-background text-on-background font-body-lg min-h-screen flex flex-col antialiased">
      {/* TopAppBar */}
      <TopAppBar
        title="Kisaan Marg"
        showBack={false}
        language={language}
        onLanguageToggle={onLanguageToggle}
      />

      {/* Main Content */}
      <main className="flex-grow flex flex-col items-center px-margin-mobile md:px-margin-desktop py-section-gap max-w-[800px] mx-auto w-full pb-28">
        
        {/* Header Section */}
        <div className="text-center mb-8 w-full">
          <div className="inline-flex items-center justify-center bg-primary-container text-on-primary-container rounded-full px-6 py-2.5 mb-4 shadow-sm font-semibold">
            <span className="material-symbols-outlined mr-2 fill">auto_awesome</span>
            <span className="font-label-lg text-label-lg">Kisaan Marg AI • SIH 2024</span>
          </div>
          <h1 className="font-headline-xl text-headline-xl text-primary mb-3 font-bold">
            कैसे काम करता है?
          </h1>
          <p className="font-body-xl text-body-xl text-on-surface-variant max-w-2xl mx-auto">
            किसान मार्ग किसानों को उनकी फसल का सही मूल्य प्राप्त करने के लिए आवाज़-आधारित AI मार्गदर्शक है।
          </p>
        </div>

        {/* Features Bento Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-stack-gap w-full mb-section-gap">
          {/* Feature 1 */}
          <div className="bg-surface-container-lowest rounded-2xl p-6 shadow-card border border-surface-container flex flex-col gap-4 relative overflow-hidden group hover:border-primary/40 transition-all">
            <div className="absolute -right-8 -top-8 w-32 h-32 bg-secondary-container opacity-20 rounded-full group-hover:scale-150 transition-transform duration-500"></div>
            <div className="w-14 h-14 rounded-full bg-primary-container text-on-primary-container flex items-center justify-center z-10 shadow-sm">
              <span className="material-symbols-outlined text-3xl">mic</span>
            </div>
            <h3 className="font-headline-lg-mobile text-2xl text-primary z-10 font-bold">
              1. आपकी आवाज़ समझता है
            </h3>
            <p className="font-body-lg text-body-lg text-on-surface-variant z-10 leading-relaxed">
              बस माइक बटन दबाएं और अपनी भाषा में फसल का नाम, जिला और मात्रा बताएं।
            </p>
          </div>

          {/* Feature 2 */}
          <div className="bg-surface-container-lowest rounded-2xl p-6 shadow-card border border-surface-container flex flex-col gap-4 relative overflow-hidden group hover:border-primary/40 transition-all">
            <div className="absolute -right-8 -top-8 w-32 h-32 bg-secondary-container opacity-20 rounded-full group-hover:scale-150 transition-transform duration-500"></div>
            <div className="w-14 h-14 rounded-full bg-primary-container text-on-primary-container flex items-center justify-center z-10 shadow-sm">
              <span className="material-symbols-outlined text-3xl">query_stats</span>
            </div>
            <h3 className="font-headline-lg-mobile text-2xl text-primary z-10 font-bold">
              2. मंडी के भाव की तुलना
            </h3>
            <p className="font-body-lg text-body-lg text-on-surface-variant z-10 leading-relaxed">
              आस-पास की सभी मंडियों में आज के ताज़ा भाव तुरंत खोजता है और वास्तविक तुलना करता है।
            </p>
          </div>

          {/* Feature 3 */}
          <div className="bg-surface-container-lowest rounded-2xl p-6 shadow-card border border-surface-container flex flex-col gap-4 relative overflow-hidden group hover:border-primary/40 transition-all">
            <div className="absolute -right-8 -top-8 w-32 h-32 bg-secondary-container opacity-20 rounded-full group-hover:scale-150 transition-transform duration-500"></div>
            <div className="w-14 h-14 rounded-full bg-primary-container text-on-primary-container flex items-center justify-center z-10 shadow-sm">
              <span className="material-symbols-outlined text-3xl">local_shipping</span>
            </div>
            <h3 className="font-headline-lg-mobile text-2xl text-primary z-10 font-bold">
              3. ट्रांसपोर्ट खर्च का हिसाब
            </h3>
            <p className="font-body-lg text-body-lg text-on-surface-variant z-10 leading-relaxed">
              दूरी और गाड़ी के भाड़े का सटीक खर्च घटाकर आपको आपकी जेब का शुद्ध मुनाफा (Net Margin) बताता है।
            </p>
          </div>

          {/* Feature 4 */}
          <div className="bg-surface-container-lowest rounded-2xl p-6 shadow-card border border-surface-container flex flex-col gap-4 relative overflow-hidden group hover:border-primary/40 transition-all">
            <div className="absolute -right-8 -top-8 w-32 h-32 bg-secondary-container opacity-20 rounded-full group-hover:scale-150 transition-transform duration-500"></div>
            <div className="w-14 h-14 rounded-full bg-primary-container text-on-primary-container flex items-center justify-center z-10 shadow-sm">
              <span className="material-symbols-outlined text-3xl">record_voice_over</span>
            </div>
            <h3 className="font-headline-lg-mobile text-2xl text-primary z-10 font-bold">
              4. सरल आवाज़ में मोलभाव सलाह
            </h3>
            <p className="font-body-lg text-body-lg text-on-surface-variant z-10 leading-relaxed">
              स्थानीय बोली में बोलकर बताता है कि कौन सी मंडी जाना है और बिचौलियों से क्या भाव माँगना है।
            </p>
          </div>
        </div>

        {/* Prototype Disclaimer */}
        <div className="bg-error-container text-on-error-container rounded-2xl p-5 w-full flex items-start gap-4 mb-8 border border-error/30 shadow-sm">
          <span className="material-symbols-outlined text-3xl text-error mt-0.5">warning</span>
          <p className="font-body-lg text-body-lg font-medium leading-relaxed">
            यह SIH प्रोटोटाइप प्रदर्शन है। यह स्थानीय किसानों की सहायता के लिए डिज़ाइन किया गया वॉयस-फ़र्स्ट इंटरफ़ेस प्रस्तुत करता है।
          </p>
        </div>

        {/* CTA Launch Button */}
        <div className="w-full flex justify-center">
          <button
            type="button"
            onClick={handleStartPrototype}
            className="bg-primary text-on-primary font-label-lg text-label-lg rounded-full px-10 py-4 min-h-[56px] flex items-center justify-center gap-3 hover:bg-primary-container active:scale-95 transition-all w-full md:w-auto shadow-md font-bold text-lg"
          >
            <span>प्रोटोटाइप शुरू करें (Start Voice Assistant)</span>
            <span className="material-symbols-outlined text-2xl">arrow_forward</span>
          </button>
        </div>
      </main>

      {/* Mobile Bottom Nav */}
      <BottomNavBar />
    </div>
  );
}
