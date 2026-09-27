---
source: PREING1-S1/Analyse1/Fiche-Somme-Produit_2024-2025_Analyse1_P1S1__CarlotaM.pdf
pages: 1
transcription: manuelle
---

# Analyse 1 — Sommes et produits

## Notations

Pour $m\le n$,

$$\sum_{i=m}^n a_i=a_m+a_{m+1}+\cdots+a_n,$$

$$\prod_{i=m}^n a_i=a_m a_{m+1}\cdots a_n.$$

La factorielle est $n!=\prod_{k=1}^n k$ pour $n\ge1$, avec $0!=1$ et $n!=n(n-1)!$.

## Relation de Chasles

Pour des entiers $m\le p<n$,

$$\sum_{k=m}^n a_k=\sum_{k=m}^p a_k+\sum_{k=p+1}^n a_k,$$

$$\prod_{k=m}^n a_k=\left(\prod_{k=m}^p a_k\right)\left(\prod_{k=p+1}^n a_k\right).$$

## Linéarité des sommes

Pour deux familles de réels $(a_i)$ et $(b_i)$, et $\lambda,\beta\in\mathbb R$,

$$\sum_{i=m}^n(a_i+b_i)=\sum_{i=m}^n a_i+\sum_{i=m}^n b_i,$$

$$\sum_{i=m}^n\lambda a_i=\lambda\sum_{i=m}^n a_i,$$

$$\sum_{i=m}^n(\lambda a_i+\beta b_i)=\lambda\sum_{i=m}^n a_i+\beta\sum_{i=m}^n b_i.$$

## Propriétés des produits

**Multiplicativité :**

$$\prod_{i=m}^n(a_i b_i)=\left(\prod_{i=m}^n a_i\right)\left(\prod_{i=m}^n b_i\right).$$

**Puissance :** pour $p\in\mathbb N$, lorsque les puissances sont définies,

$$\prod_{i=m}^n a_i^p=\left(\prod_{i=m}^n a_i\right)^p.$$

**Facteur constant :**

$$\prod_{k=m}^n(\lambda a_k)=\lambda^{n-m+1}\prod_{k=m}^n a_k.$$

## Simplifications télescopiques

Dans la somme

$$\sum_{i=m}^n(a_{i+1}-a_i)
=(a_{m+1}-a_m)+(a_{m+2}-a_{m+1})+\cdots+(a_{n+1}-a_n),$$

les termes intermédiaires s'annulent, d'où

$$\sum_{i=m}^n(a_{i+1}-a_i)=a_{n+1}-a_m.$$

Pour des réels non nuls $a_m,\ldots,a_{n+1}$,

$$\prod_{i=m}^n\frac{a_{i+1}}{a_i}=\frac{a_{n+1}}{a_m}.$$

En particulier,

$$\prod_{k=0}^n\frac{a_{k+1}}{a_k}
=\frac{a_1}{a_0}\frac{a_2}{a_1}\cdots\frac{a_{n+1}}{a_n}
=\frac{a_{n+1}}{a_0}.$$

## Sommes usuelles

**Somme de constantes :**

$$\sum_{k=m}^n a=(n-m+1)a.$$

Il y a $n-m+1$ termes.

**Somme arithmétique :**

$$\sum_{k=m}^n k=\frac{(n-m+1)(m+n)}2,\qquad
\sum_{k=0}^n k=\frac{n(n+1)}2.$$

**Somme géométrique :** pour $q\ne1$,

$$\sum_{i=m}^n q^i=q^m\frac{1-q^{n-m+1}}{1-q},\qquad
\sum_{i=0}^n q^i=\frac{1-q^{n+1}}{1-q}.$$

> La condition $q\ne1$, implicite dans les quotients de la fiche, est explicitée ici. Pour $q=1$, la somme vaut $n-m+1$.
