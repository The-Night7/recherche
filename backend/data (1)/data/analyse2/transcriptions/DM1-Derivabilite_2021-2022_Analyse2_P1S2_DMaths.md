# Analyse 2 — Devoir Dérivabilité (DM1) 2021–2022, sujet et solution

> Source : `PREING1-S2/Analyse2/DM1-Derivabilite_2021-2022_Analyse2_P1S2_DMaths.pdf`, 5 pages (PDF natif LaTeX). En-tête : « Cycle Préparatoire - Première Année — Analyse II - 2021/2022 ».
> Transcription du 13 octobre 2026 : lecture visuelle intégrale ; formules restituées en LaTeX. La notation de la source ($(\arcsin x)\prime$, $\cos x(\arcsin x)$ pour $\cos(\arcsin x)$, alternance argch/arcosh/arcch) est conservée.
> Erreurs de la source, signalées et non corrigées dans le texte :
> - **Ex. 1.2** : « On restreint la fonction sin » → cos ; $-\sin<0$ sur $]0;\pi[$ donne une fonction strictement **décroissante**, et non croissante.
> - **Ex. 1.3** : les intervalles $]-\frac\pi2;\frac\pi2]$ doivent être ouverts : $]-\frac\pi2;\frac\pi2[$.
> - **Énoncé ex. 2** : 4(b) « dérivabilité de arcsh sur $E$ » → argch ; 5(b) argsh est définie de $\mathbb R$ dans $\mathbb R$, et non dans $\mathbb R^+$.
> - **Solution 1** : $sh(-x)=-sh(x)$ montre que sh est **impaire**, et non paire.
> - **Solution 4(b)** : argch est dérivable sur $]1;+\infty[$, et non en $1$. Le dénominateur est $\sqrt{ch^2(\operatorname{argch}x)-1}$, et non $\sqrt{sh^2(\dots)-1}$.
> - **Solution 5(a)** : $ch(x)=\frac{e^{2x}+1}{2e^x}>0$ pour **tout** $x$, et non « $\Leftrightarrow x>0$ ».
> - **Solution 5(c)** (seconde méthode) : on résout $x=\sinh z$, et non $\cosh z$.
> - **Solution 6(b)** : la dérivée de th est **non nulle**, et non « nulle ».
> - **Solution 7(c)** : $h(x)=\frac12(\ln(1+x)-\ln(1-x))$, et non $\frac1x(\dots)$ ; « $h=arcth(0)$ » se lit $h=\operatorname{argth}$.

# Devoir Dérivabilité

## Exercice 1

On appelle $arcsin, arccos, arctan$ les fonctions réciproques des fonctions $sin, cos, tan$.
Déterminer les ensembles de départ et d’arrivée pour pouvoir définir ces fonctions réciproques et en tout réel pour lesquelles ces fonctions sont dérivables, exprimer la dérivée de la fonction réciproque sous une forme qui n’utilise pas sin ou cos.
*Indication : on obtiendra $arctan'(x)=\dfrac1{1+x^2}$*

### Solution

1. Fonction sin :
   Tout d’abord, la fonction sin prend ses valeurs dans $\mathbb R$, et ses images se situent dans l’intervalle $J=[-1;1]$.
   On restreint la fonction sin à l’ensemble de définition $I=[-\frac\pi2;\frac\pi2]$ et l’ensemble d’arrivée $J=[-1;1]$.
   La fonction sin est dérivable de dérivée cos. Donc la dérivée est strictement positive sur I (sauf en deux réels) donc la fonction est strictement croissante. Comme elle est continue, elle est bijective de I sur J.
   d’où $f:\begin{cases}\left[-\frac\pi2,\frac\pi2\right]\to[-1,1]\\ x\to\sin x\end{cases}$
   On a donc $f^{-1}:\begin{cases}[-1,1]\to\left[-\frac\pi2,\frac\pi2\right]\\ x\to\arcsin x\end{cases}$
   Cherchons à présent une écriture de la dérivée de arcsin :
   On utilise la leçon et on obtient $(\arcsin x)\prime=\dfrac1{\cos x(\arcsin x)}$
   On utilise la formule trigonométrique : $\cos^2x+\sin^2x=1$
   $\Longrightarrow\cos x^2(\arcsin x)=1-\sin^2(\arcsin x)$ et $\sqrt{\cos x^2(\arcsin x)}=\sqrt{1-\sin(\arcsin x)^2}$
   $\Longrightarrow\cos x(\arcsin x)=\sqrt{1-x^2}$
   d’où en revenant à l’expression : $(\arcsin x)\prime=\dfrac1{\cos x(\arcsin x)}=\dfrac1{\sqrt{1-x^2}}$
2. Fonction cos :
   Tout d’abord, la fonction cos prend ses valeurs dans $\mathbb R$, et ses images se situent dans l’intervalle $J=[-1;1]$.
   On restreint la fonction sin à l’ensemble de définition $I=[0;\pi]$ et l’ensemble d’arrivée $J=[-1;1]$.
   La fonction cos est dérivable de dérivée $-\sin$. Donc la dérivée est strictement négative sur I (sauf en deux réels) donc la fonction est strictement croissante. Comme elle est continue, elle est bijective de I sur J.
   d’où $f:\begin{cases}[0,\pi]\to[-1,1]\\ x\to\cos x\end{cases}$
   On a donc $f^{-1}:\begin{cases}[-1,1]\to[0,\pi]\\ x\to\arccos x\end{cases}$
   Cherchons à présent une écriture de la dérivée de arccos :
   On utilise la leçon et on obtient $(\arccos x)\prime=\dfrac1{\sin x(\arccos x)}$
   On utilise la formule trigonométrique : $\cos^2x+\sin^2x=1$
   $\Longrightarrow\sin x^2(\arccos x)=1-\cos^2(\arccos x)$ et $\sqrt{\sin x^2(\arccos x)}=\sqrt{1-\cos(\arccos x)^2}$
   $\Longrightarrow\sin x(\arccos x)=\sqrt{1-x^2}$
   d’où en revenant à l’expression : $(\arccos x)\prime=\dfrac1{-\sin x(\arccos x)}=-\dfrac1{\sqrt{1-x^2}}$
3. Étude de la fonction tan
   Tout d’abord rappelons que $\tan x=\dfrac{\sin x}{\cos x}$
   donc le domaine de définition de tan est $\mathbb R\setminus\{x/\cos x\neq0\}$
   $\cos x=0\Longrightarrow\begin{cases}x=\frac\pi2+[2k\pi],\ avec\ k\in\mathbb Z\\ x=-\frac\pi2+[2k\pi],\ avec\ k\in\mathbb Z\end{cases}$
   donc la fonction tan est définie sur $\mathbb R\setminus\left\{\frac\pi2+[k\pi]\ avec\ k\in\mathbb Z\right\}$
   On pose $f:\begin{cases}I=]-\frac\pi2;\frac\pi2]\to\mathbb R\\ x\to\tan x\end{cases}$,
   Cette fonction est dérivable sur I de dérivée : $f'(x)=1+\tan^2x>0$ donc elle est strictement croissante sur I.
   De plus $\displaystyle\lim_{x\to\frac\pi2^-}\tan x=+\infty$ et $\displaystyle\lim_{x\to-\frac\pi2^+}\tan x=-\infty$ (car quotient de sin et cos
   Comme $f$ est continue sur I, elle réalise une bijection de I sur $f(I)$
   On peut donc définir : $\arctan:\begin{cases}\mathbb R\to]-\frac\pi2;\frac\pi2]\\ x\to\arctan x\end{cases}$
   On peut utiliser la propriété du cours ou bien utiliser l’expression : $x=\tan(\arctan(x))$
   $x\prime=(\tan\arctan x)\prime\Longrightarrow1=(\arctan)\prime\left(1+\tan^2\arctan x\right)$
   $\Longrightarrow1=(\arctan)\prime\left(1+x^2\right)$
   $\Longrightarrow(\arctan x)\prime=\dfrac1{1+x^2}$

> Note : la condition « $\{x/\cos x\neq0\}$ » de la source désigne l’ensemble des points exclus ; il faut lire $\mathbb R\setminus\{x/\cos x=0\}$.

## Exercice 2

On définit deux fonctions $sh$ et $ch$ de $\mathbb R$ dans $\mathbb R$ par

$$shx=\frac{e^x-e^{-x}}2\quad\text{et}\quad chx=\frac{e^x+e^{-x}}2$$

1. Démontrer que $ch$ est paire et $sh$ est impaire.
2. Déterminer les dérivées de $ch$ et $sh$ et les exprimer en fonction de $ch$ et $sh$.
3. Démontrer que $ch^2x-sh^2x=1$
4. (a) Démontrer que $ch$ permet de définir une bijection de $\mathbb R^+$ dans un ensemble $E$ que l’on déterminera.
   (b) On appelle $argch$ la fonction réciproque de $ch$ définie de $E$ dans $\mathbb R^+$. Étudier la dérivabilité de $arcsh$ sur $E$. Et exprimer $argch'(x)$ en fonction de $x$ (sans utiliser $sh$ ou $ch$).
   (c) Soit $g:x\mapsto\ln(x+\sqrt{x^2-1})$. En utilisant la dérivation, montrer que $g=argcosh$.
5. (a) Démontrer que $sh$ permet de définir une bijection de $\mathbb R$ dans $\mathbb R$.
   (b) On appelle $argsh$ la fonction réciproque de $sh$ définie de $\mathbb R$ dans $\mathbb R^+$. Étudier la dérivabilité de $arcsh$ sur $\mathbb R$.
   (c) Soit $f:x\mapsto\ln(x+\sqrt{x^2+1})$. En utilisant la dérivation, montrer que $f=argsh$.
6. On appelle $th$ la fonction $th=\dfrac{sh}{ch}$. Étudier la fonction $th$, déterminer sa dérivée et son sens de variation.
7. (a) Démontrer que $th$ permet de définir une bijection de $\mathbb R^+$ dans un ensemble $F$ que l’on déterminera.
   (b) On appelle $argth$ la fonction réciproque de $th$ définie de $F$ dans $\mathbb R^+$. Étudier la dérivabilité de $argth$ sur $F$. Et exprimer $argth'(x)$ en fonction de $x$ (sans utiliser $sh$ ou $ch$ ou $th$).
   (c) Soit $h:x\mapsto\dfrac12\ln\dfrac{1+x}{1-x}$. En utilisant la dérivation, montrer que $h=argth(x)$.

### Solution

1. La fonction $ch$ est-elle paire ?
   $\forall x\in\mathbb R,\ ch(-x)=\dfrac{e^{-x}+e^{-(-x)}}2=\dfrac{e^{-x}+e^x}2=ch(x)$, donc la fonction ch est paire.
   $\forall x\in\mathbb R,\ sh(-x)=\dfrac{e^{-x}-e^{-(-x)}}2=\dfrac{e^{-x}-e^x}2=-sh(x)$, donc la fonction sh est paire.
2. Dérivée de $ch(x)$ : $ch\prime(x)=\left(\dfrac{e^x+e^{-x}}2\right)\prime=\dfrac{e^x-e^{-x}}2=sh(x)$
   Dérivée de $sh(x)$ : $sh\prime(x)=\left(\dfrac{e^x-e^{-x}}2\right)\prime=\dfrac{e^x-e^{-x}(-1)}2=\dfrac{e^x+e^{-x}}2=ch(x)$
3. On écrit :
   $$\begin{aligned}
   ch^2x-sh^2x&=\left(\frac{e^x+e^{-x}}2\right)^2-\left(\frac{e^x-e^{-x}}2\right)^2=\frac{(e^x+e^{-x})^2}4-\frac{(e^x-e^{-x})^2}4\\
   &=\frac{e^{2x}+2e^xe^{-x}+e^{-2x}-(e^{2x}-2e^xe^{-x}+e^{-2x})}4\\
   &=\frac{e^{2x}+2+e^{-2x}-(e^{2x}-2+e^{-2x})}4\\
   &=\frac{e^{2x}+2+e^{-2x}-e^{2x}+2-e^{-2x}}4=\frac44=1
   \end{aligned}$$
   Donc $ch^2x-sh^2x=1$.
4. (a) Soit $ch:x\to\dfrac{e^x+e^{-x}}2$
   $ch$ est continue sur $\mathbb R$ et dérivable sur $\mathbb R$ de dérivée $ch'(x)=sh(x)=\dfrac{e^{2x}-1}{2e^x}>0\Leftrightarrow x>0$
   Donc $ch$ est strictement croissante sur $\mathbb R^+$, comme $ch(0)=\dfrac{e^0+e^0}2=\dfrac{1+1}2=1$ et $\displaystyle\lim_{x\to+\infty}ch(x)=+\infty$ on peut appliquer le théorème de la bijection à cette fonction continue et $ch$ réalise une bijection de $\mathbb R^+$ dans $[1;+\infty[$
   (b) On observe que $sh$ ne s’annule pas sur $]0;+\infty[$ donc $argch$ est dérivable sur $[1;+\infty[$, de dérivée :
   $$arccosh'(x)=\frac1{sharccosh(x)}=\frac1{\sqrt{sh^2arccosh(x)-1}}=\frac1{\sqrt{x^2-1}}$$
   (c) On a
   $$\begin{aligned}
   g\prime(x)&=\frac{1+\frac{2x}{2\sqrt{x^2-1}}}{x+\sqrt{x^2-1}}=1+\frac{2x}{2\sqrt{x^2-1}}\,\frac1{x+\sqrt{x^2-1}}\\
   &=\frac{2\sqrt{x^2-1}+2x}{2\sqrt{x^2-1}}\,\frac1{x+\sqrt{x^2-1}}=\frac{2\left(\sqrt{x^2-1}+x\right)}{2\sqrt{x^2-1}}\,\frac1{x+\sqrt{x^2-1}}=\frac1{\sqrt{x^2-1}}
   \end{aligned}$$
   On observe que $g'(x)=arcosh'(x)$ or $g(1)=0$ et $argcosh(1)=0$ donc $g=arcosh$
   On peut aussi remarquer que $cosh(x)=\dfrac{e^x+e^{-x}}2$
   On résout $x=\cosh z\Leftrightarrow2x=y+\dfrac1y$ et $y=e^z\Leftrightarrow y^2-2xy+1=0$ et $y=e^z$
   $\Delta'=x^2-1$ et $y_1=x+\sqrt{x^2-1}$ et $y_2=x-\sqrt{x^2-1}$
   Donc $z=\ln\left(x+\sqrt{x^2-1}\right)$ ou $z=\ln\left(x-\sqrt{x^2-1}\right)$
   Or $x-\sqrt{x^2-1}=\dfrac1{x+\sqrt{x^2-1}}$ et pour $x\geqslant1$, $x+\sqrt{x^2-1}\geqslant1$ donc $x-\sqrt{x^2-1}<1$
   donc la $arccoshx=\ln\left(x+\sqrt{x^2-1}\right)$

   > Dans la première ligne de $g'$, le « $=1+\dots$ » de la source est une coquille pour « $=\left(1+\dots\right)\times\dots$ » ; la ligne suivante est juste.
5. (a) Soit $sh:x\to\dfrac{e^x-e^{-x}}2$
   $sh$ est continue sur $\mathbb R$ et dérivable sur $\mathbb R$ de dérivée $sh'(x)=ch(x)=\dfrac{e^x+e^{-x}}{2e^x}>0\Leftrightarrow x>0$
   Donc $sh$ est strictement croissante sur $\mathbb R$.
   $\displaystyle\lim_{x\to-\infty}sh(x)=-\infty$ et $\displaystyle\lim_{x\to+\infty}sh(x)=+\infty$ on peut appliquer le théorème de la bijection à cette fonction continue et $sh$ réalise une bijection de $\mathbb R$ dans $\mathbb R$
   (b) On observe que $ch$ ne s’annule pas sur $\mathbb R$ donc $argsh$ est dérivable sur $\mathbb R$, de dérivée :
   $$arcsinh'(x)=\frac1{ch\ arcsh(x)}=\frac1{\sqrt{sh^2arcsh(x)+1}}=\frac1{\sqrt{x^2+1}}$$
   (c) On a
   $$\begin{aligned}
   f\prime(x)&=\frac{1+\frac{2x}{2\sqrt{x^2+1}}}{x+\sqrt{x^2+1}}=1+\frac{2x}{2\sqrt{x^2+1}}\,\frac1{x+\sqrt{x^2+1}}\\
   &=\frac{2\sqrt{x^2+1}+2x}{2\sqrt{x^2+1}}\,\frac1{x+\sqrt{x^2+1}}=\frac{2\left(\sqrt{x^2+1}+x\right)}{2\sqrt{x^2+1}}\,\frac1{x+\sqrt{x^2+1}}=\frac1{\sqrt{x^2+1}}
   \end{aligned}$$
   On observe que $f'(x)=arcsh'(x)$ or $f(0)=0$ et $sh(0)=0$ donc $f=arcsh$
   On peut aussi remarquer que $sh(x)=\dfrac{e^x-e^{-x}}2$
   On résout $x=\cosh z\Leftrightarrow2x=y-\dfrac1y$ et $y=e^z\Leftrightarrow y^2-2xy-1=0$ et $y=e^z$
   $\Delta'=x^2+1$ et $y_1=x+\sqrt{x^2+1}$ et $y_2=x-\sqrt{x^2+1}$
   Or $\sqrt{x^2+1}>|x|$ donc $x-\sqrt{x^2+1}<0$
   Donc $z=\ln\left(x+\sqrt{x^2+1}\right)$
   donc la $arcshx=\ln\left(x+\sqrt{x^2+1}\right)$
6. (a) La fonction $th$ est dérivable comme quotient de fonctions dérivables.
   on a $th'\,x=\dfrac{ch\,x\,ch\,x-shx\,shx}{ch^2x}=\dfrac1{ch^2x}>0$ donc la fonction $th$ est strictement croissante
   $$th\,x=\frac{\frac{e^x-e^{-x}}2}{\frac{e^x+e^{-x}}2}=\left(\frac{e^x-e^{-x}}2\right)\frac2{e^x+e^{-x}}=\frac{e^x-e^{-x}}{e^x+e^{-x}}\ \text{donc}$$
   $\displaystyle\lim_{x\to-\infty}thx=\lim_{x\to-\infty}\frac{e^{2x}-e^0}{e^{2x}+e^0}=-1$ et $\displaystyle\lim_{x\to+\infty}thx=\lim_{x\to+\infty}\frac{e^0-e^{2x}}{e^0+e^{2x}}=1$
   Comme $th$ est continue sur $\mathbb R$ et strictement croissante, elle réalise une bijection de $\mathbb R$ dans $]-1;1[$
   (b) La fonction $th$ étant bijective et de dérivée nulle, $argth'(x)=\dfrac1{1-th^2(arcth(x))}=\dfrac1{1-x^2}$
   (c) $h(x)=\dfrac12(\ln(1+x)-\ln(1-x))$
   donc $h'(x)=\dfrac12\left(\dfrac1{1+x}+\dfrac1{1-x}\right)=\dfrac1{1-x^2}$
   On obtient la même dérivée que $argth$ or $h(0)=0$ et $arcth(0)=0$ donc $h=arcth(0)$
   $h(x)=\dfrac1x(\ln(1+x)-\ln(1-x))$
   Remarque : $y=th(x)\Leftrightarrow y=\dfrac{e^x-e^{-x}}{e^x+e^{-x}}\Leftrightarrow y=\dfrac{e^{2x}-1}{e^{2x}+1}\Leftrightarrow e^{2x}=\dfrac{1+y}{1-y}\Leftrightarrow x=\dfrac12\ln\dfrac{1+y}{1-y}$

   > Dans la limite en $+\infty$, la source écrit $\frac{e^0-e^{2x}}{e^0+e^{2x}}$, qui tend vers $-1$ ; il faut lire $\frac{1-e^{-2x}}{1+e^{-2x}}$, qui tend bien vers $1$.
