---
source: PREING1-S1/Informatique1/Styles Globaux (Tailwind v4).docx
transcription: manuelle
format_source: docx
verification: lecture intégrale du texte et des tableaux Word
---

# Styles globaux — Tailwind v4

## Code CSS

```css
@import "tailwindcss";

@theme {
  --color-primary: #4f46e5;
  --font-sans: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}

/* Styles globaux */
body {
  background-color: #f8fafc; /* slate-50 */
  color: #0f172a; /* slate-900 */
  font-family: var(--font-sans);
  margin: 0;
  -webkit-font-smoothing: antialiased;
}

/* Utilitaires Scrollbar */
.hide-scrollbar::-webkit-scrollbar {
  display: none;
}
.hide-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

/* Animations */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.fade-in {
  animation: fadeIn 0.4s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}
```
