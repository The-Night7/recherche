---
source: "PREING2-S1/Series/TD1-Correction_2022-2023_Series_P2S1_Inconnu.pdf"
pages: 70
transcription: manuelle, depuis les pages manuscrites
transcription_date: 2026-10-07
verification: lecture visuelle intégrale des 70 pages manuscrites ; calculs et annotations transcrits, corrections signalées
---

# Séries — TD1 : séries numériques — Corrigé manuscrit (2022–2023)

## Page 1

### TD1 — Séries numériques

#### Exercice 1

Soit $S_n=\sum_{k=1}^nu_k$ la suite des sommes partielles. La série de terme général $u_n$ converge si et seulement si $(S_n)$ converge. Ici $u_k=v_k-v_{k-1}$, donc
$$S_n=\sum_{k=1}^n(v_k-v_{k-1})=v_n-v_0.$$
Ainsi $(S_n)$ converge si et seulement si $(v_n)$ converge, et il en est de même pour la série $\sum u_n$.

#### Exercice 2

**1.** $u_n=1/(1+2+\cdots+n)$. Comme $\sum_{k=1}^nk=n(n+1)/2$,
$$u_n=\frac2{n(n+1)}=2\left(\frac1n-\frac1{n+1}\right).$$
Avec $v_n=1/n$, $S_n=-2(v_{n+1}-v_1)$. Comme $v_n\to0$, $(S_n)$ converge et $S_n\to2$.

## Page 2

**Exercice 2, question 1 (fin).** $\sum_{n\ge1}u_n$ converge et sa somme vaut $2$.

**2.** Décomposer
$$u_n=\frac1{n(n+1)(n+2)}=\frac1{2n}-\frac1{n+1}+\frac1{2(n+2)}$$
$$=-\frac12\left(\frac1{n+1}-\frac1n\right)+\frac12\left(\frac1{n+2}-\frac1{n+1}\right).$$
Alors
$$S_n=-\frac12\left(\frac1{n+1}-1\right)+\frac12\left(\frac1{n+2}-\frac12\right)\longrightarrow\frac12-\frac14=\frac14.$$
Les suites inverses tendent vers zéro ; la série converge et
$$\sum_{n=1}^{+\infty}\frac1{n(n+1)(n+2)}=\frac14.$$
**3.**
$$u_n=\ln\frac{(n+1)^2}{n(n+2)}=2\ln(n+1)-\ln n-\ln(n+2)$$
$$=[\ln(n+1)-\ln n]-[\ln(n+2)-\ln(n+1)].$$
La somme partielle est la différence des deux sommes télescopiques correspondantes.

## Page 3

**Exercice 2, question 3 (suite).**
$$S_n=\ln(n+1)-\ln1-[\ln(n+2)-\ln2]=\ln2+\ln\frac{n+1}{n+2}.$$
Le dernier logarithme tend vers $\ln1=0$. Donc la série converge et sa somme vaut **$\ln2$**.

**4.** Pour $u_n=1/[3+(-1)^n]^n$, les termes pairs et impairs donnent
$$\sum_{n\ge0}u_n=\sum_{p\ge0}\frac1{4^{2p}}+\sum_{p\ge0}\frac1{2^{2p+1}}=\sum_{p\ge0}\left(\frac1{16}\right)^p+\frac12\sum_{p\ge0}\left(\frac14\right)^p.$$
La première série est géométrique de raison $1/16$, de module inférieur à $1$ ; elle converge et a pour somme $1/(1-1/16)$.

**Précision de transcription :** les égalités de sommes infinies sont justifiées ici par la positivité et la convergence des deux sous-séries, établies sur cette page et la suivante. Avant cela, la séparation peut s’écrire sur les sommes partielles. Les indices du manuscrit ont été distingués en $n$ et $p$.

## Page 4

**Exercice 2, question 4 (fin).** La seconde série géométrique, de raison $1/4$, converge et a pour somme $1/(1-1/4)$. Ainsi
$$\sum_{n=0}^{+\infty}u_n=\frac1{1-1/16}+\frac12\frac1{1-1/4}=\frac{16}{15}+\frac23=\frac{26}{15}.$$
Le résultat intermédiaire $26/15$ reste lisible ; une écriture finale à sa droite est barrée en rouge.

#### Exercice 3

Soit $\sum u_n$ et $\sum v_n$ deux séries convergentes à termes positifs.

**a.** Poser $w_n=\sqrt{u_nv_n}$. De $(a-b)^2\ge0$, on tire $ab\le(a^2+b^2)/2$. Avec $a=\sqrt{u_n}$ et $b=\sqrt{v_n}$,
$$0\le w_n\le\frac12(u_n+v_n)=\frac12u_n+\frac12v_n.$$

## Page 5

**Exercice 3, a (fin).** Par linéarité, $\sum\frac12(u_n+v_n)$ converge. Le critère de comparaison des séries positives donne la convergence de $\sum w_n$.

**b.** Poser $t_n=\sqrt{u_n}/n=\sqrt{u_n/n^2}$. La série $\sum_{n\ge1}1/n^2$ est une série de Riemann convergente, d’exposant $2>1$. Prendre $v_n=1/n^2$ dans la question a : $t_n=\sqrt{u_nv_n}$, donc $\sum t_n$ converge.

La page porte ensuite le titre « Exercice 4 », sans développement sur cette feuille.

## Page 6

Page quadrillée laissée blanche dans le document source.

## Page 7

#### Exercice 3 — seconde rédaction annotée

On considère deux séries convergentes à termes positifs $\sum u_n$ et $\sum v_n$. Étudier $\sum w_n$, avec $w_n=\sqrt{u_nv_n}$.

Pour tous $a,b\in\mathbb R$,
$$0\le(a-b)^2=a^2+b^2-2ab\Rightarrow ab\le\frac12(a^2+b^2).$$
En prenant $a=\sqrt{u_n}$ et $b=\sqrt{v_n}$,
$$0\le w_n\le\frac12(u_n+v_n).$$
La somme de deux séries convergentes à termes positifs converge ; donc $\sum\frac12(u_n+v_n)$ converge. Le théorème de majoration donne la convergence de $\sum w_n$.

## Page 8

**Remarque.** La convergence de $\sum u_n$ et de $\sum v_n$ implique celle de $\sum(u_n+v_n)$ ; la réciproque est fausse dans le cas général. Exemple : $u_n=1/n$, $v_n=-1/n$. Leur somme est nulle, tandis que chacune des deux séries diverge. Cet exemple sort du cadre des deux suites positives de l’exercice.

**b.** Pour étudier $\sum_{n\ge1}\sqrt{u_n}/n$, appliquer a avec $\sqrt{v_n}=1/n$, soit $v_n=1/n^2$. Cette série de Riemann converge, et $\sum u_n$ converge par hypothèse ; donc $\sum\sqrt{u_nv_n}=\sum\sqrt{u_n}/n$ converge.

## Page 9

**Remarques sur les racines carrées.** Pour $n\ge1$, $t_n=\sqrt{u_n}/n\le\sqrt{u_n}$. Cette inégalité est vraie mais ne suffit pas à conclure à la convergence.

En général, $\sqrt x\le x$ pour $x\ge1$, tandis que $\sqrt x\ge x$ pour $0\le x\le1$. Si $\sum u_n$ est une série positive convergente, alors $u_n\to0$ ; à partir d’un rang, $0\le u_n\le1$. On ne peut donc pas majorer $\sqrt{u_n}$ par $u_n$ dans ce régime.

**La convergence de $\sum u_n$ n’entraîne pas celle de $\sum\sqrt{u_n}$.** Cette implication est barrée dans les annotations.

## Page 10

**Exemples.**

1. $u_n=1/n^2$ : $\sum u_n$ converge, mais $\sum\sqrt{u_n}=\sum1/n$ diverge.
2. $u_n=1/n^4$ : $\sum u_n$ et $\sum\sqrt{u_n}=\sum1/n^2$ convergent.

**Autre méthode pour les questions a et b.** Poser les sommes partielles $U_n=\sum_{k=0}^nu_k$ et $V_n=\sum_{k=0}^nv_k$. Elles convergent, puisque les séries convergent. L’inégalité de Cauchy–Schwarz donne
$$\sum_{k=0}^n\sqrt{u_kv_k}\le\sqrt{\sum_{k=0}^nu_k}\sqrt{\sum_{k=0}^nv_k}=\sqrt{U_n}\sqrt{V_n}.$$

## Page 11

**Autre méthode (suite).** Poser $S_n=\sum_{k=0}^nw_k$. Alors $0\le S_n\le\sqrt{U_n}\sqrt{V_n}$, et cette dernière suite tend vers $\sqrt{\ell_1}\sqrt{\ell_2}$, où $\ell_1=\lim U_n$ et $\ell_2=\lim V_n$. Les sommes partielles de la série positive sont donc majorées ; elles convergent et $\sum w_n$ converge.

**Précision de transcription :** la convergence découle de la croissance et de la majoration des sommes partielles, et non de la seule existence d’une majorante convergente.

#### Exercice 4

Soit une série à termes positifs $\sum u_n$.

**1.a.** Poser $v_n=u_n/(1+n^2u_n)$ et montrer que $\sum v_n$ converge. Si tous les $u_n$ sont nuls, tous les $v_n$ sont nuls : la conclusion est immédiate.

## Page 12

**Exercice 4, 1.a (suite).** Pour $u_n>0$ et $n\ge1$,
$$1+n^2u_n\ge n^2u_n\Rightarrow\frac1{1+n^2u_n}\le\frac1{n^2u_n}\Rightarrow0\le v_n\le\frac1{n^2}.$$
La même borne vaut si $u_n=0$, puisque $v_n=0$. La série de Riemann $\sum1/n^2$ converge ; par majoration, $\sum v_n$ converge. Le manuscrit traite les cas « tous nuls » et « tous non nuls » ; la remarque sur les termes nuls isolés complète l’argument sans changer la conclusion.

**1.b.** Poser $v_n=u_n/(1+u_n)$. Montrer $\sum v_n$ convergente si et seulement si $\sum u_n$ convergente.

Sens direct de la comparaison : supposons $\sum u_n$ convergente. Comme $u_n\ge0$, $1+u_n\ge1$.

## Page 13

**Exercice 4, 1.b (suite).** $1/(1+u_n)\le1$, donc
$$0\le v_n=\frac{u_n}{1+u_n}\le u_n.$$
La convergence de $\sum u_n$ implique celle de $\sum v_n$ par majoration.

Réciproquement, supposons $\sum v_n$ convergente. L’identité $v_n=u_n/(1+u_n)$ donne
$$u_n=v_n+v_nu_n,\qquad(1-v_n)u_n=v_n.$$
Comme $u_n\ge0$, on a $0\le v_n<1$ ; donc $u_n=v_n/(1-v_n)$. La série $\sum v_n$ convergeant, son terme général tend vers zéro.

## Page 14

**Exercice 4, 1.b (fin).** Il existe $N$ tel que $v_n\le1/2$ pour $n\ge N$. Alors $1-v_n\ge1/2$, d’où
$$\frac1{1-v_n}\le2,\qquad u_n=\frac{v_n}{1-v_n}\le2v_n.$$
La queue $\sum_{n\ge N}u_n$ converge par majoration. Ajouter la somme finie $\sum_{k=0}^{N-1}u_k$ ne change pas la convergence : $\sum u_n$ converge.

**2.** On considère trois séries convergentes à termes positifs $\sum u_n$, $\sum v_n$ et $\sum w_n$.

## Page 15

**Exercice 4, question 2.** Étudier la série de terme général
$$z_n=\sqrt{u_nv_n+u_nw_n+v_nw_n}.$$
On développe
$$(u_n+v_n+w_n)^2=u_n^2+v_n^2+w_n^2+2(u_nv_n+u_nw_n+v_nw_n).$$
Donc
$$0\le u_nv_n+u_nw_n+v_nw_n=\frac12(u_n+v_n+w_n)^2-\frac12(u_n^2+v_n^2+w_n^2)\le\frac12(u_n+v_n+w_n)^2.$$
Par croissance de la racine carrée,
$$0\le z_n\le\frac1{\sqrt2}(u_n+v_n+w_n).$$
La série majorante converge comme combinaison linéaire des trois séries convergentes.

## Page 16

**Exercice 4, question 2 (fin).** Le théorème de majoration des séries à termes positifs donne la convergence de $\sum z_n$. Le reste de la page est vide.

## Page 17

### TD1 — Exercice 5

**Méthode pour les séries numériques à termes positifs.** Commencer par la limite du terme général. Si $u_n\to\ell\ne0$, la série diverge grossièrement. Si $u_n\to0$, employer un critère adapté : équivalence, comparaison, séries de Riemann, Bertrand ou géométriques, télescopage, règle de d’Alembert, de Cauchy ou lemme de Riemann. Le schéma du manuscrit relie ces méthodes au cas de limite nulle.

**1.** $u_n=n^2/(n^2+1)\to1\ne0$. La série diverge grossièrement.

## Page 18

**Exercice 5, 2.**
$$u_n=\sqrt{n^2+n}-n=n\left(\sqrt{1+\frac1n}-1\right)=n\left[1+\frac1{2n}+o(1/n)-1\right]=\frac12+o(1).$$
La limite est $1/2\ne0$ : divergence grossière.

**3.** $u_n=1/\ln(n+1)\sim1/\ln n=v_n>0$. La série $\sum v_n$ est une série de Bertrand avec $\alpha=0<1$, $\beta=1$, donc divergente. Autre justification : $nv_n=n/\ln n\to+\infty$, et le lemme de Riemann avec exposant $1$ donne la divergence. Par équivalence de termes positifs, $\sum u_n$ diverge.

## Page 19

**Exercice 5, 4.** $u_n=\ln n/n^2$ est un terme de série de Bertrand avec $\alpha=2>1$ et $\beta=-1$. Pour le vérifier par comparaison, poser $\gamma=(\alpha+1)/2=3/2$. Alors
$$\frac{u_n}{n^{-3/2}}=\frac{\ln n}{\sqrt n}\to0,$$
donc $u_n=o(n^{-3/2})$. La série de Riemann d’exposant $3/2$ converge ; $\sum u_n$ converge.

**5.** $u_n=2^{-\sqrt n}=e^{-\sqrt n\ln2}$. Le quotient vaut
$$\frac{u_{n+1}}{u_n}=e^{(\sqrt n-\sqrt{n+1})\ln2}.$$

## Page 20

**Exercice 5, 5 (suite).** Comme $\sqrt n-\sqrt{n+1}=-1/(\sqrt n+\sqrt{n+1})$, le quotient tend vers $1$ : d’Alembert ne conclut pas. La racine $n$-ième vaut
$$\sqrt[n]{u_n}=2^{-1/\sqrt n}=e^{-\ln2/\sqrt n}\to1,$$
donc Cauchy ne conclut pas non plus. La comparaison $2^{-\sqrt n}\ge2^{-n}$ ne fournit pas de majorante convergente.

En revanche,
$$n^2u_n=e^{2\ln n-\sqrt n\ln2}=e^{\ln n(2-\sqrt n\ln2/\ln n)}\to0.$$
Le lemme de Riemann avec exposant $2>1$ donne la convergence de la série.

## Page 21

**Exercice 5, 6.**
$$u_n=\frac{n+\sqrt n}{2n^3-1}\sim\frac n{2n^3}=\frac1{2n^2}>0.$$
La série de Riemann d’exposant $2$ converge ; par équivalence, $\sum u_n$ converge.

**7.** $u_n=\sin^3(1/n)$. Pour $n\ge1$, $1/n\in]0,\pi/2]$, donc les termes sont positifs. Comme $\sin(1/n)=1/n+o(1/n)$,
$$u_n\sim\frac1{n^3}.$$
La série de Riemann d’exposant $3>1$ converge ; il en est de même pour $\sum u_n$.

## Page 22

**Exercice 5, 8.**
$$u_n=\frac{\ln(n^n)}{(\ln n)^n}=\frac{n\ln n}{e^{n\ln(\ln n)}}.$$
Alors
$$\sqrt[n]{u_n}=\frac{(n\ln n)^{1/n}}{\ln n}=\frac{e^{\ln(n\ln n)/n}}{\ln n}\to0<1.$$
Par Cauchy, la série converge.

**9.**
$$u_n=\left(\frac n{n+1}\right)^n=\left(1+\frac1n\right)^{-n}=e^{-n\ln(1+1/n)}=e^{-1+o(1)}\to e^{-1}\ne0.$$
La série diverge grossièrement.

## Page 23

**Exercice 5, 10.** $u_n=(n/(n+1))^{n^2}$. La racine $n$-ième vaut $(n/(n+1))^n\to e^{-1}<1$ (question 9). Par Cauchy, la série converge.

**11.**
$$u_n=\frac1{(2n-1)2^{2n-1}}=\frac{e^{-(2n-1)\ln2}}{2n-1}.$$
Ainsi $n^2u_n=\frac{n^2}{2n-1}e^{-(2n-1)\ln2}\to0$. Le lemme de Riemann avec exposant $2$ donne la convergence.

**12.**
$$u_n=\frac{(n+1)(n+2)\cdots(2n)}{(2n)^n}=\frac{(2n)!}{2^nn^nn!}.$$
Donc
$$\frac{u_{n+1}}{u_n}=\frac{(2n+2)!}{2^{n+1}(n+1)^{n+1}(n+1)!}\frac{2^nn^nn!}{(2n)!}.$$

## Page 24

**Exercice 5, 12 (fin).** En simplifiant,
$$\frac{u_{n+1}}{u_n}=\frac{2n+1}{n+1}\left(\frac n{n+1}\right)^n\to2e^{-1}<1.$$
Par d’Alembert, $\sum u_n$ converge.

**13.** $u_n=(n!)^2/(2n)!$. On a
$$u_{n+1}=\frac{((n+1)!)^2}{(2n+2)!}=\frac{(n+1)(n!)^2}{2(2n+1)(2n)!},$$
$$\frac{u_{n+1}}{u_n}=\frac{n+1}{2(2n+1)}\to\frac14<1.$$
La série converge par d’Alembert.

## Page 25

**Exercice 5, 14.** Pour $a>0$,
$$u_n=\frac{a^n}{(1+a)(1+a^2)\cdots(1+a^n)},\qquad\frac{u_{n+1}}{u_n}=\frac a{1+a^{n+1}}.$$

- Si $a=1$, le quotient vaut $1/2<1$ : convergence.
- Si $0<a<1$, $a^{n+1}\to0$ et le quotient tend vers $a<1$ : convergence.
- Si $a>1$, $a^{n+1}\to+\infty$ et le quotient tend vers $0<1$ : convergence.

Les trois cas utilisent la règle de d’Alembert.

## Page 26

**Exercice 5, 14 (conclusion).** Pour tout $a>0$, la série converge puisque la limite du quotient est inférieure à $1$.

**15.**
$$u_n=\frac{n^2}{2^n+n}=\frac{n^2}{e^{n\ln2}+n}\sim v_n=\frac{n^2}{2^n}>0.$$
Or $n^2v_n=n^4e^{-n\ln2}\to0$ : $\sum v_n$ converge par le lemme de Riemann d’exposant $2$. Par équivalence de termes positifs, $\sum u_n$ converge.

## Page 27

**Exercice 5, 16.**
$$u_n=n^{1/n}-(n+1)^{1/n}=n^{1/n}\left[1-\left(1+\frac1n\right)^{1/n}\right]$$
$$=n^{1/n}\left[1-e^{\frac1n\ln(1+1/n)}\right]=n^{1/n}\left[1-e^{1/n^2+o(n^{-2})}\right]$$
$$=n^{1/n}\left[-\frac1{n^2}+o(n^{-2})\right].$$
Comme $n^{1/n}=e^{\ln n/n}\to1$, on obtient **$u_n\sim-1/n^2$**. Les annotations rappellent $\ln n/n\to0$ ; une écriture intermédiaire positive est corrigée par le signe moins à la page suivante.

## Page 28

**Exercice 5, 16 (fin).** $u_n\sim-1/n^2<0$, ou $-u_n\sim1/n^2>0$. Le signe reste constant. La série de Riemann $\sum1/n^2$ converge, donc $\sum(-1/n^2)$ aussi. Le théorème d’équivalence pour les séries de signe constant donne la convergence de $\sum u_n$.

**17.** $u_n=\ln n/2^n$. Alors
$$n^2u_n=n^2\ln n\,e^{-n\ln2}.$$

## Page 29

**Exercice 5, 17 (fin).** $n^2u_n\to0$ par croissance comparée ; le lemme de Riemann d’exposant $2>1$ donne la convergence de la série.

**18.**
$$u_n=\frac{n\sqrt n}{2^n+\sqrt n}.$$
On a $2^n+\sqrt n\sim2^n$ car
$$\frac{2^n}{\sqrt n}=e^{n\ln2-\frac12\ln n}=e^{n(\ln2-\frac12\ln n/n)}\to+\infty.$$
Donc $u_n\sim v_n=n^{3/2}/2^n>0$.

## Page 30

**Exercice 5, 18 (fin).** $n^2v_n=n^{7/2}e^{-n\ln2}\to0$. Le lemme de Riemann donne la convergence de $\sum v_n$, puis l’équivalence celle de $\sum u_n$.

#### Exercice 7

Pour $u_n=\sqrt n+a\sqrt{n+1}+b\sqrt{n+2}$,
$$u_n=\sqrt n\left[1+a\sqrt{1+\frac1n}+b\sqrt{1+\frac2n}\right]$$
$$=\sqrt n\left[1+a\left(1+\frac1{2n}-\frac1{8n^2}+o(n^{-2})\right)+b\left(1+\frac1n-\frac1{2n^2}+o(n^{-2})\right)\right]$$
$$=\sqrt n\left[(1+a+b)+\left(\frac a2+b\right)\frac1n+\left(-\frac a8-\frac b2\right)\frac1{n^2}+o(n^{-2})\right].$$
Le manuscrit passe de l’exercice 5 à l’exercice 7 ; aucun exercice 6 n’est intercalé ici.

## Page 31

**Exercice 7 (suite). Premier cas : $1+a+b\ne0$.** Alors $u_n\sim(1+a+b)\sqrt n$, donc $u_n\to+\infty$ ou $-\infty$ selon le signe de $1+a+b$. Le terme général ne tend pas vers zéro : divergence grossière.

**Deuxième cas : $1+a+b=0$, soit $b=-1-a$.** Le développement devient
$$u_n=\left(-1-\frac a2\right)\frac1{\sqrt n}+\left(\frac12+\frac{3a}8\right)\frac1{n^{3/2}}+o(n^{-3/2}).$$
Si $-1-a/2\ne0$, alors $u_n\sim(-1-a/2)/\sqrt n$. La série de Riemann d’exposant $1/2$ diverge, donc cette série de signe constant diverge par équivalence.

## Page 32

**Exercice 7 (suite).** Pour supprimer le terme en $n^{-1/2}$, il faut $-1-a/2=0$, soit $a=-2$. Avec $b=-1-a$, on obtient $b=1$. Alors
$$u_n=\left(\frac12+\frac{3a}8\right)n^{-3/2}+o(n^{-3/2})=-\frac14n^{-3/2}+o(n^{-3/2}).$$
Donc $u_n\sim-1/(4n^{3/2})$, de signe constant négatif. La série de Riemann d’exposant $3/2$ converge ; par équivalence, $\sum u_n$ converge.

**Conclusion : la série converge si et seulement si $a=-2$ et $b=1$.**

## Page 33

**Exercice 7 — calcul de la somme.** Pour $u_n=\sqrt n-2\sqrt{n+1}+\sqrt{n+2}$,
$$u_n=-(\sqrt{n+1}-\sqrt n)+(\sqrt{n+2}-\sqrt{n+1}).$$
Ainsi
$$S_n=\sum_{k=0}^nu_k=-(\sqrt{n+1}-\sqrt0)+(\sqrt{n+2}-\sqrt1)$$
$$=\sqrt{n+2}-\sqrt{n+1}-1=\frac{(n+2)-(n+1)}{\sqrt{n+2}+\sqrt{n+1}}-1\longrightarrow-1.$$
D’où **$\sum_{n=0}^{+\infty}u_n=-1$**.

## Page 34

#### Exercice 6 (placé après l’exercice 7 dans le manuscrit)

Pour $p\in\mathbb N$, étudier
$$u_n=\frac{1!+2!+\cdots+n!}{(n+p)!}.$$
**1. Cas $p=0$.**
$$u_n=\frac{1!}{n!}+\frac{2!}{n!}+\cdots+\frac{(n-1)!}{n!}+1\ge1.$$
Le terme général ne peut donc pas tendre vers zéro : la série diverge grossièrement.

**Note de transcription :** le manuscrit écrit « $\lim u_n\ge1$ » puis « $\lim u_n\ne0$ ». La borne $u_n\ge1$ suffit à la conclusion, sans supposer préalablement l’existence de la limite.

## Page 35

**Exercice 6, cas $p=0$ (conclusion).** La série diverge grossièrement.

**2. Cas $p\ge3$.** $(n+p)!\ge(n+3)!$, donc
$$0\le u_n\le\frac{1!+\cdots+n!}{(n+3)!}.$$
Comme $k!\le n!$ pour $1\le k\le n$, on a $\sum_{k=1}^nk!\le nn!$. Ainsi
$$0\le u_n\le\frac{nn!}{(n+3)!}=\frac n{(n+3)(n+2)(n+1)}=:v_n,$$
et $v_n\sim1/n^2>0$.

## Page 36

**Exercice 6, cas $p\ge3$ (fin).** La série de Riemann $\sum1/n^2$ converge. Par équivalence, $\sum v_n$ converge ; par majoration, $\sum u_n$ converge.

**3. Cas $p=1$.**
$$u_n=\frac{1!+2!+\cdots+n!}{(n+1)!}\ge\frac{n!}{(n+1)!}=\frac1{n+1}=:v_n\ge0.$$
Comme $v_n\sim1/n$, on compare à la série harmonique.

## Page 37

**Exercice 6, cas $p=1$ (fin).** La série harmonique diverge. Par équivalence, $\sum v_n$ diverge, puis par minoration $\sum u_n$ diverge.

**Cas $p=2$.** Séparer le dernier terme :
$$u_n=\frac{1!+\cdots+(n-1)!}{(n+2)!}+\frac{n!}{(n+2)!}=v_n+w_n,$$
avec $w_n=1/[(n+2)(n+1)]\sim1/n^2$.

## Page 38

**Exercice 6, cas $p=2$ (suite).** Pour $1\le k\le n-1$, $k!\le(n-1)!$. D’où
$$\sum_{k=1}^{n-1}k!\le(n-1)(n-1)!,$$
$$0\le v_n\le\frac{(n-1)(n-1)!}{(n+2)!}=\frac{n-1}{(n+2)(n+1)n}=:t_n\sim\frac1{n^2}.$$
On a donc $u_n=v_n+w_n$, avec $w_n\sim1/n^2$ et $0\le v_n\le t_n\sim1/n^2$. La série $\sum w_n$ converge par équivalence avec une série de Riemann.

## Page 39

**Exercice 6, cas $p=2$ (fin).** La série $\sum t_n$ converge par équivalence avec $\sum1/n^2$, puis $\sum v_n$ converge par majoration. Comme $u_n=v_n+w_n$ et les deux séries convergent, $\sum u_n$ converge.

**Rappel annoté.** Somme de deux séries convergentes : convergence. Somme d’une convergente et d’une divergente : divergence. Somme de deux divergentes : on ne peut pas conclure en général.

## Page 40

#### Exercice 9

**1.** $u_n=\sin(n\alpha)/n^2$, $\alpha\in\mathbb R$. On a $0\le|u_n|\le1/n^2$. La série de Riemann d’exposant $2$ converge : par majoration, $\sum|u_n|$ converge. La série converge donc absolument, et par conséquent converge.

**2.** $u_n=(-2)^n/(1+3^n)$. Alors
$$|u_n|=\frac{2^n}{1+3^n}\sim\left(\frac23\right)^n>0.$$
La série géométrique de raison $2/3$ converge. Par équivalence, $\sum|u_n|$ converge.

## Page 41

**Exercice 9, 2 (fin).** La convergence absolue entraîne la convergence de $\sum u_n$.

**3.** $u_n=(-1)^n/(n^2+\ln n)$. Pour $n\ge1$,
$$|u_n|=\frac1{n^2+\ln n}\sim\frac1{n^2}>0.$$
La série de Riemann d’exposant $2$ converge ; par équivalence, $\sum|u_n|$ converge, donc $\sum u_n$ converge absolument.

**4.** $u_n=\sin n/(1+\cos n+e^n)$. Comme $|\sin n|\le1$ et $1+\cos n\ge0$,
$$|u_n|\le\frac1{e^n}=\left(\frac1e\right)^n.$$
La majorante est le terme d’une série géométrique convergente.

## Page 42

**Exercice 9, 4 (fin).** La raison $1/e$ a un module inférieur à $1$. Par majoration, $\sum|u_n|$ converge ; donc $\sum u_n$ converge absolument, puis converge.

**5.** $u_n=(-1)^n/(n-\ln n)$. On écrit $u_n=(-1)^nv_n$, avec $v_n=|u_n|=1/(n-\ln n)\ge0$ pour $n\ge2$. La série est alternée. De plus,
$$\lim_{n\to+\infty}|u_n|=\lim_{n\to+\infty}\frac1{n-\ln n}=0.$$
Il reste à établir que $(|u_n|)$ est décroissante.

## Page 43

**Exercice 9, 5 (fin).** Pour étudier la monotonie d’une suite, le manuscrit rappelle trois méthodes : différence $v_{n+1}-v_n$, quotient $v_{n+1}/v_n$ si les termes sont positifs, ou fonction associée $v_n=f(n)$.

Ici, poser $f(x)=1/(x-\ln x)$ sur $[2,+\infty[$. Alors
$$f'(x)=-\frac{1-1/x}{(x-\ln x)^2}\le0.$$
La fonction est décroissante, donc la suite $(|u_n|)$ l’est. La série est alternée, ses valeurs absolues décroissent vers zéro : elle converge par le théorème spécial des séries alternées.

**Note de transcription :** dans la ligne reliant la fonction à la suite, $f(n)$ est $|u_n|$, et non le terme signé $u_n$.

## Page 44

**Exercice 9, 6.** $u_n=\arctan(n\alpha)\sin(1/n^3)$, avec $\alpha\in\mathbb R$.

**Premier cas : $\alpha=0$.** Le manuscrit commence ce cas puis rappelle graphiquement tangente et arctangente.

Le premier graphique représente la tangente croissante sur $]-\pi/2,\pi/2[$, passant par l’origine et tendant vers les infinis aux bornes. Le second représente l’arctangente croissante, passant par $(0,0)$, avec asymptotes horizontales $\pm\pi/2$ :
$$\arctan0=0,\quad\lim_{x\to+\infty}\arctan x=\frac\pi2,\quad\lim_{x\to-\infty}\arctan x=-\frac\pi2,\quad\arctan x\sim_{x\to0}x.$$

## Page 45

**Exercice 9, 6 (suite).**

- Si $\alpha=0$, tous les $u_n$ sont nuls : la série converge.
- Si $\alpha\ne0$, $\arctan(n\alpha)$ a le signe de $\alpha$ ; pour $n\ge1$, $1/n^3\in]0,\pi/2]$ et son sinus est positif. Ainsi
$$|u_n|=|\arctan(n\alpha)\sin(1/n^3)|\sim\frac\pi2\frac1{n^3}.$$
La série de Riemann d’exposant $3$ converge. Par équivalence, $\sum|u_n|$ converge, donc $\sum u_n$ converge absolument, puis converge.

## Page 46

**Exercice 9, 7.** $u_n=[1+(-1)^n]/n^2$ pour $n\ge1$.

Première observation : $u_{2k}=2/(2k)^2=1/(2k^2)$ et $u_{2k+1}=0$. Deuxième méthode :
$$0\le|u_n|\le\frac2{n^2}.$$
La série majorante converge (Riemann, exposant $2$). Donc la série converge absolument et converge.

**8.**
$$u_n=(-1)^n(\sqrt{n^2+1}-1)=\frac{(-1)^nn^2}{\sqrt{n^2+1}+1}.$$
Son module est équivalent à $n$, donc ne tend pas vers zéro. La série diverge grossièrement.

**Note de transcription :** la formule « $\lim u_n\ne0$ » du manuscrit se comprend comme « $u_n$ ne tend pas vers zéro » ; le terme signé n’a pas de limite.

## Page 47

#### Exercice 10 — $\alpha>0$, $\alpha\ne1$

**1.** Poser $f_\alpha(x)=1/x^\alpha$. Sa dérivée est
$$f_\alpha'(x)=-\frac\alpha{x^{\alpha+1}}\le0,$$
donc la fonction est décroissante. Pour $n\ge2$ et $x\in[n-1,n]$,
$$f_\alpha(n)\le f_\alpha(x)\le f_\alpha(n-1).$$
Intégrer sur cet intervalle, de longueur $1$ :
$$\frac1{n^\alpha}\le\int_{n-1}^n\frac{dx}{x^\alpha}\le\frac1{(n-1)^\alpha}.\tag{1}$$
Pour encadrer les sommes partielles, on commence par encadrer un terme, puis on somme les inégalités.

**Précision de transcription :** le domaine de la fonction est annoncé $[2,+\infty[$, mais l’intégration pour $n=2$ nécessite aussi $[1,2]$. La même formule et la même décroissance sont valables sur $[1,+\infty[$.

## Page 48

**Exercice 10, 1 (suite).** Pour $x\in[n,n+1]$,
$$f_\alpha(n+1)\le f_\alpha(x)\le f_\alpha(n),$$
donc
$$\int_n^{n+1}\frac{dx}{x^\alpha}\le\frac1{n^\alpha}.\tag{2}$$
Réunir (1) et (2) :
$$\int_n^{n+1}\frac{dx}{x^\alpha}\le\frac1{n^\alpha}\le\int_{n-1}^n\frac{dx}{x^\alpha}.$$
Sommer pour $n=2,\ldots,N$ :
$$\sum_{n=2}^N\int_n^{n+1}\frac{dx}{x^\alpha}\le\sum_{n=2}^N\frac1{n^\alpha}\le\sum_{n=2}^N\int_{n-1}^n\frac{dx}{x^\alpha}.$$

## Page 49

**Exercice 10, 1 (fin).** Avec $S_N=\sum_{n=1}^N1/n^\alpha$,
$$\int_2^{N+1}\frac{dx}{x^\alpha}\le S_N-1\le\int_1^N\frac{dx}{x^\alpha}.$$
Pour $\alpha\ne1$, une primitive est $x^{1-\alpha}/(1-\alpha)$. Ainsi
$$t_N:=\frac{(N+1)^{1-\alpha}-2^{1-\alpha}}{1-\alpha}+1\le S_N\le\frac{N^{1-\alpha}-1}{1-\alpha}+1=:w_N.$$
**2. Cas $0<\alpha<1$.** Poser $v_N=N^{1-\alpha}/(1-\alpha)$. Montrer $t_N\sim v_N$ :
$$\frac{t_N}{v_N}=\left(\frac N{N+1}\right)^{\alpha-1}-\frac{N^{\alpha-1}}{2^{\alpha-1}}+(1-\alpha)N^{\alpha-1}\to1.$$
En effet $N^{\alpha-1}\to0$. Le facteur $1-\alpha$ absent dans le dernier terme du quotient manuscrit est rétabli ; il ne change pas la limite.

## Page 50

**Exercice 10, cas $0<\alpha<1$ (suite).**
$$w_N=\frac{N^{1-\alpha}}{1-\alpha}-\frac1{1-\alpha}+1,$$
$$\frac{w_N}{v_N}=1-N^{\alpha-1}+(1-\alpha)N^{\alpha-1}\to1.$$
Avec $t_N\le S_N\le w_N$ et $v_N>0$,
$$\frac{t_N}{v_N}\le\frac{S_N}{v_N}\le\frac{w_N}{v_N}.$$
Les deux bornes tendent vers $1$, donc $S_N/v_N\to1$ et
$$\sum_{n=1}^N\frac1{n^\alpha}\sim\frac1{1-\alpha}N^{1-\alpha}.$$

## Page 51

**Exercice 10, remarque.** Pour $0<\alpha<1$, cet équivalent tend vers $+\infty$, donc les sommes partielles divergent et la série $\sum1/n^\alpha$ diverge.

**3.a. Cas $\alpha>1$.** Les termes $N^{1-\alpha}$ et $(N+1)^{1-\alpha}$ tendent vers zéro. Le majorant des sommes partielles est borné ; la positivité garantit leur convergence. En passant à la limite dans l’encadrement,
$$1+\frac1{(\alpha-1)2^{\alpha-1}}\le\sum_{n=1}^{+\infty}\frac1{n^\alpha}\le1+\frac1{\alpha-1}.$$
Le manuscrit passe directement à la limite ; la convergence résulte de la croissance et de la majoration des sommes partielles.

## Page 52

**Exercice 10, exemples.**

- Pour $\alpha=2$ : $3/2\le\sum_{n=1}^{+\infty}1/n^2\le2$.
- Pour $\alpha=3$ : $9/8\le\sum_{n=1}^{+\infty}1/n^3\le3/2$.

**3.b. Équivalent du reste.** Poser
$$R_N=S-S_N=\sum_{n=N+1}^{+\infty}\frac1{n^\alpha},\qquad R_{N,m}=\sum_{n=N+1}^m\frac1{n^\alpha}.$$
L’encadrement d’un terme donne, après sommation de $N+1$ à $m$,
$$\sum_{n=N+1}^m\int_n^{n+1}\frac{dx}{x^\alpha}\le R_{N,m}\le\sum_{n=N+1}^m\int_{n-1}^n\frac{dx}{x^\alpha}.$$

## Page 53

**Exercice 10, 3.b (suite).**
$$\int_{N+1}^{m+1}\frac{dx}{x^\alpha}\le R_{N,m}\le\int_N^m\frac{dx}{x^\alpha}.$$
Calculer les primitives :
$$\frac{(m+1)^{1-\alpha}-(N+1)^{1-\alpha}}{1-\alpha}\le R_{N,m}\le\frac{m^{1-\alpha}-N^{1-\alpha}}{1-\alpha}.$$
Puisque $\alpha>1$, les puissances en $m$ tendent vers zéro. En faisant $m\to+\infty$,
$$\frac1{(\alpha-1)(N+1)^{\alpha-1}}\le R_N\le\frac1{(\alpha-1)N^{\alpha-1}}.$$
Poser $x_N=1/[(\alpha-1)N^{\alpha-1}]$ et diviser par cette quantité positive.

## Page 54

**Exercice 10, 3.b (fin).**
$$\frac{N^{\alpha-1}}{(N+1)^{\alpha-1}}\le\frac{R_N}{x_N}\le1.$$
Les bornes tendent vers $1$ ; donc $R_N/x_N\to1$. Finalement,
$$R_N=\sum_{n=N+1}^{+\infty}\frac1{n^\alpha}\sim\frac1{\alpha-1}\frac1{N^{\alpha-1}}\qquad(\alpha>1).$$

## Page 55

#### Exercice 11

**1.** Poser $f:[2,+\infty[\to\mathbb R$, $f(x)=1/(x\ln x)$. Alors
$$f'(x)=-\frac{\ln x+1}{(x\ln x)^2}<0,$$
donc $f$ est décroissante. Pour $n\ge2$ et $x\in[n,n+1]$, $f(x)\le f(n)$. En intégrant,
$$\int_n^{n+1}\frac{dx}{x\ln x}\le\frac1{n\ln n}.$$

## Page 56

**Exercice 11, 1 (suite).** Sommer pour $n=2,\ldots,N$ :
$$\int_2^{N+1}\frac{dx}{x\ln x}\le S_N:=\sum_{n=2}^N\frac1{n\ln n}.$$
Poser $t=\ln x$, $dt=dx/x$. Les bornes deviennent $\ln2$ et $\ln(N+1)$, donc
$$\int_2^{N+1}\frac{dx}{x\ln x}=\int_{\ln2}^{\ln(N+1)}\frac{dt}t=\ln(\ln(N+1))-\ln(\ln2).$$
Ainsi $S_N$ est minorée par une expression tendant vers $+\infty$.

## Page 57

**Exercice 11, 1 (fin).** $S_N\to+\infty$, donc $\sum_{n\ge2}1/(n\ln n)$ diverge.

**2.**
$$\ln(\ln(n+1))-\ln(\ln n)=\ln\left(\frac{\ln(n+1)}{\ln n}\right)$$
$$=\ln\left(\frac{\ln n+\ln(1+1/n)}{\ln n}\right)=\ln\left[1+\frac1{\ln n}\ln\left(1+\frac1n\right)\right].$$
Utiliser $\ln(1+1/n)=1/n+o(1/n)$.

## Page 58

**Exercice 11, 2 (fin).** L’expression devient
$$\ln\left[1+\frac1{n\ln n}+o\left(\frac1{n\ln n}\right)\right]\sim\frac1{n\ln n},$$
puisque $1/(n\ln n)\to0$ et $\ln(1+X)\sim X$ en zéro.

**3.** Chercher un équivalent de $\sum_{k=2}^n1/(k\ln k)$ à l’aide de la question 2.

**Proposition rappelée.** Si $u_n\sim v_n>0$ et si les séries divergent, alors leurs sommes partielles sont équivalentes :
$$\sum_{k=0}^nu_k\sim\sum_{k=0}^nv_k.$$

## Page 59

**Exercice 11, 3 (fin).** Poser $u_n=\ln(\ln(n+1))-\ln(\ln n)$ et $v_n=1/(n\ln n)$. Comme $u_n\sim v_n>0$ et $\sum v_n$ diverge,
$$\sum_{k=2}^n[\ln(\ln(k+1))-\ln(\ln k)]\sim\sum_{k=2}^n\frac1{k\ln k}.$$
Par télescopage,
$$\ln(\ln(n+1))-\ln(\ln2)\sim\sum_{k=2}^n\frac1{k\ln k}.$$

#### Exercice 12

**1.** Pour $n\ge1$, $u_n=\ln[1+(-1)^{n+1}/\sqrt n]$. Les termes ne gardent pas un signe constant. Poser $X=(-1)^{n+1}/\sqrt n\to0$. Avec $\ln(1+X)=X-X^2/2+X^3/3+o(X^3)$,
$$u_n=\frac{(-1)^{n+1}}{\sqrt n}-\frac1{2n}+\frac{(-1)^{n+1}}{3n^{3/2}}+o(n^{-3/2})=:a_n+b_n+c_n+d_n.$$
Ces quatre termes sont identifiés par des accolades dans le manuscrit.

## Page 60

**Exercice 12, 1 (suite).** Étudier séparément les quatre séries.

- $a_n=-(-1)^n/\sqrt n$ : la série alternée converge, car $1/\sqrt n$ décroît vers zéro.
- $b_n=-1/(2n)$ : la série diverge, comme multiple non nul de la série harmonique.
- $c_n=(-1)^{n+1}/(3n^{3/2})$ : la série converge absolument, par comparaison à la série de Riemann d’exposant $3/2$.
- $d_n=o(n^{-3/2})$ : sa valeur absolue est majorée à partir d’un rang par $1/n^{3/2}$, donc sa série converge absolument.

La dernière comparaison est indiquée par les flèches reliant les termes aux conclusions de convergence.

## Page 61

**Exercice 12, 1 (conclusion).** La série $\sum u_n$ diverge : elle est la somme d’une série divergente $\sum b_n$ et de trois séries convergentes.

Pourtant $u_n\sim(-1)^{n+1}/\sqrt n=a_n$, et $\sum a_n$ converge. On ne peut pas appliquer le théorème d’équivalence des séries de signe constant, car les termes changent de signe.

**2.a.** Étudier $u_n=\exp[(-1)^{n+1}/\sqrt n]-1$. Poser à nouveau $X=(-1)^{n+1}/\sqrt n\to0$ et utiliser le développement limité de l’exponentielle à l’ordre 3.

## Page 62

**Exercice 12, 2.a (suite).** Comme $e^X=1+X+X^2/2+X^3/6+o(X^3)$,
$$u_n=\frac{(-1)^{n+1}}{\sqrt n}+\frac1{2n}+\frac{(-1)^{n+1}}{6n^{3/2}}+o(n^{-3/2}).$$
La première série converge par alternance ; la série harmonique $\sum1/(2n)$ diverge ; les deux dernières séries convergent absolument. Donc $\sum u_n$ diverge.

**2.b.** $u_n=\sin[(-1)^{n+1}/\sqrt n]-1$. Le terme général tend vers **$-1$**, donc la série diverge grossièrement.

**Note de transcription :** l’annotation de limite à droite de cette dernière ligne est peu nette ; la limite de l’expression écrite est $-1$, et la conclusion de divergence est bien celle du manuscrit.

## Page 63

**Exercice 12, 2.c.**
$$u_n=\sin\left(\frac{(-1)^{n+1}}{\sqrt n}\right)=\frac{(-1)^{n+1}}{\sqrt n}-\frac16\left(\frac{(-1)^{n+1}}{\sqrt n}\right)^3+o(n^{-3/2})$$
$$=\frac{(-1)^{n+1}}{\sqrt n}+\frac{(-1)^n}{6n^{3/2}}+o(n^{-3/2}).$$
La première série converge par alternance, et les deux autres absolument. Donc la série converge.

**2.d.**
$$u_n=\exp\left(\frac{(-1)^{n+1}}{\sqrt n}\right)-\frac{2n+1}{2n}.$$
Le développement de l’exponentielle donne
$$u_n=1+\frac{(-1)^{n+1}}{\sqrt n}+\frac1{2n}+\frac{(-1)^{n+1}}{6n^{3/2}}+o(n^{-3/2})-1-\frac1{2n}.$$
Les termes constants et ceux en $1/(2n)$ sont barrés dans le manuscrit.

## Page 64

**Exercice 12, 2.d (fin).** Il reste la somme des termes alternés en $1/\sqrt n$, de termes absolument sommables en $1/n^{3/2}$ et d’un $o(n^{-3/2})$. Les trois séries convergent, donc $\sum u_n$ converge.

**2.e.**
$$u_n=\frac{1+(-1)^{n+1}\sqrt n}{1+n}=\frac{1/n+(-1)^{n+1}/\sqrt n}{1+1/n}.$$
Le manuscrit développe le facteur $(1+1/n)^{-1}$ et obtient
$$u_n=\frac1n-\frac1{n^2}+\frac{(-1)^{n+1}}{\sqrt n}-\frac{(-1)^{n+1}}{n^{3/2}}+o(n^{-2}).$$
La série $\sum1/n$ diverge ; $\sum1/n^2$ converge ; la série alternée en $1/\sqrt n$ converge.

**Précision de transcription :** pour justifier le reste $o(n^{-2})$ après multiplication, on peut écrire $(1+1/n)^{-1}=1-1/n+O(n^{-2})$. Le développement seulement à l’ordre 1 avec $o(1/n)$, écrit dans le manuscrit, ne fournit pas directement ce reste plus précis.

## Page 65

**Exercice 12, 2.e (fin).** Les termes en $(-1)^{n+1}/n^{3/2}$ sont absolument sommables, et le reste $o(n^{-2})$ également par comparaison à Riemann. La seule contribution divergente est celle en $1/n$ : **$\sum u_n$ diverge**.

#### Exercice 13

Poser
$$a_n=\frac{n!e^n}{n^n\sqrt n},\qquad u_n=\ln a_{n+1}-\ln a_n=\ln\frac{a_{n+1}}{a_n}.$$
**1. Montrer que $\sum u_n$ converge.**
$$\frac{a_{n+1}}{a_n}=\frac{(n+1)!}{n!}\frac{e^{n+1}}{e^n}\frac{n^n}{(n+1)^{n+1}}\frac{\sqrt n}{\sqrt{n+1}}$$
$$=e\left(\frac n{n+1}\right)^n\sqrt{\frac n{n+1}}=e^{-n\ln(1+1/n)+1+\frac12\ln(n/(n+1))}.$$

## Page 66

**Exercice 13, 1 (suite).** L’expression exacte est
$$u_n=1-n\ln(1+1/n)+\frac12\ln\frac n{n+1}=1-\left(n+\frac12\right)\ln\left(1+\frac1n\right).$$
Le manuscrit remplace le logarithme par $1/n-1/(2n^2)+o(n^{-2})$, puis affiche $u_n=-1/(4n^2)+o(n^{-2})$ et conclut à la convergence par comparaison avec Riemann.

**Erreur du support et correction du calcul.** Le développement du logarithme à l’ordre 2 ne suffit pas, car il est multiplié par $n+1/2$ ; en outre le coefficient affiché est incorrect. À l’ordre 3,
$$\ln(1+1/n)=\frac1n-\frac1{2n^2}+\frac1{3n^3}+o(n^{-3}),$$
$$\left(n+\frac12\right)\ln(1+1/n)=1+\frac1{12n^2}+o(n^{-2}).$$
Donc **$u_n\sim-1/(12n^2)$**. La conclusion du manuscrit reste correcte : les termes sont de signe constant à partir d’un rang et $\sum u_n$ converge, même absolument, par comparaison à $\sum1/n^2$.

## Page 67

**Exercice 13, 2.** En déduire que $(a_n)$ converge vers un réel $L>0$.

On sait que $\sum u_n$ converge et $u_n=\ln a_{n+1}-\ln a_n$. Alors
$$S_N=\sum_{n=1}^Nu_n=\ln a_{N+1}-\ln a_1.$$
La suite $(S_N)$ converge ; noter $S$ sa limite. Comme $a_1=e$,
$$S=\lim_{N\to+\infty}\ln a_{N+1}-\ln e=\lim_{N\to+\infty}\ln a_{N+1}-1.$$

## Page 68

**Exercice 13, 2 (fin).** $\ln a_{N+1}\to S+1$. L’exponentielle étant continue,
$$a_{N+1}=e^{\ln a_{N+1}}\to e^{S+1}>0.$$
La suite $(a_n)$ converge donc vers $L=e^{S+1}\in\mathbb R_+^*$.

**3.** La suite $(a_n^2)$ converge vers $L^2$. La sous-suite $(a_{2n})$ converge vers $L$. Par quotient,
$$\frac{a_n^2}{a_{2n}}\longrightarrow\frac{L^2}L=L.$$

## Page 69

**Exercice 13, 3 (suite).** Avec $a_n=n!e^n/(n^n\sqrt n)$,
$$\frac{a_n^2}{a_{2n}}=\frac{(n!)^2e^{2n}}{n^{2n}n}\frac{(2n)^{2n}\sqrt{2n}}{(2n)!e^{2n}}=\frac{(2^nn!)^2}{\sqrt n(2n)!}\sqrt2.$$
Le manuscrit utilise la limite
$$\frac{(2^nn!)^2}{(2n)!\sqrt{2n}}\longrightarrow\sqrt{\frac\pi2},$$
d’où $\frac{(2^nn!)^2}{\sqrt n(2n)!}\to\sqrt\pi$, puis
$$\frac{a_n^2}{a_{2n}}\to\sqrt\pi\sqrt2=\sqrt{2\pi}.$$
Par la question précédente, $L=\sqrt{2\pi}$.

**4.** Ainsi
$$\frac{n!e^n}{n^n\sqrt n}\sim\sqrt{2\pi},\qquad n!\sim n^n\sqrt n\,e^{-n}\sqrt{2\pi}.$$
La limite intermédiaire est utilisée comme connue dans le manuscrit, sans démonstration sur cette page.

## Page 70

**Exercice 13, conclusion — formule de Stirling.**
$$\boxed{n!\sim_{n\to+\infty}\left(\frac ne\right)^n\sqrt{2\pi n}}.$$
Le reste de la page est vide.
