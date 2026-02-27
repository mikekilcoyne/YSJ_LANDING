# Hotspot Cutout Images

Place cropped element images here. Each should be a **transparent WebP/PNG**
cropped from the original background photo, matching the exact shape of the element.

## Required files

| Filename        | Element            | Notes                                 |
| --------------- | ------------------ | ------------------------------------- |
| `picture1.webp` | Large movie poster | Top-left shelf area ("Midnight")      |
| `picture2.webp` | Small movie poster | Overlapping poster ("Forged in Fury") |
| `jacket1.webp`  | Left jacket        | Leftmost hanging jacket               |
| `jacket2.webp`  | Middle jacket      | Center hanging jacket                 |
| `jacket3.webp`  | Right jacket       | Right-side hanging jacket             |
| `airpods.webp`  | AirPods / device   | Small device on the right side        |

## How to create them

1. Open `bg_desktop_fast.webp` in Photoshop / Figma
2. Select the element (magic wand, pen tool, etc.)
3. Copy to a **new canvas matching the hitbox dimensions**
4. Export as WebP with transparency

## Debug mode

Add `?debug` to the page URL to see hitbox outlines and labels,
making it easy to fine-tune positions in the JS config.
