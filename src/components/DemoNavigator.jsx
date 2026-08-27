import React, { useState } from 'react';
import { NavLink, useLocation } from 'react-router-dom';

const screens = [
  { path: '/presentation', label: '1. AI Presentation (How it Works)' },
  { path: '/', label: '2. Home (Voice Hub)' },
  { path: '/listening', label: '3. Listening State' },
  { path: '/district', label: '4. District Query' },
  { path: '/quantity', label: '5. Quantity Query' },
  { path: '/advice', label: '6. Advice Result' },
  { path: '/trader-offer', label: '7. Trader Offer' },
  { path: '/bargaining', label: '8. Bargaining Assistant' },
  { path: '/daily-alert', label: '9. Daily Alert' },
  { path: '/completion', label: '10. Completion Summary' },
];

export default function DemoNavigator() {
  const [isOpen, setIsOpen] = useState(false);
  const location = useLocation();

  const currentScreen = screens.find((s) => s.path === location.pathname) || { label: 'Explore Screens' };

  return (
    <aside aria-label="SIH Demo Navigation Panel" className="fixed top-20 right-4 z-50">
      {/* Floating Toggle Button */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="bg-primary text-on-primary px-4 py-2 rounded-full text-xs font-semibold shadow-lg hover:bg-primary-container flex items-center gap-1.5 border border-primary-fixed-dim/40 backdrop-blur-md"
        title="Quickly jump between all 10 Kisaan Marg screens for SIH demo"
      >
        <span className="material-symbols-outlined text-sm">dashboard</span>
        <span>Demo Screens ({screens.findIndex(s => s.path === location.pathname) + 1 || '•'}/10)</span>
        <span className="material-symbols-outlined text-sm">
          {isOpen ? 'expand_less' : 'expand_more'}
        </span>
      </button>

      {/* Screen Selector Dropdown */}
      {isOpen && (
        <div className="absolute right-0 mt-2 w-72 bg-surface-container-lowest border-2 border-primary/20 rounded-2xl shadow-2xl p-2 z-50 text-sm max-h-[80vh] overflow-y-auto">
          <div className="px-3 py-2 border-b border-surface-container font-bold text-primary flex items-center justify-between">
            <span>SIH 10-Screen Demo Navigator</span>
            <button
              onClick={() => setIsOpen(false)}
              className="text-on-surface-variant hover:text-primary"
            >
              <span className="material-symbols-outlined text-base">close</span>
            </button>
          </div>
          <div className="flex flex-col gap-1 mt-2">
            {screens.map((screen) => {
              const isActive = location.pathname === screen.path;
              return (
                <NavLink
                  key={screen.path}
                  to={screen.path}
                  onClick={() => setIsOpen(false)}
                  className={`px-3 py-2 rounded-xl text-left font-medium transition-colors flex items-center justify-between ${
                    isActive
                      ? 'bg-secondary-container text-on-secondary-container font-bold'
                      : 'hover:bg-surface-container-low text-on-surface'
                  }`}
                >
                  <span className="truncate">{screen.label}</span>
                  {isActive && (
                    <span className="material-symbols-outlined text-base text-secondary">
                      check_circle
                    </span>
                  )}
                </NavLink>
              );
            })}
          </div>
        </div>
      )}
    </aside>
  );
}
