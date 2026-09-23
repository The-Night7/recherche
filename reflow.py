# -*- coding: utf-8 -*-
"""
Mise en forme d'affichage des passages extraits de PDF (fmt == "pdf").

L'extraction PDF linéarise les formules : une fraction devient trois
lignes ("vn =", "un", "1 + un"), l'indice d'une somme passe à la ligne
("∑n∈N", "un"), chaque ligne du PDF est une ligne du texte. L'ancien
to_blocks() transformait chacun de ces morceaux en bloc "formule" : d'où
l'alternance illisible prose / encadrés.

Ici on produit un seul texte Markdown (rendu par renderMd + KaTeX côté
page) :
  - les lignes coupées par la largeur de page sont recollées en paragraphes ;
  - nouveau paragraphe seulement aux vrais débuts (Exercice, Réponse,
    Remarque, Théorème, ⇒, ⇐, tirets, questions numérotées...) ;
  - les fractions empilées sont reconstruites en $\\dfrac{…}{…}$ ;
  - ∑n∈N un, lim n→+∞ un, fn(x), (un) passent en LaTeX ;
  - les numéros de page isolés disparaissent.
C'est une heuristique : le texte indexé (chunks.json) n'est pas modifié.
"""
import re

HEADING_RE = re.compile(
    r"^(Exercice|R[ée]ponse|Question|Partie|Probl[èe]me)\s+\d+[a-z]?\b\s*[.:]?\s*(.*)$", re.I
)
BLOCK_START_RE = re.compile(
    r"^(Remarques?|D[ée]finition|Th[ée]or[èe]me|Proposition|Propri[ée]t[ée]|Lemme|Corollaire|"
    r"D[ée]monstration|Preuve|Exemples?|G[ée]n[ée]ralisation|Indication|Rappel|Consignes?|"
    r"Attention|Notation|M[ée]thode|Conclusion|Solution)\b"
)
LIST_RE = re.compile(r"^(?:(\d{1,2})[.)]|\(?([a-h]|i{1,3}|iv|v|vi{0,3})\))\s+(\S.*)$")
BULLET_RE = re.compile(r"^([—–•▶►]|-(?=\s))\s*(.*)$")
ARROW_START_RE = re.compile(r"^[⇒⇐]\s")
PAGE_NUM_RE = re.compile(r"^\d{1,3}$")
INLINE_ITEM_RE = re.compile(r"(?<=\S)\s+(?=\d{1,2}\.\s+(?:[a-zA-Z]{1,2}\w?(?:\(\w{1,3}\))?\s*=|∑))")

MATH_WORDS = {"sin", "cos", "tan", "exp", "ln", "log", "lim", "sup", "inf", "max", "min",
              "arctan", "arcsin", "arccos", "sh", "ch", "th", "cotan", "det", "si", "dt", "dx"}
OPERATOR_END_RE = re.compile(r"(?:[=<>≤≥∼≈⇔⇒+−\-×·(,]|:=|\bet)\s*$")
EQ_TAIL_RE = re.compile(r"^(.*[=<>≤≥∼≈])\s*(\S{1,12})$")


def balanced(s):
    d = 0
    for ch in s:
        d += ch in "(" 
        d -= ch in ")"
        if d < 0:
            return False
    return d == 0


def is_math_line(s, maxlen=20):
    s = s.strip()
    if not balanced(s) or re.search(r"[=→≠∼≤≥<>]|⇐|⇒|⇔|\blim\b|\(\d+\.\d+\)|[\[\]]", s) \
            or not re.search(r"[A-Za-z0-9α-ωΑ-Ω∂]", s):
        return False
    if not s or len(s) > maxlen or s[0] in ".,;:" or HEADING_RE.match(s):
        return False
    for w in re.findall(r"[A-Za-zÀ-ÿ]{3,}", s):
        if w.lower() not in MATH_WORDS:
            return False
    return True


# ---------- conversion vers LaTeX (uniquement dans un contexte mathématique) ----------
GREEK = {
    "α": r"\alpha ", "β": r"\beta ", "γ": r"\gamma ", "δ": r"\delta ", "ε": r"\varepsilon ",
    "θ": r"\theta ", "λ": r"\lambda ", "μ": r"\mu ", "π": r"\pi ", "ρ": r"\rho ", "σ": r"\sigma ",
    "τ": r"\tau ", "φ": r"\varphi ", "ϕ": r"\varphi ", "ψ": r"\psi ", "ω": r"\omega ", "Ω": r"\Omega ",
    "∞": r"\infty ", "−": "-", "×": r"\times ", "·": r"\cdot ", "≤": r"\le ", "≥": r"\ge ",
    "∼": r"\sim ", "≈": r"\approx ", "≠": r"\neq ", "∈": r"\in ", "→": r"\to ", "∂": r"\partial ",
    "⇔": r"\Leftrightarrow ", "⇒": r"\Rightarrow ", "√": r"\surd ", "ᐟ": "/", "!": "!", "∗": "^*",
}
SETS = {"N": r"\mathbb{N}", "Z": r"\mathbb{Z}", "R": r"\mathbb{R}", "C": r"\mathbb{C}", "Q": r"\mathbb{Q}"}


SUP_CHARS = {"⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5", "⁶": "6", "⁷": "7",
             "⁸": "8", "⁹": "9", "ⁿ": "n", "ᵖ": "p", "⁺": "+", "⁻": "-"}
SUP_CHARS["ᐟ"] = "/"
SUB_CHARS = {"₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4", "ₙ": "n", "ₖ": "k", "ₚ": "p",
             "ᵢ": "i", "ⱼ": "j", "ₘ": "m", "ₗ": "l"}


def tex(s):
    s = s.strip()
    s = re.sub(r"√\s*(\([^()]*\)|[A-Za-z0-9]+)", lambda m: r"\sqrt{" + m.group(1) + "}", s)
    s = re.sub("[" + "".join(SUP_CHARS) + "]+", lambda m: "^{" + "".join(SUP_CHARS[c] for c in m.group(0)) + "}", s)
    s = re.sub("[" + "".join(SUB_CHARS) + "]+", lambda m: "_{" + "".join(SUB_CHARS[c] for c in m.group(0)) + "}", s)
    s = re.sub(r"\b(sin|cos|tan|exp|ln|log|arctan)\b", r"\\\1 ", s)
    s = re.sub(r"(?<![A-Za-z\\])([a-zA-Z])([nkpij])(?![A-Za-z])", r"\1_\2", s)  # un -> u_n
    s = "".join(GREEK.get(ch, ch) for ch in s)
    return s


def frac(num, den):
    return f"$\\dfrac{{{tex(num)}}}{{{tex(den)}}}$"


SUM_RE = re.compile(r"([∑∏])\s*([a-z])\s*(∈\s*[NZRC]\*?|[≥>]\s*\d+|=\s*\d+)\s+(?!ln\b)([a-zA-Z])\2?(\([^()]{0,12}\))?(?![A-Za-z(])")
SUM_BARE_RE = re.compile(r"([∑∏])\s*([a-z])\s*(∈\s*[NZRC]\*?|[≥>]\s*\d+|=\s*\d+)")
LIM_RE = re.compile(r"\blim\s*([a-z])\s*→\s*([+−-]?∞|[+−-]?\d+[+−-]?)(?:([A-Za-z]{1,2}\([^()]{1,8}\))|\s*([a-zA-Z])\1(\([^()]{0,12}\))?)?")
FN_CALL_RE = re.compile(r"(?<![\w$\\])([a-zA-Z])([nk])\((\w{1,3})\)")
PAREN_SEQ_RE = re.compile(r"(?<![\w$])\(([a-zA-Z])([nk])\)(?:([nk])(\s*[≥∈>]\s*[\dNZ]+)?(?![\w]))?")


def sub_index(idx):
    idx = idx.replace(" ", "")
    m = re.match(r"∈([NZRC])(\*?)", idx)
    if m:
        return r"\in " + SETS[m.group(1)] + ("^*" if m.group(2) else "")
    return "".join(GREEK.get(ch, ch) for ch in idx)


SAFE_SUB_RE = re.compile(r"(?<![\w$\\_])([fgvwxyhSRP])([nk])(?![\w(])")
UN_OP_RE = re.compile(r"(?<![\w$])([uab])([nk])(?=\s*[=∼<>≤≥→])|(?<=[=∼<>≤≥⇔]\s)([uab])([nk])(?![\w(])")
SET_RE = re.compile(r"(?<![\w$\\{])(R|(?<=[∈⊂(] )[NZ]|(?<=[∈⊂(])[NZ]|(?<=\bsur )[NZ]|(?<=\bdans )[NZ])"
                    r"(?![A-Za-zÀ-ÿ0-9'’])(\s*∗)?(\s*\+(?![\w∞(]))?")
NORM_RE = re.compile(r"(?<![A-Za-z])k([a-zA-Z·]{1,3})k(?:(\d|∞)|(?=[\s,.;:)=≤≥<>+−-]|$))")
BRA_RE = re.compile(r"(?<![A-Za-z])h([a-zA-Z]{1,2})\|([a-zA-Z]{1,2})i(?![A-Za-z])")  # hu|vi = ⟨u|v⟩
SUBDIGIT = {"1": "₁", "2": "₂", "3": "₃", "∞": "∞"}
SETS_U = {"R": "ℝ", "N": "ℕ", "Z": "ℤ"}
SUBS_U = {"n": "ₙ", "k": "ₖ"}
MERGE_R = re.compile(r"\$([^$]+)\$\s*([=∼≠<>≤≥⇔])\s*(\$[^$]+\$|[+−-]?\d+(?:[.,]\d+)?(?![\w])|[+−-]?∞)")
MERGE_EQ = re.compile(r"\$([^$]+)\$\s*([=∼≠<>≤≥⇔])\s*\$([^$]+)\$")


def texify_rel(op):
    return GREEK.get(op, op).strip() if op not in "=<>" else op


def close_parens(p):
    r"""'$( \dfrac{1}{e}$)ⁿ' -> '$( \dfrac{1}{e})^{n}$'"""
    def repl(m):
        body, closers, sups = m.group(1), m.group(2), m.group(3)
        missing = body.count("(") - body.count(")")
        if missing <= 0:
            return m.group(0)
        take = closers[:missing]
        return "$" + body + take + (tex(sups) if sups else "") + "$" + closers[missing:]
    return re.sub(r"\$([^$]+)\$(\)+)([⁰-⁹¹²³ⁿᐟ⁻⁺]*)", repl, p)


def merge_math(p):
    p = close_parens(p)
    p = re.sub(r"(?<![\w$\\])([a-zA-Z0-9]{1,2})\$([^$]+)\$", lambda m: f"${m.group(1)}{m.group(2)}$"
               if not re.match(r"[A-Za-z]", m.group(2)[:1]) or len(m.group(1)) == 1 else m.group(0), p)
    p = re.sub(r"\$([^$]+)\$[ ]+\$([^$]+)\$", r"$\1 \2$", p)
    for _ in range(4):
        new = MERGE_R.sub(lambda m: f"${m.group(1)} {texify_rel(m.group(2))} "
                          f"{m.group(3)[1:-1] if m.group(3).startswith('$') else tex(m.group(3))}$", p)
        if new == p:
            break
        p = new
    return p


def inline_math(line):
    """convertit en LaTeX les constructions non ambiguës d'une ligne de prose"""
    def sum_term(m):
        op = r"\sum" if m.group(1) == "∑" else r"\prod"
        term = f"{m.group(4)}_{m.group(2)}" + (tex(m.group(5)) if m.group(5) else "")
        return f"${op}_{{{m.group(2)}{sub_index(m.group(3))}}} {term}$"

    def lim(m):
        to = "".join(GREEK.get(ch, ch) for ch in re.sub(r"(\d)([+−-])$", r"\1^\2", m.group(2)))
        if m.group(3):
            term = " " + tex(m.group(3))
        elif m.group(4):
            term = f" {m.group(4)}_{m.group(1)}" + (tex(m.group(5)) if m.group(5) else "")
        else:
            term = ""
        return f"$\\lim\\limits_{{{m.group(1)}\\to {to}}}{term}$" + ("" if term else " ")

    def paren_seq(m):
        rng = f"_{{{m.group(3)}{sub_index(m.group(4) or '')}}}" if m.group(3) else ""
        return f"$({m.group(1)}_{m.group(2)}){rng}$"

    parts = re.split(r"(\$[^$]+\$)", line)
    for i in range(0, len(parts), 2):
        p = parts[i]
        p = re.sub(r"([A-Za-z0-9]|\([^()]{1,14}\))([⁰-⁹¹²³ⁿ⁻⁺]+ᐟ[⁰-⁹¹²³ⁿ]+)", lambda m: f"${tex(m.group(0))}$", p)
        p = SUM_RE.sub(sum_term, p)
        p = SUM_BARE_RE.sub(lambda m: f"$\\{'sum' if m.group(1) == '∑' else 'prod'}_{{{m.group(2)}{sub_index(m.group(3))}}}$", p)
        p = LIM_RE.sub(lim, p)
        p = FN_CALL_RE.sub(lambda m: f"${m.group(1)}_{m.group(2)}({m.group(3)})$", p)
        p = PAREN_SEQ_RE.sub(paren_seq, p)
        p = UN_OP_RE.sub(lambda m: f"${m.group(1) or m.group(3)}_{m.group(2) or m.group(4)}$", p)
        parts[i] = p
    line = "".join(parts)
    parts = re.split(r"(\$[^$]+\$)", line)
    for i in range(0, len(parts), 2):
        p = SAFE_SUB_RE.sub(lambda m: m.group(1) + SUBS_U[m.group(2)], parts[i])
        p = BRA_RE.sub(r"⟨\1|\2⟩", p).replace("vuut", "√")
        p = NORM_RE.sub(lambda m: "‖" + m.group(1) + "‖" + SUBDIGIT.get(m.group(2) or "", m.group(2) or ""), p)
        p = SET_RE.sub(lambda m: SETS_U[m.group(1)] + ("∗" if m.group(2) else "") + ("₊" if m.group(3) else ""), p)
        parts[i] = p
    return merge_math("".join(parts))


# ---------- recollage des lignes ----------
BIG_SUM_RE = re.compile(r"^([+−-]?)\s*X\s*([+−-]?∞|[a-zA-Z0-9+−-]{1,4})$")
SUM_LOW_RE = re.compile(r"^([a-z])\s*=\s*(\S{1,6})$")
MATH_TAIL_TOKEN_RE = re.compile(r"^(?:[=<>≤≥∼≈⇔+−\-×·]|[α-ωΑ-Ω]|[a-zA-Z][nk]?(?:\(\w{1,3}\))?|\d+|[+−-]?∞)$")


def split_math_tail(cur):
    """'On en déduit que vn =' -> ('On en déduit que', 'vn =')"""
    toks = cur.rstrip().split(" ")
    j = len(toks)
    while j > 0 and MATH_TAIL_TOKEN_RE.match(toks[j - 1]):
        j -= 1
    # au moins une variable avant l'opérateur, sinon on ne prend que l'opérateur
    tail = toks[j:]
    if len(tail) < 2:
        return " ".join(toks[:-1]), toks[-1]
    return " ".join(toks[:j]), " ".join(tail)


def big_sums(lines):
    out, i = [], 0
    while i < len(lines):
        # "f(x) = X" / "+∞" / "n=0"  (le Σ du PDF est extrait comme un X)
        if lines[i].endswith(" X") and i + 2 < len(lines) \
                and re.fullmatch(r"[+−-]?∞|[a-zA-Z0-9+−-]{1,4}", lines[i + 1]) and SUM_LOW_RE.match(lines[i + 2]):
            low = SUM_LOW_RE.match(lines[i + 2])
            out.append(lines[i][:-1] + f"$\\sum_{{{low.group(1)}={tex(low.group(2))}}}^{{{tex(lines[i + 1])}}}$")
            i += 3
            continue
        m = BIG_SUM_RE.match(lines[i])
        low = SUM_LOW_RE.match(lines[i + 1]) if m and i + 1 < len(lines) else None
        if low:
            up = m.group(1) + m.group(2)
            out.append(f"$\\sum_{{{low.group(1)}={tex(low.group(2))}}}^{{{tex(up)}}}$")
            i += 2
            continue
        out.append(lines[i])
        i += 1
    return out


PARTIAL_RE = re.compile(r"^(∂\S{0,4}|d[a-zA-Z]{0,2})$")
POINT_RE = re.compile(r"^[a-zA-Z0-9]{1,2}(,[a-zA-Z0-9]{1,2}){1,3}$")


SUP_OF = {"0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸",
          "9": "⁹", "n": "ⁿ", "−": "⁻", "-": "⁻", "+": "⁺", "x": "ˣ", "k": "ᵏ", "p": "ᵖ", "t": "ᵗ"}
UNSUP = {v: k for k, v in SUP_OF.items() if k != "-"}
LONE_MARK_RE = re.compile(r"^\d{1,2}[.)]$")
REL_RE = re.compile(r"\s*(→|≠|=|∼|≤|≥|<|>)")


def sup(s):
    return "".join(SUP_OF[c] for c in s) if all(c in SUP_OF for c in s) else None


def exponents(l):
    """n2 -> n², (2n + 1)4 -> (2n + 1)⁴, (ln(n))n -> (ln(n))ⁿ : exposants posés à plat par l'extraction"""
    l = re.sub(r"(?<![A-Za-z_])n([2-9])(?![\d.,]\d|\w)", lambda m: "n" + SUP_OF[m.group(1)], l)
    l = re.sub(r"(?:(?<=[^\s(])|^)\)([2-9n])(?![\w(])", lambda m: ")" + SUP_OF[m.group(1)], l)
    return l


def repair_lines(lines):
    out, i = [], 0
    while i < len(lines):
        l = lines[i]
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        nxt2 = lines[i + 2] if i + 2 < len(lines) else ""
        nxt3 = lines[i + 3] if i + 3 < len(lines) else ""
        # "ln 1 + e" ... ")" : parenthèse ouvrante perdue avec la grande parenthèse
        if re.search(r"\bln \d", l) and ")" in lines[i + 1:i + 4]:
            l = re.sub(r"\bln (\d)", r"ln(\1", l)
        # quatre petits nombres empilés : "2" "4" "7" "3" = 2⁴/7³
        if all(re.fullmatch(r"\d{1,2}", x) for x in (l, nxt, nxt2, nxt3)):
            out.append(f"$\\dfrac{{{l}^{{{nxt}}}}}{{{nxt2}^{{{nxt3}}}}}$")
            i += 4
            continue
        # exposant fractionnaire : "n¹" / "2" = n^(1/2)
        if l.endswith("¹") and nxt in ("2", "n"):
            lines[i + 1] = l + "ᐟ" + SUP_OF[nxt]
            i += 1
            continue
        # "(un)" / "1" / "n = ..." ou ") 1" / "n" : puissance 1/n
        if re.search(r"\)$", l) and nxt == "1" and re.match(r"^n(\s|$)", nxt2):
            lines[i + 2] = l + "¹ᐟⁿ" + nxt2[1:]
            i += 2
            continue
        if re.search(r"\)\s*1$", l) and re.match(r"^n(\s|$)", nxt):
            lines[i + 1] = re.sub(r"\s*1$", "", l) + "¹ᐟⁿ" + nxt[1:]
            i += 1
            continue
        # "√" seul sur sa ligne : racine de la ligne suivante
        if l == "√" and nxt and len(nxt) <= 8:
            out.append("√" + nxt)
            i += 2
            continue
        # le Σ du PDF extrait comme "X" (avec parfois le 1er caractère du terme en exposant)
        m = re.match(r"^(\d{1,2}[.)]\s*)?X([¹²³ⁿ]?)$", l)
        if m:
            out.append((m.group(1) or "") + "∑")
            if m.group(2):
                c = UNSUP[m.group(2)]
                if c.isalpha() and re.match(r"^\d\s", nxt):  # "Xⁿ" / "2 + 1" = ∑ n² + 1
                    out.append(c + SUP_OF[nxt[0]] + nxt[1:])
                    i += 2
                    continue
                out.append(c)
            i += 1
            continue
        # exposant 1/n empilé : "ne" / "1" / "n − n"  ou  "e¹" / "n − 1"
        if re.search(r"e$", l) and nxt == "1" and re.match(r"^n\b", nxt2):
            out.append(l[:-1] + "e¹ᐟⁿ" + nxt2[1:])
            i += 3
            continue
        if l.endswith("e¹") and re.match(r"^n\b", nxt):
            out.append(l[:-2] + "e¹ᐟⁿ" + nxt[1:])
            i += 2
            continue
        # exposant seul sur la ligne suivante : "e" / "−n"
        me = re.match(r"^([−-]?[a-z0-9]{1,2})(\s+[=∼≠<>≤≥→].*)?$", nxt)
        if re.search(r"(?:^|[\s(+−-])e$", l) and me and sup(me.group(1)):
            lines[i + 1] = l + sup(me.group(1)) + (me.group(2) or "")
            i += 1
            continue
        out.append(exponents(l))
        i += 1
    return out


def split_rel(line):
    """'n2 → 1 ≠ 0 donc...' -> ('n2', ' → 1 ≠ 0 donc...') si le début est une petite formule"""
    m = REL_RE.search(line)
    if not m or m.start() == 0:
        return None
    head = line[:m.start()]
    return (head, line[m.start():]) if is_math_line(head, 14) else None


SUM_TAIL_RE = re.compile(r"∑\s*(?:([a-z])\s*(∈\s*[NZRC]\*?|[≥>]\s*\d+|=\s*\d+))?$")


def lone_frac(cur, num, den):
    """'1.' ou '2. ∑' ou '3. ∑n∈N' suivi d'une fraction"""
    m = SUM_TAIL_RE.search(cur)
    if m:
        pre = cur[:m.start()].rstrip()
        op = r"\sum" + (f"_{{{m.group(1)}{sub_index(m.group(2))}}}" if m.group(1) else "") + " "
    else:
        pre, op = cur, ""
    return (pre + " " if pre else "") + f"${op}\\dfrac{{{tex(num)}}}{{{tex(den)}}}$"


def rebuild_fractions(lines):
    out, i = [], 0
    while i < len(lines):
        cur = lines[i]
        nxt = lines[i + 1] if i + 1 < len(lines) else None
        nxt2 = lines[i + 2] if i + 2 < len(lines) else None
        # dérivée partielle empilée : "∂f" / "∂x" / "x,y"
        if cur.startswith("∂") and PARTIAL_RE.match(cur) and nxt and nxt.startswith("∂") and PARTIAL_RE.match(nxt):
            f = f"\\dfrac{{{tex(cur)}}}{{{tex(nxt)}}}"
            skip = 2
            if nxt2 and POINT_RE.match(nxt2):
                f += f"({nxt2})"
                skip = 3
            out.append(f"${f}$")
            i += skip
            continue
        # "vn =" / "un" / "1 + un"  ->  vn = frac(un, 1 + un)
        if "$" in cur or (nxt and "$" in nxt) or (nxt2 and "$" in nxt2):
            out.append(cur)
            i += 1
            continue
        lone = LONE_MARK_RE.match(cur) or SUM_TAIL_RE.search(cur)
        if nxt is not None and nxt2 is not None and (lone or OPERATOR_END_RE.search(cur)) \
                and is_math_line(nxt, 14) and not is_math_line(nxt2, 18) and split_rel(nxt2) \
                and not LIST_RE.match(nxt) and not OPERATOR_END_RE.search(nxt):
            den, rest = split_rel(nxt2)
            if lone:
                out.append(lone_frac(cur, nxt, den) + rest)
            else:
                head, tail = split_math_tail(cur)
                out.append((head + " " if head else "") + f"${tex(tail)} \\dfrac{{{tex(nxt)}}}{{{tex(den)}}}$" + rest)
            i += 3
            continue
        if nxt is not None and nxt2 is not None and lone \
                and is_math_line(nxt, 14) and is_math_line(nxt2, 18) and not LIST_RE.match(nxt2):
            out.append(lone_frac(cur, nxt, nxt2))
            i += 3
            continue
        if nxt is not None and nxt2 is not None and OPERATOR_END_RE.search(cur) \
                and is_math_line(nxt, 14) and is_math_line(nxt2, 18) \
                and not LIST_RE.match(nxt) and not LIST_RE.match(nxt2) and not nxt.startswith("∂") \
                and not OPERATOR_END_RE.search(nxt):
            head, tail = split_math_tail(cur)
            f = f"{tex(tail)} \\dfrac{{{tex(nxt)}}}{{{tex(nxt2)}}}"
            out.append((head + " " if head else "") + f"${f}$")
            i += 3
            continue
        # "fn(x) = 1" / "1 + n2x"  ->  fn(x) = frac(1, 1 + n2x)
        m = EQ_TAIL_RE.match(cur.rstrip())
        if m and nxt is not None and is_math_line(m.group(2), 12) and is_math_line(nxt, 14) \
                and not m.group(2).endswith((".", ",", ";")) and not LIST_RE.match(nxt) \
                and not PAGE_NUM_RE.match(nxt) and not HEADING_RE.match(nxt):
            den, skip = nxt, 2
            if nxt2 is not None and re.fullmatch(r"\d", nxt2.strip()):
                den, skip = nxt + "^" + nxt2.strip(), 3  # exposant resté seul sur sa ligne
            elif nxt2 is not None and is_math_line(nxt2, 6) and nxt2.strip()[:1] not in ".,;":
                out.append(cur)
                i += 1
                continue
            head, tail = split_math_tail(m.group(1))
            out.append((head + " " if head else "") + f"${tex(tail)} \\dfrac{{{tex(m.group(2))}}}{{{tex(den)}}}$")
            i += skip
            continue
        out.append(cur)
        i += 1
    return out


def mark_options(lines):
    """propositions de QCM : lignes consécutives qui commencent pareil
    ("converge uniformément sur ...") -> puces"""
    key = [" ".join(l.split()[:2]).lower()
           if len(l.split()) >= 3 and len(l) < 90 and re.match(r"[A-Za-zÀ-ÿ]{3,}\s", l) else None
           for l in lines]
    out = []
    for j, l in enumerate(lines):
        same = key[j] and ((j > 0 and key[j - 1] == key[j]) or (j + 1 < len(lines) and key[j + 1] == key[j]))
        out.append("- " + l if same and not BULLET_RE.match(l) and not LIST_RE.match(l) else l)
    return out


def glue(prev, frag):
    if not prev:
        return frag
    if frag[:1] in ".,;:)]}" or prev[-1:] in "({":
        return prev + frag
    return prev + " " + frag


def reflow(text):
    text = text.replace("̸=", "≠").replace("̸∼", "≁").replace("̸∈", "∉").replace("\u0338", "").replace("$", "＄")
    lines = [l.strip() for l in text.split("\n")]
    # numéros de page : seuls sur leur ligne, en fin de passage ou entre deux phrases
    kept = []
    for j, l in enumerate(lines):
        if PAGE_NUM_RE.match(l):
            prev = next((x for x in reversed(kept) if x), "")
            after = next((x for x in lines[j + 1:] if x), "")
            if not after or (prev.endswith((".", "?", "!", ":")) and (not after or after[:1].isupper())):
                continue
        kept.append(l)
    split = []
    for l in kept:  # mise en page sur deux colonnes : "n(n + 1) 2. un ="
        split += [x.strip() for x in INLINE_ITEM_RE.split(l)] if l else [l]
    lines = rebuild_fractions(big_sums(repair_lines([l for l in split if l != ""])))
    lines = mark_options(lines)

    paras, cur, cur_is_list = [], "", False
    prev_line = ""

    def flush():
        nonlocal cur, cur_is_list
        if cur:
            paras.append(("li" if cur_is_list else "p", cur))
        cur, cur_is_list = "", False

    for l in lines:
        pl, prev_line = prev_line, l
        h = HEADING_RE.match(l)
        if h:
            flush()
            title = l[:h.start(2)].rstrip(" .:") if h.group(2) else l.rstrip(" .:")
            paras.append(("h", title))
            if h.group(2):
                cur = h.group(2)
            continue
        if LONE_MARK_RE.match(l):
            flush()
            cur, cur_is_list = l[:-1] + ".", True
            continue
        lm = LIST_RE.match(l)
        bm = BULLET_RE.match(l)
        if lm and (lm.group(1) is None or int(lm.group(1)) <= 30):
            flush()
            num = lm.group(1) or lm.group(2)
            cur, cur_is_list = (f"{num}. " if lm.group(1) else f"({num}) ") + lm.group(3), True
            continue
        if bm or ARROW_START_RE.match(l) or BLOCK_START_RE.match(l):
            flush()
            if bm:
                cur, cur_is_list = "- " + bm.group(2), True
            else:
                cur = l
            continue
        # fin de paragraphe probable : ligne précédente courte terminée par un point
        if cur and not cur_is_list and pl.endswith((".", ":")) and len(pl) < 55 \
                and l[:1].isupper():
            flush()
        cur = glue(cur, l)
    flush()

    out, prev_kind = [], None
    for kind, t in paras:
        t = inline_math(t)
        if kind == "h":
            out.append(f"\n#### {t}\n")
        elif kind == "li":
            if t[0].isdigit() or t.startswith("- "):
                out.append(("" if prev_kind == "li" else "\n") + t)
                prev_kind = kind
                continue
            out.append("\n" + t + "\n")  # (a) : paragraphe simple
        else:
            out.append("\n" + t + "\n")
        prev_kind = kind
    md = "\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", md).strip()


KNOWN_CMDS = set("""sqrt dfrac sum prod lim limits to infty in mathbb le ge sim approx neq partial times cdot
Leftrightarrow Rightarrow sin cos tan exp ln log arctan surd alpha beta gamma delta varepsilon theta
lambda mu pi rho sigma tau varphi psi omega Omega""".split())


def valid_tex(t):
    depth = 0
    for ch in t:
        depth += ch == "{"
        depth -= ch == "}"
        if depth < 0:
            return False
    if depth or re.search(r"[\^_]\s*$|[\^_]\s*[}^_]", t):
        return False
    if any(c not in KNOWN_CMDS for c in re.findall(r"\\([A-Za-z]+)", t)):
        return False
    for m in re.finditer(r"\\dfrac", t):  # deux groupes obligatoires
        if not re.match(r"\\dfrac\s*\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}\s*\{", t[m.start():]):
            return False
    return True


UNTEX = {v.strip(): k for k, v in GREEK.items() if v.startswith("\\")}
UNTEX.update({r"\mathbb{N}": "ℕ", r"\mathbb{Z}": "ℤ", r"\mathbb{R}": "ℝ", r"\mathbb{C}": "ℂ",
              r"\mathbb{Q}": "ℚ", r"\sum": "∑", r"\prod": "∏", r"\lim": "lim", r"\limits": ""})


def detex(t):
    """repli lisible quand la formule reconstruite n'est pas du LaTeX valide"""
    t = re.sub(r"\\dfrac\s*\{([^{}]*)\}\s*\{([^{}]*)\}", r"(\1)/(\2)", t)
    t = re.sub(r"\\mathbb\{(\w)\}", lambda m: UNTEX.get(m.group(0), m.group(1)), t)
    t = re.sub(r"\\([A-Za-z]+)\s?", lambda m: UNTEX.get("\\" + m.group(1), m.group(1)), t)
    return t.replace("{", "").replace("}", "")


def sanitize(md):
    return re.sub(r"\$([^$]+)\$", lambda m: m.group(0) if valid_tex(m.group(1)) else detex(m.group(1)), md)


def to_md_blocks(text):
    return [{"type": "md", "text": sanitize(reflow(text))}]
