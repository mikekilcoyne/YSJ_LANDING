# Gemini Handoff: Breakfast Qwest

## Project
- Repo: `/Users/mikekilcoyne/Desktop/YSJ_LATEST`
- Main working page: `/Users/mikekilcoyne/Desktop/YSJ_LATEST/breakfast-qwest.html`
- Local preview: `http://localhost:4173/breakfast-qwest.html`
- Existing YSJ landing page remains separate in `/Users/mikekilcoyne/Desktop/YSJ_LATEST/index.html`

## Current Goal
Build a `Breakfast Qwest` sub-page for the YSJ site that feels:
- clean
- mobile-friendly
- game-world / cinematic
- slightly handwritten / analog in spirit, but not messy
- more visually aligned with the user's motion assets than with a white notebook mockup

The user specifically likes the speed/aesthetic instincts Gemini tends to bring, so prioritize visual cohesion and taste.

## Current State
`breakfast-qwest.html` already exists and includes:
- full-screen looping background video
- top title slot using converted transparent title animation
- `Read Intro` button opening a modal/lightbox
- region-based club sections
- city-level checklist behavior
- local persistence via `localStorage`
- archive support
- attended date text input
- links for Instagram / LinkedIn / WhatsApp / Maps where available

## Important Current Behavior
- Checked items should stay visible in the main/default view.
- When checked, cities should simply look cleanly struck through.
- Archive is separate from completion.
- Attended dates are plain text using `YYYY-MM-DD` to avoid buggy browser date picker behavior.

## Assets In Use

### Background
- Source file on disk: `/Users/mikekilcoyne/Downloads/04_video/BACKGROUND_CLEAN.mp4`
- Repo path in page: `/Users/mikekilcoyne/Desktop/YSJ_LATEST/assets/video/BACKGROUND_CLEAN.mp4`
- Current implementation: full-screen looping background video with subtle black overlay
- Background playback is intentionally slowed to `0.6x`

### Title Animation
- Source file on disk: `/Users/mikekilcoyne/Downloads/04_video/BK_QUEST_ALPHA.mxf`
- This MXF is ProRes 4444 with alpha
- Converted web asset: `/Users/mikekilcoyne/Desktop/YSJ_LATEST/assets/title/BK_QUEST_ALPHA.webm`
- Current implementation: top title video slot in `breakfast-qwest.html`

## Design Direction From User
The user wants:
- the title media to be the hero
- the top section to feel super-clean
- less of the earlier white paper/card treatment in the hero area
- a separate background layer behind the content
- `Read Intro` as a menu-style item that opens a lightbox essay
- more of a video-game aesthetic overall

They previously liked:
- some of the clarity and softness from `Just For Today`
- the utility/actionability of card info from `FIND_MY_BK_CLUB`

But the current direction is shifting more toward:
- cinematic
- motion-led
- minimal top framing
- cleaner, darker, more intentional hero treatment

## Data Source
The checklist content is based on the BC International clubs Google Sheet:
- `https://docs.google.com/spreadsheets/d/1_4MoIXgSHjERztj0LPPC-XAa7nzFlfrdcjEQdBeSqto/edit?usp=sharing`

Club data is currently hardcoded inside `breakfast-qwest.html`.

## Relevant Reference Repos On Disk

### Find My Breakfast Club
- `/Users/mikekilcoyne/Desktop/FIND_MY_BK_CLUB`
- Useful for:
  - club card information hierarchy
  - contact/action links
  - practical club metadata

### Just For Today
- temp clone used for reference:
  - `/tmp/just-for-today-codex`
- Useful for:
  - cream/stone UI language
  - card softness
  - typography rhythm

## Likely Next Improvements
- Refine top hero composition around the title animation
- Decide whether the title should:
  - loop
  - play once and hold
  - scale larger
  - sit lower in frame
- Push the rest of the page styling slightly more toward the game aesthetic so the hero and checklist feel like one world
- Potentially reduce or restyle the section/card chrome below the hero
- Possibly make the `Read Intro` trigger feel even more like a game menu item
- Consider whether stats row still belongs visually

## Implementation Notes
- This is currently a single-file static page with inline CSS and JS.
- No framework is involved.
- The local server was started with:
  - `python3 -m http.server 4173`
- If the server is no longer running, restart it from repo root.

## Git Status At Handoff
Uncommitted local work exists:
- `/Users/mikekilcoyne/Desktop/YSJ_LATEST/breakfast-qwest.html`
- `/Users/mikekilcoyne/Desktop/YSJ_LATEST/assets/video/`
- `/Users/mikekilcoyne/Desktop/YSJ_LATEST/assets/title/`

## Ask For Gemini
Please take over aesthetic refinement of `breakfast-qwest.html` with emphasis on:
- stronger game-title hero presentation
- cleaner top section
- cohesive background/title/content relationship
- preserving usability of the checklist below

Do not remove:
- persistent checklist behavior
- archive behavior
- attended date entry
- direct contact/action links

## Revisions Implemented (Gemini)
- Replaced the heavy video background with a lightweight `BACKGROUND_SQUISHY.gif` and removed all grain masks so the pixel-art shines cleanly.
- Overhauled `breakfast-qwest.html` entirely with a 16-bit SNES UI design system.
- Styled `.city-card` boxes with vertical ocean-blue-to-yellow gradients mirroring the background, wrapped in heavy square pixel borders and blocky box shadows.
- Dropped in blocky 8-bit SVGs for the Maps and Archive action icons.
- Built a multi-stage cinematic load sequence: The massive "BREAKFAST QWEST" title descends into frame (like Castlevania IV) over 5.5s, seamlessly triggering the drop-in of the subheader, the direct-scroll "START QWEST" anchor, the "WHY QWEST?" modal trigger, and the checklist grid.
- Integrated robust "SAVE DATA" / "LOAD DATA" JSON export buttons inside the toolbar to structurally back up user checklist progress beyond standard browser `localStorage`.
- All updates securely committed to the Git repository.

## Pending Tweaks for Finalization
1. **"Why Qwest?" Modal Content:** The actual story text inside the intro modal window needs to be written out and confirmed.
2. **Search Bar Tweaks:** The search bar inside the toolbar could be squared off further or given a custom 8-bit font payload if it feels slightly out of place.
3. **Mobile Responsiveness:** A final pass on the mobile (sub-768px) breakpoint to ensure the thick shadows and rigid 16-bit card layout doesn't horizontally break the viewport constraints.
