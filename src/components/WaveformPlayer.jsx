import React, { useState, useEffect } from 'react';

export default function WaveformPlayer({
  initialPlaying = true,
  duration = 12,
  barCount = 12,
  barColor = "bg-primary",
  showReplay = true
}) {
  const [isPlaying, setIsPlaying] = useState(initialPlaying);
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    let interval = null;
    if (isPlaying) {
      interval = setInterval(() => {
        setSeconds((prev) => {
          if (prev >= duration) {
            setIsPlaying(false);
            return duration;
          }
          return prev + 1;
        });
      }, 1000);
    }
    return () => clearInterval(interval);
  }, [isPlaying, duration]);

  const handleToggle = () => {
    if (seconds >= duration) {
      setSeconds(0);
      setIsPlaying(true);
    } else {
      setIsPlaying(!isPlaying);
    }
  };

  const handleReplay = () => {
    setSeconds(0);
    setIsPlaying(true);
  };

  const formattedTime = `0:${seconds < 10 ? '0' : ''}${seconds}`;

  return (
    <div className="bg-surface-container rounded-xl p-4 flex items-center justify-between gap-4 w-full border border-outline-variant/40 shadow-sm">
      {/* Play/Pause Button */}
      <button
        type="button"
        onClick={handleToggle}
        aria-label={isPlaying ? "Pause audio" : "Play audio"}
        className="bg-primary text-on-primary w-14 h-14 rounded-full flex items-center justify-center flex-shrink-0 hover:bg-primary-container active:scale-95 transition-all shadow-md"
      >
        <span className="material-symbols-outlined text-3xl fill">
          {isPlaying ? 'pause' : 'play_arrow'}
        </span>
      </button>

      {/* Waveform Bars */}
      <div className="flex-grow flex items-end justify-center h-10 gap-1.5 overflow-hidden px-2">
        {Array.from({ length: barCount }).map((_, idx) => (
          <div
            key={idx}
            className={`w-2 rounded-t-sm h-full ${barColor} audio-bar ${!isPlaying ? 'paused-anim' : ''} ${
              idx > 6 ? 'hidden sm:block' : ''
            } ${idx > 8 ? 'hidden md:block' : ''}`}
            style={{
              animationDelay: `${(idx * 0.15) % 0.8}s`,
              height: isPlaying ? `${30 + ((idx * 17) % 70)}%` : '20%',
            }}
          />
        ))}
      </div>

      {/* Timer Display */}
      <span className="font-label-lg text-label-lg text-on-surface-variant font-mono shrink-0 min-w-[42px] text-right">
        {formattedTime}
      </span>

      {/* Replay Button */}
      {showReplay && (
        <button
          type="button"
          onClick={handleReplay}
          aria-label="Replay audio"
          className="text-on-surface-variant hover:text-primary w-11 h-11 rounded-full flex items-center justify-center flex-shrink-0 hover:bg-surface-variant active:scale-95 transition-colors"
        >
          <span className="material-symbols-outlined text-2xl">replay</span>
        </button>
      )}
    </div>
  );
}
