---
name: Modern Urban Folk
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#464555'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#777587'
  outline-variant: '#c7c4d8'
  surface-tint: '#4d44e3'
  primary: '#3525cd'
  on-primary: '#ffffff'
  primary-container: '#4f46e5'
  on-primary-container: '#dad7ff'
  inverse-primary: '#c3c0ff'
  secondary: '#9f402d'
  on-secondary: '#ffffff'
  secondary-container: '#fd876f'
  on-secondary-container: '#732010'
  tertiary: '#5d4500'
  on-tertiary: '#ffffff'
  tertiary-container: '#7a5c00'
  on-tertiary-container: '#ffd77d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2dfff'
  primary-fixed-dim: '#c3c0ff'
  on-primary-fixed: '#0f0069'
  on-primary-fixed-variant: '#3323cc'
  secondary-fixed: '#ffdad3'
  secondary-fixed-dim: '#ffb4a5'
  on-secondary-fixed: '#3e0500'
  on-secondary-fixed-variant: '#802918'
  tertiary-fixed: '#ffdf9a'
  tertiary-fixed-dim: '#f7be1d'
  on-tertiary-fixed: '#251a00'
  on-tertiary-fixed-variant: '#5a4300'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  headline-lg:
    fontFamily: Outfit
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Outfit
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Outfit
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
  max-width: 1440px
---

## Brand & Style
The design system is built on the concept of "Modern Urban Folk." It balances the systematic efficiency of a global utility with the warmth of a local community center. The UI should evoke a sense of belonging, clarity, and vibrancy.

The style blends **Minimalism** with **Tactile** elements. We use generous white space and a structured grid to manage information density, while introducing "warm utility" through organic color accents and soft, approachable geometry. The emotional response should be one of "organized discovery"—a professional tool that feels like a friendly neighbor.

## Colors
The palette is rooted in "Stitch Blue," a vibrant indigo that provides a digital-first anchor. This is balanced by "Terracotta" (Secondary) and "Mustard" (Tertiary) to inject earthy, human warmth into the neighborhood dashboard.

- **Primary (Stitch Blue):** Used for primary actions, active states, and brand-critical wayfinding.
- **Secondary (Terracotta):** Used for communal events, social indicators, and warm highlights.
- **Tertiary (Mustard):** Used for alerts, sunshine/weather data, and secondary accents.
- **Background:** A soft off-white (`#F8F9FA`) ensures that white surface cards have enough contrast to appear elevated without harsh transitions.

## Typography
The typography strategy pairs the geometric friendliness of **Outfit** for headings with the industrial clarity of **Inter** for functional text. 

Headings should be set with tighter letter-spacing to feel "stitched" and cohesive. Body text prioritizes legibility with generous line heights. For data-heavy dashboard elements, use `label-sm` in uppercase to create clear semantic separation between content and metadata.

## Layout & Spacing
The design system utilizes a **Fluid Grid** with a fixed maximum width for desktop environments. The layout is modeled on a 12-column system for desktop and a 4-column system for mobile.

- **The Dashboard Canvas:** Cards should span variable column widths (e.g., 3, 4, or 6 columns) depending on data priority.
- **Rhythm:** All margins, paddings, and gaps must be multiples of the 8px base unit. 
- **Reflow:** On mobile, the sidebar collapses into a bottom navigation bar or a hidden drawer, and dashboard cards stack vertically to fill the full width of the screen minus the 16px side margins.

## Elevation & Depth
Depth is created through **Ambient Shadows** and tonal layering. Since the background is off-white, white cards (`#FFFFFF`) serve as the primary interactive surface.

- **Level 1 (Cards):** Use a soft, diffused shadow: `0px 4px 20px rgba(0, 0, 0, 0.05)`.
- **Level 2 (Active/Hover):** When a user interacts with a card, the shadow should deepen and the card should slightly lift: `0px 8px 30px rgba(0, 0, 0, 0.08)`.
- **Level 3 (Modals/Popovers):** Higher elevation with a tighter, darker core shadow to signify focus.
- **Sidebar:** The sidebar uses a subtle right-hand border (`1px solid #E5E7EB`) rather than a shadow to maintain a clean, "stitched" architectural feel.

## Shapes
The shape language is consistently "Rounded" to maintain the approachable, friendly vibe of a neighborhood dashboard. 

- **Cards & Containers:** Use 16px (`1rem`) corner radii.
- **Buttons & Chips:** Use the `rounded-xl` setting (24px or fully pill-shaped) to distinguish interactive triggers from static information containers.
- **Inputs:** Use 8px (`0.5rem`) for a more structured, reliable feel in forms.

## Components

### Cards
Cards are the heart of the "Kiez-Teppich." Each card must have a 16px internal padding and a 16px corner radius. Headers within cards should use `headline-md` and include a small icon in the primary or secondary color to aid quick scanning.

### Buttons & Chips
Primary buttons use the Stitch Blue background with white text. Secondary "community" buttons use the Terracotta tint. Chips are used for filtering categories (e.g., "Events," "Lost & Found") and should use low-opacity versions of the primary colors with high-contrast text.

### Toggles & Switches
Switches follow a clean, modern aesthetic: a pill-shaped track in a neutral grey when off, and Stitch Blue when on. The "thumb" should be a pure white circle with a subtle shadow.

### Sidebar
The sidebar is a sleek, vertical panel. Active states for navigation items are indicated by a vertical 4px bar on the left edge and a subtle background tint (`primary-color` at 8% opacity).

### Neighborhood "Stitch"
A unique decorative element: use a dotted or dashed border-top (2px width) on section dividers to subtly reference the "Stitch" brand narrative, using the neutral-300 color.