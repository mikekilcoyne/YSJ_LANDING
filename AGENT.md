# YSJ Landing Page Handoff

## Project Location
- Root: `/Users/yellowsatinjacket/Desktop/YSJ_LANDING_PAGE`
- Main page: `/Users/yellowsatinjacket/Desktop/YSJ_LANDING_PAGE/index.html`

## Current Goal
- Finalize a pinned, responsive `PLAY TRAILER` neon sign over the shelf block.
- Keep text/sign aligned across viewport sizes and aggressive browser zoom.
- Preserve YSJ brand colors:
  - Hollywood Yellow: `#FDD66`
  - YSJ Off-White: `#E8E8E8`
  - YSJ Black: `#1C1C1C`

## Assets In Use
- Desktop background (compressed high-res): `bg_desktop_fast.webp` (2880x1620)
- Mobile background (compressed): `bg_mobile_fast.webp` (1440x1799)
- Fonts:
  - `NCLNeovibes-Regular.otf`
  - `NCLNeovibes-Outline.otf`
- Silly mode bg: `assets/silly_bg.gif`
- Favicon/social prep created:
  - `boo-favicon.png`
  - `apple-touch-icon.png`
  - `social-preview.jpg`

## What Was Implemented
- Trailer is clickable and opens Vimeo lightbox.
- Text/sign position is pinned to image coordinates using `object-fit: cover` math.
- Separate desktop/mobile pin anchors exist in JS.
- Sign has dynamic font scaling from image width.
- Attempted shelf-fit clamp exists to keep sign inside the shelf bounds.
- Pink underline+arrow callout added under text (`::after` + `::before`) and always on.
- Right-side standalone marker arrow was removed.
- Hidden clickable AirPods-area hitbox opens Silly Mode overlay.

## Current Important Code Areas
- CSS neon/sign styles: `.neon-wrapper`, `.neon-link`, `.neon-fill`, `.neon-outline`
- Underline callout: `.neon-link::after`, `.neon-link::before`
- Pinning + scale logic: `syncPinnedNeon()` in `<script>`
- Pin config object: `const pin = { ... }`

## Repeated User Mentions Not Fully Resolved
1. Interior tube glow on hover
- User repeatedly says only exterior glow appears, not true interior yellow tube fill.
- Current hover styles set `.neon-fill` to `#FDD66` with glow, but visual still reads mostly as outline glow.
- Likely conflict with blend mode + stacked outline layer + text rendering.

2. Breaks/clips at high browser zoom (e.g. 250%)
- User repeatedly shared clipping screenshots.
- There is a fit pass (`maxShelfWidth/maxShelfHeight`), but clipping still occurs.
- Current min font sizes may still be too high for extreme zoom.
- One-pass fit scaling can be insufficient; may need iterative fit and/or width-safe scaling by measured text bounds.

3. Blend mode tuning
- User wanted “part of environment” + still legible + hard yellow hover glow.
- Tried `lighten`, `overlay`, `soft-light`, then back and forth.
- Current default blend may still be suppressing interior fill read.

4. Size/position parity vs browser zoom
- User wants what they see at 67%/90% to match at 100%.
- This is difficult because browser zoom changes CSS pixel scale.
- Need robust viewport-independent fit strategy and possibly reduced dependency on large glow blur radius.

## User-Preferred Visual Direction (Latest)
- Keep current blend behavior that “vibes” with environment.
- On hover: interior must clearly pop to YSJ yellow (`#FDD66`) like a tube energizing.
- Underline arrow should remain always-on pink neon and aligned responsively.
- `PLAY TRAILER` must remain inside the shelf sign region at extreme zoom.

## Suggested Fix Strategy For Next Agent
1. Fix zoom clipping first (hard requirement)
- In `syncPinnedNeon()`:
  - compute target font from drawnWidth as now
  - then iterate shrink until:
    - neon wrapper width <= shelf width budget
    - neon wrapper height <= shelf height budget
  - allow lower mins at extreme zoom
  - include padding/underline in fit budget or reduce pseudo offsets with font size

2. Force interior fill read on hover
- Consider temporarily reducing outline opacity on hover so fill is visible.
- Use stronger fill color + inner glow:
  - `color: #FDD66`
  - add tighter bright inner shadow + medium outer shadow
- Keep outline glow but avoid overpowering fill.

3. Blend mode compromise
- Suggested: default `soft-light` or `overlay`, hover `lighten`.
- If interior still muted, switch `.neon-fill` to `mix-blend-mode: normal` always, while wrapper blend handles environmental integration.

4. Validate at:
- 100% zoom
- 150%
- 250%
- narrow desktop widths
- iPhone width

## Deployment Intent
- User intends to push live to `yellowsatinjacket.com` after final styling lock.
- Netlify deploy skill is available at:
  - `/Users/yellowsatinjacket/.codex/skills/netlify-deploy/SKILL.md`
- Not deployed in this handoff step.

## Notes
- Keep changes in `index.html` unless splitting into CSS/JS improves reliability.
- Preserve current functional wiring (lightbox + silly hitbox) unless user asks otherwise.
