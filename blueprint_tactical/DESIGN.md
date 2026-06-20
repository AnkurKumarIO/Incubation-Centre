---
name: Blueprint Tactical
colors:
  surface: '#0a1519'
  surface-dim: '#0a1519'
  surface-bright: '#303b3f'
  surface-container-lowest: '#051014'
  surface-container-low: '#121d21'
  surface-container: '#162125'
  surface-container-high: '#202c30'
  surface-container-highest: '#2b363b'
  on-surface: '#d8e4ea'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#d8e4ea'
  inverse-on-surface: '#273236'
  outline: '#849495'
  outline-variant: '#3b494b'
  surface-tint: '#00dbe9'
  primary: '#dbfcff'
  on-primary: '#00363a'
  primary-container: '#00f0ff'
  on-primary-container: '#006970'
  inverse-primary: '#006970'
  secondary: '#ffb4a7'
  on-secondary: '#640c05'
  secondary-container: '#842418'
  on-secondary-container: '#ff9a89'
  tertiary: '#f5f5f5'
  on-tertiary: '#2f3131'
  tertiary-container: '#d9d9d9'
  on-tertiary-container: '#5d5f5f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#7df4ff'
  primary-fixed-dim: '#00dbe9'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#ffdad4'
  secondary-fixed-dim: '#ffb4a7'
  on-secondary-fixed: '#400100'
  on-secondary-fixed-variant: '#842418'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#0a1519'
  on-background: '#d8e4ea'
  surface-variant: '#2b363b'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-mono:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.5'
    letterSpacing: 0.08em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '700'
    lineHeight: '1.2'
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  grid-cols: '12'
---

## Brand & Style

The design system is an architectural, high-tech framework designed for V3F VENTURES. It evokes the precision of a digital drafting board, blending high-end venture capital professionalism with the raw energy of frontier technology. The aesthetic is "Structural Futurism"—combining the clarity of architectural blueprints with the immersive depth of modern glassmorphism.

The visual narrative is defined by:
- **Architectural Wireframes:** UI elements are treated as schematic components rather than static boxes.
- **Glassmorphism:** Deep, translucent layers provide a sense of spatial intelligence and data density.
- **Precision Detailing:** 1px hairline rules, technical node indicators, and isometric grid overlays create an environment of extreme accuracy and foresight.

## Colors

The palette is anchored in **Void Black**, creating an infinite canvas for high-contrast technical data. 
- **Blueprint Cyan** is the functional lead, used for interactive states, hairline borders, and glowing accents that represent "active energy."
- **Coral Accent** is utilized sparingly for critical calls to action or "hot" data points, providing a warm organic contrast to the cool tech aesthetic.
- **Structural White** and **Muted Gray** manage the information hierarchy, ensuring readability against the deep background.

## Typography

This design system utilizes a tiered typographic approach to separate brand impact from technical data.
- **Headlines:** Space Grotesk is used in bold, condensed formats to mirror structural engineering documents. Use tight letter-spacing for large titles.
- **Body:** Inter provides a clean, neutral balance, ensuring complex venture data remains highly legible across all screen sizes.
- **Labels:** JetBrains Mono is the "data layer," used for metadata, timestamps, and technical annotations, always paired with uppercase styling for a systematic feel.

## Layout & Spacing

The system is built on a **12-column isometric grid** philosophy. 
- **The 4px Baseline:** All spacing, padding, and margins must be multiples of 4 to maintain mathematical consistency.
- **Gutter & Margins:** Large 64px outer margins on desktop create a "centered terminal" feel.
- **Responsive Behavior:** On mobile, margins shrink to 16px, and the 12-column grid collapses to a 4-column layout. Elements should feel pinned to the grid, often separated by the 1px Cyan hairline rules rather than wide gaps.

## Elevation & Depth

Depth is conveyed through transparency and luminosity rather than traditional shadows.
- **The Glass Layer:** Containers use `rgba(255, 255, 255, 0.08)` borders with a `backdrop-filter: blur(12px)`.
- **Luminous Glow:** Active elements (like primary buttons or selected nodes) emit a soft `0px 0px 15px rgba(0, 240, 255, 0.4)` outer glow.
- **Z-Axis Hierarchy:** Background elements utilize isometric grid patterns at 5% opacity. Foreground containers sit atop these grids with higher blur values to create separation.

## Shapes

The shape language is a dichotomy of hard lines and fluid interaction.
- **Structural Containers:** Use a `0px` (Sharp) radius or very subtle `4px` (Soft) radius to maintain the architectural blueprint feel.
- **Interactive Elements:** Buttons and tags utilize a **Pill-shaped (3)** radius. This creates a clear distinction between the "infrastructure" (the grid) and "tools" (the buttons).

## Components

- **Buttons:** Primary buttons are pill-shaped with a solid **Coral Accent** or **Blueprint Cyan** fill. On hover, they trigger a sharp transition to a 1px border with a high-intensity glow effect.
- **Input Fields:** Styled as "terminal prompts"—flat, underlined with a 1px Cyan rule, using **JetBrains Mono** for user-entered text. Focus states trigger a vertical cursor blink.
- **Cards:** Glassmorphic containers with 1px `rgba(255, 255, 255, 0.08)` borders. Each corner features a "crosshair" node icon to emphasize the architectural theme.
- **Technical Nodes:** Small, circular Blueprint Cyan indicators used in lists or on graphs to represent data points or status.
- **Lists:** Rows are separated by 1px horizontal rules. Every list item should have a technical index (e.g., `01`, `02`) in monospace font to the left.