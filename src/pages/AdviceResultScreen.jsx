import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import TopAppBar from '../components/TopAppBar';
import BottomNavBar from '../components/BottomNavBar';
import WaveformPlayer from '../components/WaveformPlayer';

export default function AdviceResultScreen({ language = "हिंदी", onLanguageToggle }) {
  const navigate = useNavigate();
  const location = useLocation();
  const district = location.state?.district || "Nashik";
  const quantity = location.state?.quantity || "500 Kg";

  return (
    <div className="bg-background text-on-background min-h-screen pb-safe antialiased flex flex-col">
      {/* TopAppBar */}
      <TopAppBar
        title="Kisaan Marg"
        showBack={true}
        language={language}
        onLanguageToggle={onLanguageToggle}
      />

      {/* Main Content */}
      <main className="max-w-[800px] mx-auto px-margin-mobile md:px-margin-desktop py-section-gap flex flex-col gap-6 pb-28 flex-1 w-full">
        
        {/* Header Section */}
        <section className="flex flex-col gap-2 items-center text-center">
          <div className="flex items-center gap-2 text-tertiary-container bg-tertiary-fixed px-5 py-2 rounded-full shadow-[0_4px_12px_rgba(255,152,0,0.15)] font-bold">
            <span className="material-symbols-outlined icon-thick fill text-xl">auto_awesome</span>
            <span className="font-label-lg text-label-lg">AI सलाह (Market Advice)</span>
          </div>
          <h2 className="font-headline-xl text-headline-xl text-primary-container mt-3 font-bold">
            आज लासलगाँव मंडी में बेचें
          </h2>
          <p className="text-on-surface-variant font-medium">
            जिला: {district} • मात्रा: {quantity}
          </p>
        </section>

        {/* Main Advice Card with Audio Waveform */}
        <section className="bg-surface-container-lowest rounded-2xl shadow-[0_4px_16px_rgba(0,0,0,0.06)] p-gutter border border-surface-container-highest">
          <div className="flex flex-col gap-stack-gap">
            {/* Spoken Text */}
            <p className="font-body-xl text-body-xl text-on-surface text-center md:text-left leading-relaxed">
              "लासलगाँव मंडी में टमाटर का भाव ₹26 प्रति किलो है। परिवहन का खर्च निकालकर आपको ₹23 प्रति किलो बचेंगे, जो कि आपके पास की मंडी से ₹5 प्रति किलो ज़्यादा है।"
            </p>

            {/* Audio Player UI */}
            <WaveformPlayer duration={14} barCount={12} barColor="bg-primary" />
          </div>
        </section>

        {/* Visual Fact Cards Grid */}
        <section className="grid grid-cols-1 md:grid-cols-3 gap-stack-gap">
          {/* Best Net Price */}
          <div className="bg-surface-container-lowest rounded-2xl p-5 shadow-sm border border-surface-container-highest flex flex-col items-center justify-center text-center gap-2">
            <div className="w-12 h-12 bg-primary-fixed rounded-full flex items-center justify-center text-on-primary-fixed mb-1">
              <span className="material-symbols-outlined icon-thick text-2xl">currency_rupee</span>
            </div>
            <span className="font-label-lg text-label-lg text-on-surface-variant font-semibold">शुद्ध भाव (Net)</span>
            <span className="font-headline-lg-mobile text-headline-lg-mobile text-primary-container font-bold">₹23/kg</span>
          </div>

          {/* Extra Earning */}
          <div className="bg-surface-container-lowest rounded-2xl p-5 shadow-sm border border-secondary-container flex flex-col items-center justify-center text-center gap-2 relative overflow-hidden">
            <div className="absolute inset-0 bg-secondary-fixed opacity-10 pointer-events-none"></div>
            <div className="w-12 h-12 bg-secondary-container rounded-full flex items-center justify-center text-on-secondary-container mb-1 z-10">
              <span className="material-symbols-outlined icon-thick text-2xl">trending_up</span>
            </div>
            <span className="font-label-lg text-label-lg text-on-surface-variant z-10 font-semibold">अतिरिक्त कमाई (Gain)</span>
            <span className="font-headline-lg-mobile text-headline-lg-mobile text-secondary z-10 font-bold">+₹5/kg</span>
          </div>

          {/* Distance */}
          <div className="bg-surface-container-lowest rounded-2xl p-5 shadow-sm border border-surface-container-highest flex flex-col items-center justify-center text-center gap-2">
            <div className="w-12 h-12 bg-tertiary-fixed rounded-full flex items-center justify-center text-on-tertiary-fixed mb-1">
              <span className="material-symbols-outlined icon-thick text-2xl">local_shipping</span>
            </div>
            <span className="font-label-lg text-label-lg text-on-surface-variant font-semibold">दूरी (Distance)</span>
            <span className="font-headline-lg-mobile text-headline-lg-mobile text-tertiary font-bold">42 km</span>
          </div>
        </section>

        {/* Action Buttons */}
        <section className="flex flex-col gap-4 mt-2">
          <button
            type="button"
            onClick={() => navigate('/trader-offer')}
            className="w-full h-touch-target-min bg-primary text-on-primary rounded-full font-label-lg text-label-lg flex items-center justify-center gap-2 shadow-md hover:bg-primary-container active:scale-95 transition-all font-semibold"
          >
            <span className="material-symbols-outlined">call</span>
            व्यापारी का भाव जाँचें (Check Trader Offer)
          </button>

          <button
            type="button"
            onClick={() => navigate('/daily-alert')}
            className="w-full h-touch-target-min bg-surface-container-high text-on-surface rounded-full font-label-lg text-label-lg flex items-center justify-center gap-2 shadow-sm hover:bg-surface-container-highest active:scale-95 transition-all border border-outline-variant font-semibold"
          >
            <span className="material-symbols-outlined">notifications_active</span>
            रोज़ का अलर्ट लगाएँ (Set Daily Alert)
          </button>
        </section>

        {/* Disclaimer */}
        <p className="font-body-lg text-body-lg text-on-surface-variant text-center opacity-80 pt-2">
          * यह AI आधारित अनुमान है, कृपया मंडी जाने से पहले भाव की पुष्टि कर लें।
        </p>
      </main>

      {/* Mobile Nav */}
      <BottomNavBar />
    </div>
  );
}
