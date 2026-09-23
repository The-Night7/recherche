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
    if not balanced(s) or re.search(r"=|→|⇐|⇒|⇔|\blim\b|\(\d+\.\d+\)|[\[\]]", s) \
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
    "⇔": r"\Leftrightarrow ", "⇒": r"\Rightarrow ", "√": r"\surd ", "!": "!", "∗": "^*",
}
SETS = {"N": r"\mathbb{N}", "Z": r"\mathbb{Z}", "R": r"\mathbb{R}", "C": r"\mathbb{C}", "Q": r"\mathbb{Q}"}


SUP_CHARS = {"⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5", "⁶": "6", "⁷": "7",
             "⁸": "8", "⁹": "9", "ⁿ": "n", "ᵖ": "p", "⁺": "+", "⁻": "-"}
SUB_CHARS = {"₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4", "ₙ": "n", "ₖ": "k", "ₚ": "p",
             "ᵢ": "i", "ⱼ": "j", "ₘ": "m", "ₗ": "l"}


def tex(s):
    s = s.strip()
    s = re.sub("[" + "".join(SUP_CHARS) + "]+", lambda m: "^{" + "".join(SUP_CHARS[c] for c in m.group(0)) + "}", s)
    s = re.sub("[" + "".join(SUB_CHARS) + "]+", lambda m: "_{" + "".join(SUB_CHARS[c] for c in m.group(0)) + "}", s)
    s = re.sub(r"\b(sin|cos|tan|exp|ln|log|arctan)\b", r"\\\1 ", s)
    s = re.sub(r"(?<![A-Za-z\\])([a-zA-Z])([nkpij])(?![A-Za-z])", r"\1_\2", s)  # un -> u_n
    s = "".join(GREEK.get(ch, ch) for ch in s)
    return s


def frac(num, den):
    return f"$\\dfrac{{{tex(num)}}}{{{tex(den)}}}$"


SUM_RE = re.compile(r"([∑∏])\s*([a-z])\s*(∈\s*[NZRC]\*?|[≥>]\s*\d+|=\s*\d+)\s+([a-zA-Z])\2?(\([^()]{0,12}\))?(?![A-Za-z(])")
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
SET_RE = re.compile(r"(?<![\w$\\{])([RNZ])(?![\w'’])(\s*∗)?(\s*\+(?![\w∞(]))?")
SETS_U = {"R": "ℝ", "N": "ℕ", "Z": "ℤ"}
SUBS_U = {"n": "ₙ", "k": "ₖ"}
MERGE_R = re.compile(r"\$([^$]+)\$\s*([=∼≠<>≤≥⇔])\s*(\$[^$]+\$|[+−-]?\d+(?:[.,]\d+)?(?![\w])|[+−-]?∞)")
MERGE_EQ = re.compile(r"\$([^$]+)\$\s*([=∼≠<>≤≥⇔])\s*\$([^$]+)\$")


def texify_rel(op):
    return GREEK.get(op, op).strip() if op not in "=<>" else op


def merge_math(p):
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
        p = SET_RE.sub(lambda m: SETS_U[m.group(1)] + ("∗" if m.group(2) else "") + ("₊" if m.group(3) else ""), p)
        parts[i] = p
    return merge_math("".join(parts))


# ---------- recollage des lignes ----------
BIG_SUM_RE = re.compile(r"^([+−-]?)\s*X\s*([+−-]?∞|[a-zA-Z0-9+−-]{1,4})$")
SUM_LOW_RE = re.compile(r"^([a-z])\s*=\s*(\S{1,6})$")
MATH_TAIL_TOKEN_RE = re.compile(r"^(?:[=<>≤≥∼≈⇔+−\-×·]|[a-zA-Z][nk]?(?:\(\w{1,3}\))?|\d+|[+−-]?∞)$")


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
    text = text.replace("̸=", "≠").replace("$", "＄")
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
    lines = rebuild_fractions(big_sums([l for l in split if l != ""]))
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


KNOWN_CMDS = set("""dfrac sum prod lim limits to infty in mathbb le ge sim approx neq partial times cdot
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
