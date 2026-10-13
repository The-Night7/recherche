// appliqué avant l'affichage pour éviter un flash du mauvais thème
try { const t = localStorage.getItem("tuteur-theme"); if (t) document.documentElement.dataset.theme = t; } catch (e) {}
