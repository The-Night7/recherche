# Algèbre 2 — DS 2018–2019, corrigé (5 mars 2019)

> Source : `PREING1-S2/Algebre2-DS/DS2-2018-2019-Correction_Algebre2-DS_P1S2_KFayad.pdf`, 3 pages (PDF natif LaTeX).
> Transcription du 13 octobre 2026 : lecture visuelle intégrale, recoupée avec le texte natif ; formules restituées en LaTeX. L’adresse électronique de l’auteur en en-tête n’est pas reproduite.
> **Écart de nommage :** le document est intitulé « Corrigé DS5 Algèbre (05/03/2019) » alors que le fichier est nommé DS2. L’énoncé n’est pas fourni : les objets ($V$, $W$, $F$, $G$, familles $\mathscr F,\mathscr F'$) ne sont connus que par le corrigé.
> Vérification : les calculs ont été refaits. Erreur de la source : à l’exercice 1.3, il faut lire « **$V+W$** est donc un sous-espace vectoriel de $\mathbb R^4$, de dimension 4 », et non « $V\cap W$ ». Coquilles conservées : « $(X-1)^2.,$ ».

# Corrigé DS5 Algèbre (05/03/2019)

## Exercice 1

1. On a $V=\{a\cdot(4,2,1,0)+b\cdot(0,0,0,1),\ (a,b)\in\mathbb R^2\}=\operatorname{vect}((4,2,1,0),(0,0,0,1))$.
   Ainsi, $V$ est un sous-espace vectoriel de $\mathbb R^4$ : c’est le sous-espace vectoriel de $\mathbb R^4$ engendré par la famille $((4,2,1,0),(0,0,0,1))$.

   Montrons que $W$ est un sous-espace vectoriel de $\mathbb R^4$ :
   On a : $(0,0,0,0)\in W$.
   Soit $X=(x,y,z,t)$ et $X'=(x',y',z',t')$ deux vecteurs de $W$ et soit $\lambda\in\mathbb R$. Montrons que $\lambda\cdot X+X'\in W$.
   Comme $(X,X')\in W^2$, on a $x+z=y+t$ et $x'+z'=y'+t'$.
   On a $\lambda\cdot X+X'=(\lambda x+x',\lambda y+y',\lambda z+z',\lambda t+t')$ avec :

   $$(\lambda x+x')+(\lambda z+z')=\lambda(x+z)+(x'+z')=\lambda(y+t)+(y'+t')=(\lambda y+y')+(\lambda t+t').$$

   Ainsi, $\lambda\cdot X+X'\in W$.

2. Par définition de $V$, la famille $((4,2,1,0),(0,0,0,1))$ en est une famille génératrice, de plus, cette famille est libre ; c’est donc une base de $V$, et $\dim(V)=2$.

   Cherchons une base de $W$ :
   Soit $X=(x,y,z,t)\in W$, alors $x+z=y+t$ d’où $x=y+t-z$, alors

   $$X=(y+t-z,y,z,t)=y\cdot(1,1,0,0)+z\cdot(-1,0,1,0)+t\cdot(1,0,0,1).$$

   Ainsi, $W\subset\operatorname{vect}((1,1,0,0),(-1,0,1,0),(1,0,0,1))$.
   Réciproquement, $(1,1,0,0)\in W$, $(-1,0,1,0)\in W$ et $(1,0,0,1)\in W$, d’où

   $$W=\operatorname{vect}((1,1,0,0),(-1,0,1,0),(1,0,0,1)).$$

   Montrons que la famille $((1,1,0,0),(-1,0,1,0),(1,0,0,1))$ est libre :
   Soit $(a,b,c)\in\mathbb R^3$ tel que $a\cdot(1,1,0,0)+b\cdot(-1,0,1,0)+c\cdot(1,0,0,1)=0$, alors $(a-b+c,a,b,c)=(0,0,0,0)$ d’où $a=b=c=0$.
   On déduit que la famille $((1,1,0,0),(-1,0,1,0),(1,0,0,1))$ est une base de $W$, et $\dim(W)=3$.

   Cherchons une base de $V\cap W$ :
   Soit $X=(x,y,z,t)\in V\cap W$ :
   - $X\in V\Rightarrow x=4z$ et $y=2z$
   - $X\in W\Rightarrow x=y+t-z$

   On obtient ainsi $4z=2z+t-z$, d’où $t=3z$ et $X=(4z,2z,z,3z)=z\cdot(4,2,1,3)$, on déduit que $V\cap W\subset\operatorname{vect}((4,2,1,3))$. Réciproquement, $(4,2,1,3)\in V\cap W$, ainsi $V\cap W=\operatorname{vect}((4,2,1,3))$.
   Le vecteur $(4,2,1,3)$ forme donc une base de $V\cap W$, et $\dim(V\cap W)=1$.

3. On a $\dim(V+W)=\dim(V)+\dim(W)-\dim(V\cap W)=2+3-1=4$.
   $V\cap W$ est donc un sous-espace vectoriel de $\mathbb R^4$, de dimension 4. On en déduit que $V+W=\mathbb R^4$.

## Exercice 2

1. On a clairement $0\in G$.
   Soit $(P,Q)\in G^2$ et $\lambda\in\mathbb R$. Montrons que $\lambda\cdot P+Q\in G$.
   Comme $(P,Q)\in G^2$, alors $P(1)=P'(1)=Q(1)=Q'(1)=0$, d’où :
   $(\lambda\cdot P+Q)(1)=\lambda P(1)+Q(1)=0$ et $(\lambda\cdot P+Q)'(1)=\lambda P'(1)+Q'(1)=0$. Ainsi, $\lambda\cdot P+Q\in G$.

2. Cherchons une base de $G$ (afin de calculer la dimension de $G$) :
   Soit $P\in G$, alors $P(1)=P'(1)=0$, alors $1$ est une racine au moins double de $P$, donc $P$ est divisible par $(X-1)^2$. Ainsi, il existe $Q\in\mathbb R[X]$ tel que $P=(X-1)^2Q$, avec $\deg(Q)\le1$ car $\deg(P)\le3$.
   Le polynôme $Q$ s’écrit alors $a+bX$ avec $(a,b)\in\mathbb R^2$, d’où $P=(X-1)^2(aX+b)=aX(X-1)^2+b(X-1)^2$.
   On en déduit que $G\subset\operatorname{vect}((X(X-1)^2,(X-1)^2)$.
   Réciproquement, $X(X-1)^2\in G$ et $(X-1)^2\in G$ car ces deux polynômes sont divisibles par $(X-1)^2.$, d’où

   $$G=\operatorname{vect}((X(X-1)^2,(X-1)^2)).$$

   De plus, la famille $((X(X-1)^2,(X-1)^2)$ est libre (famille de polynômes non nuls de degrés deux à deux distincts), c’est donc une base de $G$ et $\dim(G)=2$.

   Montrons maintenant que la famille $((X-1)^2,(X-1)^3)$ est une base de $G$ :
   On a clairement $(X-1)^2\in G$ et $(X-1)^3\in G$ car ces deux polynômes sont divisibles par $(X-1)^2$.
   La famille $((X-1)^2,(X-1)^3)$ est donc une famille libre (degrés distincts) de deux vecteurs de $G$, et comme $G$ est de dimension 2, on en déduit qu’il s’agit d’une base de $G$.

3. Comme $F$ est de dimension 2, il suffit de remarquer que la famille $(1,X-1)$ est une famille libre de vecteurs $F$, ce qui est clair (degrés distincts).

4. Il suffit de vérifier deux parmi les trois conditions suivantes :
   - $\dim(F)+\dim(G)=\dim(\mathbb R_3[X])$
   - $F+G=\mathbb R_3[X]$
   - $F\cap G=\{0\}$

   En effet :
   - On a $\dim(F)+\dim(G)=2+2=4=\dim(\mathbb R_3[X])$.
   - $F+G=\operatorname{vect}(1,X-1)+\operatorname{vect}((X-1)^2,(X-1)^3)=\operatorname{vect}(1,X-1,(X-1)^2,(X-1)^3)=\mathbb R_3[X]$ car la famille $(1,X-1,(X-1)^2,(X-1)^3)$ est une famille libre contenant 4 vecteurs dans $\mathbb R_3[X]$ qui est de dimension 4, elle engendre donc $\mathbb R_3[X]$.
   - Soit $P\in F\cap G$, alors il existe $(a,b,c,d)\in\mathbb R^4$ tel que $P=a+b(X-1)$ et $P=c(X-1)^2+d(X-1)^3$, ainsi $a+b(X-1)-c(X-1)^2-d(X-1)^3=0$, d’où $a=b=c=d=0$ car la famille $(1,X-1,(X-1)^2,(X-1)^3)$ est libre. On en déduit que $P=0$.

5. (a) On cherche $(a,b,c,d)\in\mathbb R^4$ tel que $P=a+b(X-1)+c(X-1)^2+d(X-1)^3$, d’où

   $$1+X+X^2+X^3=(a-b+c-d)+(b-2c+3d)X+(c-3d)X^2+dX^3.$$

   D’où le système

   $$\begin{cases}d=1\\ c-3d=1\\ b-2c+3d=1\\ a-b+c-d=1\end{cases}\Leftrightarrow\begin{cases}d=1\\ c=4\\ b=6\\ a=4\end{cases}$$

   On déduit que

   $$1+X+X^2+X^3=4+6(X-1)+4(X-1)^2+(X-1)^3.$$

   (b) De la question précédente, on déduit directement que $P=P_1+P_2$ avec :
   - $P_1=4+6(X-1)\in F$
   - $P_2=4(X-1)^2+(X-1)^3\in G$.

## Exercice 3

1. Il faut que $\operatorname{rg}(\mathscr F)+\operatorname{rg}(\mathscr F')<3$.
   On prend par exemple $\mathscr F$ la famille formée par le vecteur $(1,0,0)$ et $\mathscr F'$ la famille formée par le vecteur $(0,1,0)$.
   On a clairement $\operatorname{vect}(\mathscr F)\cap\operatorname{vect}(\mathscr F')=\{0\}$ mais $\operatorname{vect}(\mathscr F)+\operatorname{vect}(\mathscr F')=\operatorname{vect}((1,0,0),(0,1,0))\neq\mathbb R^3$.
2. Il faut que $\operatorname{vect}(\mathscr F)\cap\operatorname{vect}(\mathscr F')\neq\{0\}$.
   On prend par exemple $\mathscr F=((1,0,0),(0,1,0))$ et $\mathscr F'=((0,1,0),(0,0,1))$.
   On a $\operatorname{vect}(\mathscr F)+\operatorname{vect}(\mathscr F')=\operatorname{vect}((1,0,0),(0,1,0),(0,0,1))=\mathbb R^3$ mais $\operatorname{vect}(\mathscr F)\cap\operatorname{vect}(\mathscr F')=\operatorname{vect}((0,1,0))$.
3. On prend $\mathscr F=((1,0,0),(0,1,0))$ et $\mathscr F'=((0,0,1))$.
   On a $\dim(\operatorname{vect}(\mathscr F))+\dim(\operatorname{vect}(\mathscr F'))=\operatorname{rg}(\mathscr F)+\operatorname{rg}(\mathscr F')=2+1=3=\dim(\mathbb R^3)$ et $\operatorname{vect}(\mathscr F)+\operatorname{vect}(\mathscr F')=\operatorname{vect}((1,0,0),(0,1,0),(0,0,1))=\mathbb R^3$, ainsi $\operatorname{vect}(\mathscr F)$ et $\operatorname{vect}(\mathscr F')$ sont supplémentaires dans $\mathbb R^3$.

## Exercice 4

1. (a) On a $F\oplus G=\operatorname{vect}(u_1,\cdots,u_m)+\operatorname{vect}(v_1,\cdots,v_n)=\operatorname{vect}(u_1,\cdots,u_m,v_1,\cdots,v_n)$, ainsi, la famille $(u_1,\cdots,u_m,v_1,\cdots,v_n)$ engendre $F\oplus G$.
   Montrons que cette famille est libre :
   Soit $(\lambda_1,\cdots,\lambda_m,\mu_1,\cdots,\mu_n)\in\mathbb K^{m+n}$ tel que $\lambda_1u_1+\cdots+\lambda_mu_m+\mu_1v_1+\cdots+\mu_nv_n=0$. On a alors

   $$\underbrace{\lambda_1u_1+\cdots+\lambda_mu_m}_{\in F}=\underbrace{-(\mu_1v_1+\cdots+\mu_nv_n)}_{\in G}\in F\cap G=\{0\}.$$

   On en déduit que $\lambda_1u_1+\cdots+\lambda_mu_m=0$ et $\mu_1v_1+\cdots+\mu_nv_n=0$ ; comme les familles $(u_1,\cdots,u_m)$ et $(v_1,\cdots,v_n)$ sont libres, on déduit que $\lambda_1=\cdots=\lambda_m=\mu_1=\cdots=\mu_n=0$.
   Ainsi, la famille $(u_1,\cdots,u_m,v_1,\cdots,v_n)$ est libre. C’est donc une base de $F\oplus G$.

   (b) Dans la question précédente, on a trouvé une base de $F\oplus G$ contenant $m+n$ vecteurs. On déduit que

   $$\dim(F\oplus G)=m+n=\dim(F)+\dim(G).$$

   C’est la formule de Grassmann dans le cas où $F$ et $G$ sont en somme directe (car $F\cap G=\{0\}$).

2. (a) On a : $F=(F\cap G)\oplus H$, d’où

   $$\dim(F)=\dim((F\cap G)\oplus H)=\dim(F\cap G)+\dim(H)$$

   car $F\cap G$ et $H$ sont en somme directe (on peut donc appliquer le résultat de la question 1).

   (b) Comme $G$ est un sous-espace vectoriel de $E$, et $G\subset F+G$, alors $G$ est un sous-espace vectoriel de $F+G$.
   Comme $H$ est un sous-espace vectoriel de $F$, et $H\subset F\subset F+G$, alors $H$ est un sous-espace vectoriel de $F+G$.

   (c) Montrons que $G\cap H=\{0\}$.
   Soit $x\in G\cap H$. Comme $H\subset F$, alors $x\in F$, ainsi, $x\in H$ et $x\in F\cap G$, or $H$ et $F\cap G$ sont en somme directe, d’où $x=0$.
   Ou : comme $H\subset F$, alors $G\cap H\subset(F\cap G)\cap H=\{0\}$. Ainsi, $G\cap H=\{0\}$.

   (d) $G$ et $H$ étant des sous-espaces vectoriels de $F+G$, on a : $G+H\subset F+G$.
   Réciproquement, montrons que $F+G\subset G+H$.
   Soit $x\in F+G$, alors il existe $(y,z)\in F\times G$ tel que $x=y+z$.
   Or $F=(F\cap G)+H$ ; comme $y\in F$, alors il existe $(t,u)\in(F\cap G)\times H$ tel que $y=t+u$.
   Ainsi $x=z+t+u$ avec $z\in G$, $t\in F\cap G\subset G$ et $u\in H$. D’où

   $$x=\underbrace{z+t}_{\in G}+\underbrace{u}_{\in H}\in G+H.$$

   (e) Des deux questions précédentes, on déduit que $G$ et $H$ sont supplémentaires dans $F+G$, autrement dit : $F+G=G\oplus H$.

   (f) Comme $G$ et $H$ sont en somme directe, d’après la question 1, on a $\dim(G\oplus H)=\dim(G)+\dim(H)$.
   D’autre part, d’après la question 2a, on a $\dim(H)=\dim(F)-\dim(F\cap G)$.
   Ainsi,

   $$\begin{aligned}
   \dim(F+G)&=\dim(G\oplus H)\\
   &=\dim(G)+\dim(H)\\
   &=\dim(G)+\dim(F)-\dim(F\cap G)
   \end{aligned}$$
