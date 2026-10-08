---
source: "PREING2-S1/Analyse-dans-RN-DS/DS3-2022-2023-Correction_Analyse-dans-RN-DS_P2S1__RayaneM.pdf"
pages: 6
transcription: manuelle, depuis les pages manuscrites
transcription_date: 2026-10-08
verification: lecture visuelle intégrale des 6 pages manuscrites ; calculs transcrits, erreurs et domaines manquants signalés
---

# Analyse dans Rn — DS3 2022–2023 : correction manuscrite

## Page 1

### DS3 2022–2023 — Correction manuscrite

#### Exercice 1

**1. Compatibilité.** Les dérivées premières reprises dans les calculs sont
$$f_x=\frac1y-y^2\sin(xy^2)+2x\cos(x^2+y^2)+e^x,$$
$$f_y=-\frac{x}{y^2}-2xy\sin(xy^2)+2y\cos(x^2+y^2)+\frac1{y+1}.$$
En dérivant la seconde en $x$ et la première en $y$, on trouve dans les deux cas
$$-\frac1{y^2}-2y[\sin(xy^2)+xy^2\cos(xy^2)]-4xy\sin(x^2+y^2).$$
Le manuscrit conclut à la compatibilité des dérivées croisées.

**Réserve de domaine :** la page écrit « sur $\mathbb R^2$ », mais les expressions excluent au moins $y=0$ et $y=-1$. L’énoncé complet du domaine n’apparaît pas dans ces pages.

**2. Intégration en $x$.**
$$f(x,y)=\frac xy+\cos(xy^2)+\sin(x^2+y^2)+e^x+K(y).$$
En dérivant en $y$,
$$f_y=-\frac{x}{y^2}-2xy\sin(xy^2)+2y\cos(x^2+y^2)+K'(y).$$

## Page 2

**Exercice 1 — fin.** La comparaison donne $K'(y)=1/(y+1)$. Le manuscrit écrit $K(y)=\ln(1+y)+C$, puis
$$f(x,y)=\frac xy+\cos(xy^2)+\sin(x^2+y^2)+e^x+\ln(1+y)+C.$$
Cette formule réelle vaut pour $y>-1$, $y\ne0$. Sur un intervalle situé sous $-1$, la primitive est $\ln|1+y|$ ; des constantes indépendantes sont possibles sur les composantes disjointes du domaine.

#### Exercice 2

**1.** Le changement de variables est $\varphi(x,y)=(x^2+y,x^2-y)=(u,v)$. Ses composantes sont polynomiales, donc de classe $C^1$. On résout
$$u=x^2+y,\quad v=x^2-y\quad\Longrightarrow\quad x=\sqrt{\frac{u+v}{2}},\quad y=\frac{u-v}{2}.$$
La branche positive correspond à $x>0$. L’inverse est donc
$$\varphi^{-1}(u,v)=\left(\sqrt{\frac{u+v}{2}},\frac{u-v}{2}\right),\qquad u+v>0.$$
Il est de classe $C^1$ sur ce demi-plan, ce qui établit le difféomorphisme pour la branche $x>0$.

**Note sur la source :** le domaine initial est seulement nommé $D$ ; sa définition n’est pas reproduite. Une ligne semble inclure $u+v=0$, mais la justification suivante utilise bien $u+v>0$, nécessaire à la régularité de l’inverse et à $x>0$.

**2.** On pose $f=g\circ\varphi$, puis on applique la règle de la chaîne.

## Page 3

**Exercice 2 — résolution.**
$$f_x=2x(g_u+g_v),\qquad f_y=g_u-g_v.$$
L’équation reprise sur la page est $f_x+2xf_y=16x^3y$. En substituant et en divisant par $4x$ sur la branche $x>0$,
$$g_u=4x^2y=4\frac{u+v}{2}\frac{u-v}{2}=u^2-v^2.$$
Donc
$$g(u,v)=\frac{u^3}{3}-uv^2+h(v),$$
où $h$ est de classe $C^1$, puis
$$f(x,y)=(x^2+y)\left[\frac{(x^2+y)^2}{3}-(x^2-y)^2\right]+h(x^2-y).$$

#### Exercice 3

**1.** Le changement est $\varphi(x,y)=(y,x/y)=(u,v)$, avec $y\ne0$. Il est de classe $C^2$ sur son domaine $A$, nommé sans définition complète dans ces pages. Les équations donnent $(x,y)=(uv,u)$ ; ainsi
$$\varphi^{-1}(u,v)=(uv,u).$$
Sur les domaines correspondants $A,B$, l’application et son inverse sont de classe $C^2$ : c’est un $C^2$-difféomorphisme.

## Page 4

**Exercice 3 — 2, dérivées.** Avec $f=g\circ\varphi$, donc $g=f\circ\varphi^{-1}$, les fonctions sont de classe $C^2$. On obtient
$$f_x=\frac1u g_v,\qquad f_y=g_u-\frac vu g_v,\qquad f_{xx}=\frac1{u^2}g_{vv}.$$
Le manuscrit donne ensuite $f_{xy}=g_{uv}/u-vg_{vv}/u^2$ et $f_{yy}=g_{uu}-2vg_{uv}/u+v^2g_{vv}/u^2$.

**Correction des dérivations des coefficients :** les formules complètes sont
$$f_{xy}=\frac1u g_{uv}-\frac1{u^2}g_v-\frac v{u^2}g_{vv},$$
$$f_{yy}=g_{uu}-\frac{2v}{u}g_{uv}+\frac{2v}{u^2}g_v+\frac{v^2}{u^2}g_{vv}.$$
Les termes en $g_v$ manquants dans le manuscrit se compensent toutefois dans l’opérateur de la question suivante.

**3.** L’équation est
$$x^2f_{xx}+2xyf_{xy}+y^2f_{yy}=xy+2y^3.$$
Avec $x=uv$, $y=u$, elle devient $u^2g_{uu}=u^2v+2u^3$, donc $g_{uu}=v+2u$. Première intégration : $g_u=uv+u^2+K(v)$.

**Seconde intégration corrigée :**
$$g(u,v)=\frac12u^2v+\frac13u^3+uK(v)+H(v),$$
soit
$$f(x,y)=\frac12xy+\frac13y^3+yK(x/y)+H(x/y).$$
Les fonctions arbitraires sont de classe $C^2$ sur les intervalles correspondant au domaine.

**Lacunes du manuscrit :** le terme $uK(v)$ disparaît dans la seconde intégration ; un signe devant $u^3/3$ est aussi incohérent avec $g_u$. La dernière formule inscrite retient seulement $y^2(x/(2y)+y/3)+h(x/y)$, qui est une sous-famille de solutions, sans le terme arbitraire $yK(x/y)$.

## Page 5

#### Exercice 4 — régularité

La fonction étudiée est $f(x,y)=x^5/(x^2+y^2)$ hors de l’origine, prolongée par $f(0,0)=0$.

**1.** Hors de zéro, elle est continue comme quotient de fonctions continues à dénominateur non nul. En coordonnées polaires,
$$f(r\cos\theta,r\sin\theta)=r^3\cos^5\theta\to0,$$
uniformément en $\theta$. Donc $f$ est continue sur $\mathbb R^2$.

Hors de zéro,
$$f_x=\frac{5x^4(x^2+y^2)-2x^6}{(x^2+y^2)^2}=\frac{x^4(3x^2+5y^2)}{(x^2+y^2)^2},\qquad f_y=-\frac{2yx^5}{(x^2+y^2)^2}.$$
En zéro, $f_x(0,0)=\lim_{t\to0}t^2=0$ et $f_y(0,0)=0$. En polaires,
$$f_x=r^2\cos^4\theta(3\cos^2\theta+5\sin^2\theta)\to0.$$

**Correction de simplification :** le manuscrit perd le facteur $5$ devant $y^2$ dans le numérateur simplifié de $f_x$, ainsi qu’un facteur $\cos^4\theta$ dans une ligne en polaires. Les formules ci-dessus les rétablissent ; la limite nulle reste correcte.

## Page 6

**Exercice 4 — 1, fin.**
$$f_y(r\cos\theta,r\sin\theta)=-2r^2\sin\theta\cos^5\theta\to0.$$
Les dérivées partielles sont donc continues à l’origine et hors de l’origine ; ainsi $f\in C^1(\mathbb R^2)$.

**2. Différentielle d’une composée.** Le manuscrit introduit $\varphi(x,y)=xy^2g(x,y)$, comme produit de fonctions différentiables, puis $h=f\circ\varphi$. Le diagramme est
$$\mathbb R^2\xrightarrow{\ \varphi\ }\mathbb R^2\xrightarrow{\ f\ }\mathbb R.$$
Pour $a\in\mathbb R^2$ et un incrément $k=(k_1,k_2)$, la règle de la chaîne donne
$$Dh(a)[k]=Df(\varphi(a))[D\varphi(a)[k]].$$
Le texte développe cette identité à l’aide des dérivées de $\varphi$ en $x,y$ et de celles de $f$ au point $\varphi(a)$.

**Précision de notation :** la définition complète de $g$ n’est pas reproduite dans ces pages. Selon le diagramme, $g$ et $\varphi$ prennent des valeurs dans $\mathbb R^2$. En écrivant $a=(a_1,a_2)$, le produit se différentie sous la forme
$$D\varphi(a)[k]=a_1a_2^2Dg(a)[k]+(a_2^2k_1+2a_1a_2k_2)g(a).$$
Cette écriture précise les dimensions que les notations manuscrites, utilisant un argument $t$ pour $f$, laissent implicites.
