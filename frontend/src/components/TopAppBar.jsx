import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function TopAppBar({ title = "Kisaan Marg", showBack = false, onBack, language = "हिंदी", onLanguageToggle }) {
  const navigate = useNavigate();

  const handleBack = () => {
    if (onBack) {
      onBack();
    } else {
      navigate(-1);
    }
  };

  return (
    <header className="bg-surface dark:bg-surface-dim docked full-width top-0 flex justify-between items-center px-margin-mobile md:px-margin-desktop py-4 w-full z-40 shadow-sm border-b border-surface-container transition-colors duration-200">
      <div className="flex items-center gap-3">
        {showBack ? (
          <button
            onClick={handleBack}
            aria-label="Go Back"
            className="text-primary hover:bg-surface-container-low transition-colors duration-200 p-2 rounded-full flex items-center justify-center h-touch-target-min w-touch-target-min"
          >
            <span className="material-symbols-outlined text-2xl">arrow_back</span>
          </button>
        ) : (
          <button 
            onClick={() => navigate('/')}
            className="flex items-center gap-2 hover:opacity-85 transition-opacity"
            title="Kisaan Marg Home"
          >
            <span className="material-symbols-outlined text-primary fill text-3xl">language</span>
          </button>
        )}
        <h1 
          onClick={() => navigate('/')}
          className="font-headline-lg-mobile text-headline-lg-mobile md:font-headline-lg md:text-headline-lg text-primary tracking-tight font-bold cursor-pointer"
        >
          {title}
        </h1>
      </div>

      {/* Language Switcher */}
      <button
        type="button"
        onClick={onLanguageToggle}
        className="flex items-center gap-1 font-label-lg text-label-lg bg-primary text-on-primary px-5 py-2.5 rounded-full shadow-sm hover:opacity-90 active:scale-95 transition-all min-h-touch-target-min"
        aria-label="Toggle language"
      >
        <span className="material-symbols-outlined text-xl">language</span>
        <span>{language}</span>
        <span className="material-symbols-outlined text-xl">arrow_drop_down</span>
      </button>
    </header>
  );
}
