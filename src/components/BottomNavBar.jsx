import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';

export default function BottomNavBar() {
  const navigate = useNavigate();
  const location = useLocation();

  const isHome = location.pathname === '/';

  return (
    <nav className="md:hidden fixed bottom-0 w-full z-40 flex justify-around items-center h-[76px] px-gutter pb-safe bg-surface-container shadow-[0_-4px_16px_rgba(0,0,0,0.06)] rounded-t-2xl border-t border-outline-variant/30">
      {/* Back Button */}
      <button
        onClick={() => navigate(-1)}
        className="flex flex-col items-center justify-center text-on-surface-variant hover:text-primary active:scale-95 transition-all w-20 py-1"
        aria-label="Back"
      >
        <span className="material-symbols-outlined text-2xl mb-1">arrow_back</span>
        <span className="font-label-lg text-xs font-semibold">Back</span>
      </button>

      {/* Home Button */}
      <button
        onClick={() => navigate('/')}
        className={`flex flex-col items-center justify-center rounded-full px-6 py-1.5 transition-all active:scale-95 ${
          isHome
            ? 'bg-secondary-container text-on-secondary-container font-bold shadow-sm'
            : 'text-on-surface-variant hover:text-primary'
        }`}
        aria-label="Home"
      >
        <span className="material-symbols-outlined text-2xl mb-0.5 fill">home</span>
        <span className="font-label-lg text-xs">Home</span>
      </button>
    </nav>
  );
}
