---
name: Agro-Humanist Path
colors:
  surface: '#f9fbe7'
  surface-dim: '#d9dcc8'
  surface-bright: '#f9fbe7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f5e1'
  surface-container: '#edf0dc'
  surface-container-high: '#e8ead6'
  surface-container-highest: '#e2e4d1'
  on-surface: '#1a1d11'
  on-surface-variant: '#41493e'
  inverse-surface: '#2f3225'
  inverse-on-surface: '#f0f2df'
  outline: '#717a6d'
  outline-variant: '#c0c9bb'
  surface-tint: '#2a6b2c'
  primary: '#00450d'
  on-primary: '#ffffff'
  primary-container: '#1b5e20'
  on-primary-container: '#90d689'
  inverse-primary: '#91d78a'
  secondary: '#006e1c'
  on-secondary: '#ffffff'
  secondary-container: '#91f78e'
  on-secondary-container: '#00731e'
  tertiary: '#583100'
  on-tertiary: '#ffffff'
  tertiary-container: '#794500'
  on-tertiary-container: '#ffb66b'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#acf4a4'
  primary-fixed-dim: '#91d78a'
  on-primary-fixed: '#002203'
  on-primary-fixed-variant: '#0c5216'
  secondary-fixed: '#94f990'
  secondary-fixed-dim: '#78dc77'
  on-secondary-fixed: '#002204'
  on-secondary-fixed-variant: '#005313'
  tertiary-fixed: '#ffdcbe'
  tertiary-fixed-dim: '#ffb870'
  on-tertiary-fixed: '#2c1600'
  on-tertiary-fixed-variant: '#693c00'
  background: '#f9fbe7'
  on-background: '#1a1d11'
  surface-variant: '#e2e4d1'
typography:
  headline-xl:
    fontFamily: Be Vietnam Pro
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
  headline-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Be Vietnam Pro
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 34px
  body-xl:
    fontFamily: Atkinson Hyperlegible Next
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
  body-lg:
    fontFamily: Atkinson Hyperlegible Next
    fontSize: 20px
    fontWeight: '400'
    lineHeight: 28px
  label-lg:
    fontFamily: Atkinson Hyperlegible Next
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: 0.5px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  touch-target-min: 56px
  gutter: 1.5rem
  margin-mobile: 1rem
  margin-desktop: 4rem
  stack-gap: 1rem
  section-gap: 2.5rem
---

## Brand & Style

The design system is centered on the **Agro-Humanist** aesthetic, specifically tailored for agricultural professionals who prioritize speed, clarity, and reliability over visual complexity. The brand personality is that of a "wise companion"—warm, dependable, and deeply rooted in the physical reality of farming.

The style blends **Modern Professionalism** with **Tactile Minimalist** elements. By using high-contrast surfaces and generous touch targets, the UI compensates for varying literacy levels and environmental factors like outdoor glare. The emotional response is one of safety and empowerment, ensuring that technology feels like a natural extension of the farmer's toolkit rather than a barrier.

## Colors

The palette is derived from the agricultural lifecycle:
- **Primary (#1B5E20):** Deep Forest Green. Used for essential structural elements and high-priority actions to evoke growth and stability.
- **Secondary (#4CAF50):** Leaf Green. Used for success states, active indicators, and secondary navigation.
- **Tertiary (#FF9800):** Saffron. Reserved for critical highlights, warnings, and the primary "Listen" action to ensure maximum visibility against the green landscape.
- **Neutral (#F9FBE7):** Off-White/Cream. A low-strain background color that reduces glare in sunlight compared to pure white.

Surface colors should prioritize high contrast ratios (minimum 7:1 for text) to ensure legibility for users with limited vision or literacy.

## Typography

This design system utilizes **Atkinson Hyperlegible Next** for all functional text to maximize character recognition, which is vital for users with limited literacy. **Be Vietnam Pro** is used for headlines to provide a modern, friendly character.

- **Size Matters:** No text should be smaller than 18px. 
- **Hierarchies:** Use weight (Bold/Semi-Bold) rather than color shifts to denote importance, as color perception varies in bright outdoor light.
- **Bilingual Support:** Ensure line heights are generous (1.4x+) to accommodate the vertical height of Devanagari script characters without clipping.

## Layout & Spacing

The layout follows a **Fluid Content Model** optimized for one-handed thumb interaction. 

- **Grid:** On desktop, a 12-column centered grid is used, but content is capped at 800px to maintain focus. On mobile, a single-column stack is mandatory.
- **Safe Zones:** All primary interaction points (Microphone, Playback) are located in the "bottom-third" of the screen for ergonomic accessibility.
- **Rhythm:** Use an 8px base unit. Gaps between interactive elements (chips, buttons) must be at least 16px to prevent accidental taps.

## Elevation & Depth

This design system uses **Tonal Layering** combined with **Soft Ambient Shadows** to define hierarchy.

- **Level 0 (Background):** The neutral Off-White (#F9FBE7).
- **Level 1 (Cards):** Pure White (#FFFFFF) with a very soft, 10% opacity shadow (12px blur, 4px Y-offset). These represent advice or data.
- **Level 2 (Interactive):** Elements like the Microphone button use a 20% opacity Saffron shadow to create a "floating" effect, indicating it can be pressed.
- **Active State:** When the voice assistant is listening, the primary button should feature a 16px pulsating glow in Saffron (#FF9800) to provide visual feedback that the device is "alive."

## Shapes

The shape language is **Rounded and Friendly**. 

- **Standard Elements:** Use a 0.5rem (8px) radius for cards and input fields.
- **Action Elements:** Use "rounded-xl" (1.5rem) for suggestion chips and large buttons to make them appear softer and more approachable.
- **Primary Voice Action:** The microphone button is a perfect circle, signifying its role as the central "heart" of the interface.

## Components

### Voice Interaction
- **Microphone Button:** An extra-large (88px minimum) circular button. When active, it pulses with a Tertiary Saffron (#FF9800) ring.
- **Audio Playback:** Features a simplified thick-line waveform. Play/Pause buttons are 64px wide to ensure ease of use.
- **Progress Trackers:** Large horizontal segments that fill with Leaf Green (#4CAF50) as steps are completed.

### Navigation & Input
- **Suggestion Chips:** Large, pill-shaped containers with a leading icon (e.g., Tomato icon + "Price" text). Backgrounds are high-contrast white against the off-white page.
- **Interactive Cards:** Information cards use high-contrast headers (Forest Green). Use icons for Mandi stalls, trucks, and currency to provide visual context without requiring reading.

### Feedback
- **Icons:** Use thick, 2px stroke weights. Icons must always be accompanied by text labels, never standalone.
- **Buttons:** All buttons must have a height of at least 56px. Primary buttons use white text on a Forest Green background.