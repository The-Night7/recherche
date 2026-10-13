---
source: "PREING1-S2/Analyse2/Fiches-Derivee_2024-2025_Analyse2_P1S2_DMaths.pdf"
pages: 1
transcription: manuelle
transcription_date: 2026-09-30
verification: lecture visuelle intégrale du PDF et vérification des formules
---

# Formulaire de dérivation — Fonctions usuelles

Lycée Gustave Eiffel — PTSI 2 — Année 2011-2012 (indications de la couche texte). Le nom du fichier de classement indique 2024-2025.

$u,v,f,g$ désignent des fonctions dérivables ; $a,b,\alpha$ des réels ; $n\in\mathbb N$. Les expressions se lisent sur leurs domaines de définition et de dérivabilité ; les dénominateurs doivent être non nuls.

## Dérivées des fonctions usuelles

| Expression de $F$ | Expression de $F'$ |
| --- | --- |
| $a$ | $0$ |
| $ax+b$ | $a$ |
| $x^2$ | $2x$ |
| $\frac1x$ | $-\frac1{x^2}$ |
| $x^n$ | $nx^{n-1}$ |
| $x^\alpha$ | $\alpha x^{\alpha-1}$ |
| $\frac1{x^n}$ | $-\frac n{x^{n+1}}$ |
| $\frac1{x^\alpha}$ | $-\frac\alpha{x^{\alpha+1}}$ |
| $\sqrt x$ | $\frac1{2\sqrt x}$ |
| $\sqrt[n]x$ | $\frac1{n(\sqrt[n]x)^{n-1}}=\frac{\sqrt[n]x}{nx}$ |
| $\frac1{\sqrt x}$ | $-\frac1{2x\sqrt x}$ |
| $\frac1{\sqrt[n]x}$ | $-\frac1{nx\sqrt[n]x}$ |
| $\sin x$ | $\cos x$ |
| $\arcsin x$ | $\frac1{\sqrt{1-x^2}}$ |
| $\cos x$ | $-\sin x$ |
| $\arccos x$ | $-\frac1{\sqrt{1-x^2}}$ |
| $\tan x$ | $1+\tan^2x=\frac1{\cos^2x}$ |
| $\arctan x$ | $\frac1{1+x^2}$ |
| $\exp x$ | $\exp x$ |
| $\ln x$ | $\frac1x$ |
| $\operatorname{ch}x$ | $\operatorname{sh}x$ |
| $\operatorname{argch}x$ | $\frac1{\sqrt{x^2-1}}$ |
| $\operatorname{sh}x$ | $\operatorname{ch}x$ |
| $\operatorname{argsh}x$ | $\frac1{\sqrt{x^2+1}}$ |
| $\operatorname{th}x$ | $1-\operatorname{th}^2x=\frac1{\operatorname{ch}^2x}$ |
| $\operatorname{argth}x$ | $\frac1{1-t^2}$, tel qu’imprimé |

> **Coquille de variable :** le dernier dénominateur est imprimé $1-t^2$. Pour la fonction $\operatorname{argth}(x)$, la dérivée est $1/(1-x^2)$ sur $]-1,1[$. Les lignes comportant une racine $n$-ième supposent $n\ge1$.

## Opérations et fonctions composées

| Expression de $F$ | Expression de $F'$ |
| --- | --- |
| $au$ | $au'$ |
| $u+v$ | $u'+v'$ |
| $uv$ | $u'v+uv'$ |
| $\frac uv$ | $\frac{u'}v-\frac{uv'}{v^2}=\frac{u'v-uv'}{v^2}$ |
| $f\circ g$ | $g'\cdot(f'\circ g)$ |
| $u^n$ | $nu'u^{n-1}$ |
| $u^\alpha$ | $\alpha u'u^{\alpha-1}$ |
| $\frac1{u^n}$ | $-\frac{nu'}{u^{n+1}}$ |
| $\frac u{v^n}$ | $\frac{u'}{v^n}-\frac{nuv'}{v^{n+1}}=\frac{u'v-nuv'}{v^{n+1}}$ |
| $\frac u{v^\alpha}$ | $\frac{u'}{v^\alpha}-\frac{\alpha uv'}{v^{\alpha+1}}=\frac{u'v-\alpha uv'}{v^{\alpha+1}}$ |
| $u^2$ | $2u'u$ |
| $\frac1u$ | $-\frac{u'}{u^2}$ |
| $\sqrt u$ | $\frac{u'}{2\sqrt u}$ |
| $\frac1{\sqrt u}$ | $-\frac{u'}{2u\sqrt u}$ |
| $\sin u$ | $u'\cos u$ |
| $\arcsin u$ | $\frac{u'}{\sqrt{1-u^2}}$ |
| $\cos u$ | $-u'\sin u$ |
| $\arccos u$ | $-\frac{u'}{\sqrt{1-u^2}}$ |
| $\tan u$ | $u'(1+\tan^2u)$ |
| $\arctan u$ | $\frac{u'}{1+u^2}$ |
| $\exp u$ | $u'\exp u$ |
| $\ln u$ | $\frac{u'}u$ |
| $\operatorname{ch}u$ | $u'\operatorname{sh}u$ |
| $\operatorname{argch}u$ | $\frac{u'}{\sqrt{u^2-1}}$ |
| $\operatorname{sh}u$ | $u'\operatorname{ch}u$ |
| $\operatorname{argsh}u$ | $\frac{u'}{\sqrt{u^2+1}}$ |
| $\operatorname{th}u$ | $u'(1-\operatorname{th}^2u)$ |
| $\operatorname{argth}u$ | $\frac{u'}{1-u^2}$ |

## Théorème 1 — Dérivée de la réciproque

Soit $f:I\to J$ une fonction bijective et dérivable. Soient $x_0\in I$ et $y_0\in J$.

1. Si $f'(x_0)\ne0$, alors $f^{-1}$ est dérivable en $f(x_0)$ et

   $$(f^{-1})'(f(x_0))=\frac1{f'(x_0)}.$$

2. Si $f'(f^{-1}(y_0))\ne0$, alors $f^{-1}$ est dérivable en $y_0$ et

   $$(f^{-1})'(y_0)=\frac1{f'(f^{-1}(y_0))}.$$
