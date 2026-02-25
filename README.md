# Yellow Satin Jacket - Landing Page

The single-page landing gate for [yellowsatinjacket.com](https://yellowsatinjacket.com).

## 🚀 Quick Start
- **Main Entry:** `index.html`
- **Local Preview:** Open `index.html` in any browser.
- **Deploy:** `npx netlify deploy --prod`

## 📁 Project Structure
- `index.html` - Core site (HTML, CSS, JS)
- `assets/` - Production assets (Favicons, Silly Mode BG)
- `bg_desktop_fast.webp` - Optimized desktop background
- `bg_mobile_fast.webp` - Optimized mobile background
- `*.otf` - Neon signage fonts
- `#archives/` - Unused/Original high-res assets, glitch videos, and test renders. (Ignored by Git/Netlify)

## 🛠 Features
- **Neon Signage:** Pinned to background shelf coordinates via JS with iterative scaling for responsive fit.
- **Visual States:**
  - *At Rest:* Subtle flickering neon outline/border using `screen` blend mode.
  - *Hover:* Full-glow highlighted state with energized yellow tube fill.
- **Vimeo Lightbox:** Click 'PLAY TRAILER' to open.
- **Silly Mode:** Hidden hitbox on AirPods area opens an alternative overlay.

## 📝 Recent Improvements
- Optimized "PLAY TRAILER" neon sign responsiveness.
- Fixed clipping at high browser zoom levels using iterative shrink loop.
- Refined flicker animations for a "living" neon look.
- Cleaned up project structure for deployment.

---
*Maintained by Antigravity*
