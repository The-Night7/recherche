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
  - les calculs sont séparés de la prose, avec les égalités alignées ;
  - les paragraphes et calculs restent dans leur question numérotée.
C'est une heuristique : le texte indexé (chunks.json) n'est pas modifié.
"""
import re

HEADING_RE = re.compile(
    r"^(Exercice|Ex\.|R[ée]ponse|Question|Partie|Probl[èe]me)\s*\d+[a-z]?\b\s*[.:]?\s*(.*)$", re.I
)
BLOCK_START_RE = re.compile(
    r"^(Remarques?|D[ée]finition|Th[ée]or[èe]me|Proposition|Propri[ée]t[ée]|Lemme|Corollaire|"
    r"D[ée]monstration|Preuve|Exemples?|G[ée]n[ée]ralisation|Indication|Rappel|Consignes?|"
    r"Attention|Notation|M[ée]thode|Conclusion|Solution)\b"
)
LIST_RE = re.compile(r"^(?:((?:0|[1-9]\d?))[.)]|\(?([a-h]|i{1,3}|iv|v|vi{0,3})\))(?:\s+(\S.*))?$")
BULLET_RE = re.compile(r"^([—–•▶►]|-(?=\s))\s*(.*)$")
ARROW_START_RE = re.compile(r"^[⇒⇐]\s")
INLINE_ITEM_RE = re.compile(r"(?<=\S)\s+(?=\d{1,2}\.\s+(?:[a-zA-Z]{1,2}\w?(?:\(\w{1,3}\))?\s*=|∑))")

MATH_FUNCTIONS = {"sin", "cos", "tan", "exp", "ln", "log", "sinh", "cosh", "tanh",
                  "arctan", "arcsin", "arccos", "sh", "ch", "th", "cotan", "det"}
MATH_WORDS = MATH_FUNCTIONS | {"lim", "sup", "inf", "max", "min", "si", "dt", "dx"}
FUNCTION_TEX = {name: name for name in MATH_FUNCTIONS} | {"sh": "sinh", "ch": "cosh", "th": "tanh", "cotan": "cot"}
OPERATOR_END_RE = re.compile(r"(?:[=<>≤≥∼≈⇔⇒+−\-×·(,]|:=|\bet)\s*$")


def spaced_functions(s):
    """Séparer les produits/logarithmes compactés par l'extraction PDF.

    Une seule lettre peut précéder ln : on ne coupe pas les mots de prose.
    Les puissances restent attachées à la fonction jusqu'à tex().
    """
    s = re.sub(r"(?<![A-Za-zÀ-ÿ\\])([a-z])ln(?=\s|[2-9(])", r"\1 ln", s)
    return re.sub(r"\bln([2-9]?)(?=[a-z]\b)", r"ln\1 ", s)


def balanced(s):
    d = 0
    for ch in s:
        d += ch in "(" 
        d -= ch in ")"
        if d < 0:
            return False
    return d == 0


def is_math_line(s, maxlen=20):
    s = spaced_functions(s.strip())
    if HEADING_RE.match(s) or LIST_RE.match(s):
        return False
    if not balanced(s) or re.search(r"[=→≠∼≤≥<>∑∏∫]|⇐|⇒|⇔|\blim\b|\(\d+\.\d+\)|[\[\]]|[a-z]?X|\bZ\s+", s) \
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
    "∑": r"\sum ", "∏": r"\prod ", "∫": r"\int ",
}
SETS = {"N": r"\mathbb{N}", "Z": r"\mathbb{Z}", "R": r"\mathbb{R}", "C": r"\mathbb{C}", "Q": r"\mathbb{Q}"}


SUP_CHARS = {"⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5", "⁶": "6", "⁷": "7",
             "⁸": "8", "⁹": "9", "ⁿ": "n", "ᵖ": "p", "⁺": "+", "⁻": "-"}
SUP_CHARS["ᐟ"] = "/"
SUB_CHARS = {"₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4", "ₙ": "n", "ₖ": "k", "ₚ": "p",
             "ᵢ": "i", "ⱼ": "j", "ₘ": "m", "ₗ": "l"}


def tex(s):
    s = spaced_functions(s.strip())
    # Les fragments reçus ici sont du texte PDF, pas des commandes LaTeX.
    s = s.replace("\\", r"\setminus ")
    s = re.sub(r"[{}#%&]", lambda m: "\\" + m.group(0), s)
    s = re.sub(r"√\s*(\([^()]*\)|[A-Za-z0-9]+)", lambda m: r"\sqrt{" + m.group(1) + "}", s)
    s = re.sub("[" + "".join(SUP_CHARS) + "]+", lambda m: "^{" + "".join(SUP_CHARS[c] for c in m.group(0)) + "}", s)
    s = re.sub("[" + "".join(SUB_CHARS) + "]+", lambda m: "_{" + "".join(SUB_CHARS[c] for c in m.group(0)) + "}", s)
    functions = "|".join(sorted(MATH_FUNCTIONS, key=len, reverse=True))
    s = re.sub(r"\b(" + functions + r")(\d+)(?=\(|\s+[a-z(])",
               lambda m: "\\" + FUNCTION_TEX[m.group(1)] + "^{" + m.group(2) + "}", s)
    s = re.sub(r"(?<![\\\w])(" + functions + r")\b", lambda m: "\\" + FUNCTION_TEX[m.group(1)] + " ", s)
    s = re.sub(r"(?<![A-Za-z\\])([a-zA-Z])([nkpij])(?![A-Za-z])", r"\1_\2", s)  # un -> u_n
    s = "".join(GREEK.get(ch, ch) for ch in s)
    return s


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
        p = FN_CALL_RE.sub(lambda m: m.group(0) if m.group(1) + m.group(2) in MATH_WORDS
                           else f"${m.group(1)}_{m.group(2)}({m.group(3)})$", p)
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
SUM_LOW_RE = re.compile(r"^([a-z](?:0{1,3}|⁰{1,3}|'{1,3})?)\s*=\s*(\S{1,6})$")


def big_sums(lines):
    out, i = [], 0
    while i < len(lines):
        # Le signe somme peut être collé à la formule précédente, et sa
        # borne supérieure apparaît soit après X, soit de part et d'autre.
        m = re.search(r"(?:X([+−-]?∞|[a-zA-Z0-9+−-]{1,4})|([a-z])X([+−-]\d+)|([a-z]?)X|∑)$", lines[i])
        if m:
            upper = m.group(1) or ((m.group(2) or "") + (m.group(3) or ""))
            low_pos = i + 1
            if not upper and low_pos < len(lines) and re.fullmatch(r"[+−-]?∞|[a-zA-Z0-9+−-]{1,4}", lines[low_pos]):
                upper = (m.group(4) or "") + lines[low_pos]
                low_pos += 1
            low = SUM_LOW_RE.match(lines[low_pos]) if low_pos < len(lines) else None
            if upper and low:
                prefix = lines[i][:m.start()].strip()
                if prefix:
                    out.append(prefix)
                out.append(f"$\\sum_{{{tex(low.group(1))}={tex(low.group(2))}}}^{{{tex(upper)}}}$")
                i = low_pos + 1
                continue
        out.append(lines[i])
        i += 1
    return out


SUP_OF = {"0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸",
          "9": "⁹", "n": "ⁿ", "−": "⁻", "-": "⁻", "+": "⁺", "x": "ˣ", "k": "ᵏ", "p": "ᵖ", "t": "ᵗ"}
UNSUP = {v: k for k, v in SUP_OF.items() if k != "-"}


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
        if re.fullmatch(r"ln[2-9]", l) and re.fullmatch(r"[a-z]", nxt):
            out.append(l + " " + nxt)
            i += 2
            continue
        if l == "lim" and re.fullmatch(r"[a-z]\s*→\s*(?:[+−-]?∞|[+−-]?\d+[+−-]?)", nxt):
            out.append(l + " " + nxt)
            i += 2
            continue
        # "ln 1 + e" ... ")" : parenthèse ouvrante perdue avec la grande parenthèse
        if re.search(r"\bln \d", l) and ")" in lines[i + 1:i + 4]:
            l = re.sub(r"\bln (\d)", r"ln(\1", l)
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
        if re.search(r"(?:^|[\s(+−-]|\d)e$", l) and nxt == "1" and re.match(r"^n\b", nxt2):
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


def glue(prev, frag):
    if not prev:
        return frag
    if frag[:1] in ".,;:)]}" or prev[-1:] in "({":
        return prev + frag
    return prev + " " + frag


def math_only(line):
    """Reconnaître un calcul entier, sans envoyer la prose dans KaTeX."""
    if HEADING_RE.match(line) or LIST_RE.match(line):
        return False
    plain = spaced_functions(re.sub(r"\$[^$]+\$|\\[a-zA-Z]+", "", line))
    plain = LIM_RE.sub("", plain)
    if re.search(r"\b(?:en|on|de|le|la|les|est|et|qui|donc|où|ou|il|du|au|se|ce)\b", plain, re.I):
        return False
    return bool(line.strip()) and all(
        w.lower() in MATH_WORDS for w in re.findall(r"[A-Za-zÀ-ÿ]{3,}", plain)
    )


def equality_at(text):
    """Position du signe égal hors des indices et arguments LaTeX."""
    depth = 0
    for i, char in enumerate(text):
        depth += char == "{"
        depth -= char == "}"
        if char == "=" and depth == 0:
            return i
    return -1


def restore_large_parentheses(text):
    """Restituer les grandes parenthèses cmex extraites comme espace / !.

    On travaille avant strip(), qui effaçait le glyphe ouvrant. Les paires
    restent confinées à un calcul ; un factoriel ordinaire n'est pas touché.
    """
    def repair(group):
        # Un espace isolé ou devant une somme est le glyphe ouvrant cmex.
        candidates = {i for i, line in enumerate(group)
                      if line == " " or re.match(r"^ (?=∑|[a-z]?X|ln\()", line)}
        if not candidates or not any("!" in line for line in group):
            return group
        pending, result, repaired = [], [], set()
        for i, line in enumerate(group):
            if i in candidates:
                pending.append(i)
            stripped = line.strip()
            # Le ! de fermeture peut être seul ou collé à une fin de somme.
            # n!, (n + 1)! et les autres factorielles restent des factorielles.
            match = re.search(r"!(?=$|[+−-])", stripped)
            if pending and match and (stripped == "!" or (
                    re.search(r"\s[+−-]\s", stripped[:match.start()])
                    and not stripped[:match.start()].rstrip().endswith(")"))):
                opener = pending.pop()
                repaired.add(opener)
                line = line[:line.index("!")] + ")" + line[line.index("!") + 1:]
            result.append(line)
        for i in repaired:
            result[i] = "(" + result[i][1:]
        return result

    out, group = [], []
    for line in text.split("\n"):
        if line == " " or (line.strip() and math_only(line.strip())):
            group.append(line)
        else:
            out.extend(repair(group))
            group = []
            out.append(line)
    out.extend(repair(group))
    return "\n".join(out)


def wrap_equation(row, width=50):
    """Couper une longue égalité entre ses termes, jamais dans une fraction."""
    brace_depth = paren_depth = 0
    cuts = []
    for i, char in enumerate(row):
        if i and row[i - 1] == "\\":
            continue
        brace_depth += char == "{"
        brace_depth -= char == "}"
        paren_depth += char in "(["
        paren_depth -= char in ")]"
        if char in "+-" and brace_depth == paren_depth == 0 and i and row[i - 1].isspace():
            cuts.append(i)
    def measure(part):
        return len(re.sub(r"\\[A-Za-z]+|[{}]", "", part))
    parts, start = [], 0
    for j, cut in enumerate(cuts):
        end = cuts[j + 1] if j + 1 < len(cuts) else len(row)
        if measure(row[start:end]) > width and measure(row[start:cut]) >= width // 3:
            parts.append(row[start:cut].strip())
            start = cut
    parts.append(row[start:].strip())
    return parts


BOUND = r"[+−-]?(?:∞|[A-Za-z0-9]+(?:\s*[+−-]\s*\d+)?)"


def bounded_operators(lines):
    """Protéger les bornes avant toute tentative de reconstruire une fraction."""
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        following = lines[i + 1] if i + 1 < len(lines) else ""
        integral = re.search(r"(?<!\w)([Z∫])\s+(" + BOUND + r")$", line)
        # Le Z seul est aussi une variable/un ensemble. Exiger un différentiel
        # dans ce même calcul pour interpréter le glyphe PDF comme une intégrale.
        body = []
        for part in lines[i + 2:i + 12]:
            body.append(part)
            if re.search(r"[=≤≥]|\bZ\s", part):
                break
        if integral and re.fullmatch(BOUND, following) and (
                integral.group(1) == "∫" or re.search(r"\bd[txu]\b", " ".join(body))):
            prefix = line[:integral.start()].strip()
            if prefix:
                out.append(prefix)
            out.append(r"$\int_{" + tex(following) + "}^{" + tex(integral.group(2)) + "}$")
            i += 2
            continue
        # [F(t)] / b / a, ou [F(t)]b / a : les bornes ne sont pas b/a.
        evaluation = re.search(r"(\[[^\[\],]+\])\s*(" + BOUND + r")?$", line)
        if evaluation:
            upper = evaluation.group(2) or following
            lower_pos = i + (1 if evaluation.group(2) else 2)
            lower = re.match(r"^(" + BOUND + r")(\s*[=≤≥].*)?$", lines[lower_pos]) if lower_pos < len(lines) else None
            if re.fullmatch(BOUND, upper) and lower:
                prefix = line[:evaluation.start()].strip()
                if prefix:
                    out.append(prefix)
                out.append("$" + tex(evaluation.group(1)) + "_{" + tex(lower.group(1)) + "}^{" + tex(upper) + "}$")
                if lower.group(2):
                    out.append(lower.group(2).strip())
                i = lower_pos + 1
                continue
        # La primitive peut elle-même être une fraction entre crochets.
        if line == "[":
            end = next((j for j in range(i + 1, min(i + 9, len(lines))) if lines[j].startswith("]")), None)
            if end is not None:
                upper = lines[end][1:].strip()
                lower = lines[end + 1] if end + 1 < len(lines) else ""
                if re.fullmatch(BOUND, upper) and re.fullmatch(BOUND, lower):
                    inside = display_math(lines[i + 1:end])
                    out.append("$[" + inside + "]_{" + tex(lower) + "}^{" + tex(upper) + "}$")
                    i = end + 2
                    continue
        out.append(line)
        i += 1
    return out


def prepare_math(lines):
    prepared = []
    for line in bounded_operators(lines):
        # Les sommes restaurées à l'import peuvent partager la ligne du terme.
        line = re.sub(r"∑(_\{[^{}]+\})(\^\{[^{}]+\})?",
                      lambda m: "$\\sum" + m.group(1) + (m.group(2) or "") + "$", line)
        line = SUM_BARE_RE.sub(lambda m: "$\\" + ("sum" if m.group(1) == "∑" else "prod")
                              + "_{" + m.group(2) + sub_index(m.group(3)) + "}$", line)
        prepared.extend(part.strip() for part in re.split(r"(\$[^$]+\$)", line) if part.strip())
    return prepared


def readable_integral_steps(lines):
    """Replier seulement les étapes où la notation de dérivation a été perdue.

    On conserve les membres lisibles d'une chaîne d'égalités, sans deviner
    les primes ou fabriquer une division par zéro à partir d'un glyphe.
    Le calcul extrait complet reste disponible à côté du calcul abrégé.
    """
    steps, current = [], []
    for line in prepare_math(lines):
        if line.startswith("$"):
            current.append(line)
            continue
        parts = re.split(r"(=)", line)
        for part in parts:
            if part == "=" and current:
                steps.append(current)
                current = []
            if part.strip():
                current.append(part.strip())
    if current:
        steps.append(current)
    kept, omitted, uncertain = [], False, False
    for step in steps:
        joined = " ".join(step)
        damaged = False
        if r"\int" in joined and re.search(r"\bd[txu]\b", joined):
            # (ln t) / t / ln t ou (ln t) / 0 / ln² t : le caractère
            # entre les deux fonctions peut être une prime mal extraite.
            damaged = any(re.search(r"\b(?:ln|log|sin|cos)\b", part) and part.endswith(")")
                          and i + 2 < len(step) and step[i + 1] in ("0", "t", "x")
                          and re.match(r"(?:ln|log|sin|cos)", step[i + 2])
                          for i, part in enumerate(step))
            damaged |= bool(re.search(r"\)[0tx]\s+d[txu]\b", joined))
        # Une primitive qui suit une dérivation illisible ne permet pas
        # de rétablir avec certitude le signe ou l'exposant manquant.
        evaluation = uncertain and any(part.startswith("$[") for part in step)
        if damaged or evaluation:
            if not kept:
                return [], True
            omitted = uncertain = True
        else:
            kept.extend(step)
            uncertain = False
    return (kept, True) if omitted else (lines, False)


def display_math(lines):
    """Restituer les fractions empilées dans un calcul isolé de la prose.

    On garde les frontières des lignes jusqu'à la reconstruction : elles
    distinguent un numérateur de son dénominateur. Les indices des sommes
    sont déjà protégés par big_sums().
    """
    fragments = []
    for line in prepare_math(lines):
        if line.startswith("$") and line.endswith("$"):
            fragments.append(line)
            continue
        # Séparer une relation de la fraction qui la suit ("un = 1" / "n").
        relation = re.match(r"^(.*[=∼≤≥<>])\s*(.*)$", line)
        if relation:
            left = relation.group(1)[:-1].strip()
            if re.search(r"\bd[txu]$", left) and any(r"\int" in part for part in fragments):
                fragments.extend([left, relation.group(1)[-1]])
            elif fragments and is_math_line(fragments[-1], 28) and is_math_line(left, 32) \
                    and "$" not in fragments[-1] and not OPERATOR_END_RE.search(fragments[-1]):
                fragments.extend([left, relation.group(1)[-1]])
            else:
                fragments.append(relation.group(1).strip())
            line = relation.group(2).strip()
        # Une grande parenthèse peut être sur la ligne du numérateur.
        if line.startswith("(") and not balanced(line):
            fragments.append("(")
            line = line[1:].strip()
        if line:
            # Le signe après un dénominateur appartient au terme suivant.
            tail = re.match(r"^(.+?)\s+([+−-])$", line)
            if tail and is_math_line(tail.group(1), 32):
                fragments.extend(tail.groups())
            else:
                fragments.append(line)

    out, i = [], 0
    while i < len(fragments):
        cur = fragments[i]
        nxt = fragments[i + 1] if i + 1 < len(fragments) else ""
        # Extraire seulement les parenthèses fermantes excédentaires du dénominateur.
        den, closers = nxt, ""
        while den.endswith(")") and den.count(")") > den.count("("):
            den, closers = den[:-1].rstrip(), ")" + closers
        if "$" not in cur + den and is_math_line(cur, 28) and is_math_line(den, 32) \
                and (not re.fullmatch(r"d[txu]", den) or re.fullmatch(r"d[A-Za-z]", cur)) \
                and not OPERATOR_END_RE.search(cur) and not OPERATOR_END_RE.search(den):
            value = r"\dfrac{" + tex(cur) + "}{" + tex(den) + "}"
            i += 2
            # (1/2)/n, issu de trois niveaux empilés dans le PDF.
            third = fragments[i] if i < len(fragments) else ""
            third_den = third.rstrip(")").strip()
            if not closers and cur.isdigit() and den.isdigit() and re.match(r"^[a-z]\b", third_den) \
                    and is_math_line(third_den, 20) and not OPERATOR_END_RE.search(third_den):
                factor = "(" + tex(third_den) + ")" if re.search(r"[+−-]", third_den) else tex(third_den)
                value = r"\dfrac{" + tex(cur) + "}{" + tex(den) + factor + "}"
                closers = third[len(third_den):]
                i += 1
            out.append(value + closers)
            continue
        converted = inline_math(cur)
        parts = re.split(r"(\$[^$]+\$)", converted)
        out.append("".join(p[1:-1] if j % 2 else tex(p) for j, p in enumerate(parts)))
        i += 1

    # Une égalité par ligne : les longues chaînes de calcul ne repoussent plus
    # l'explication jusqu'au bord de la carte.
    rows, current = [], ""
    for part in out:
        if part.startswith("=") and current and not current.endswith(("=", "+", "-")):
            rows.append(current)
            current = part
        elif equality_at(part) >= 0 and current and not current.endswith(("=", "+", "-", "(")) \
                and not part.startswith("\\sum"):
            # Le symbole de somme immédiatement précédent appartient au membre gauche.
            tail = re.search(r"\\sum_\{[^{}]+\}\^\{[^{}]+\}$", current)
            if tail and "\\lim" in current[:tail.start()]:
                current = glue(current, part)
            elif tail:
                if current[:tail.start()].strip():
                    rows.append(current[:tail.start()].strip())
                current = current[tail.start():] + " " + part
            else:
                rows.append(current)
                current = part
        else:
            current = glue(current, part)
    if current:
        rows.append(current)
    rows = [part for row in rows for part in wrap_equation(row)]
    if len(rows) == 1:
        return rows[0]
    aligned = []
    for row in rows:
        pos = equality_at(row)
        aligned.append(row[:pos] + "&" + row[pos:] if pos >= 0 else "&" + row)
    return "\\begin{aligned}\n" + " \\\\\n".join(aligned) + "\n\\end{aligned}"


def ambiguous_formula(lines):
    """Repérer les extractions dont la géométrie manque pour choisir le LaTeX.

    Un bloc ambigu reste entier et conserve ses lignes source. La validité
    syntaxique d'un LaTeX inventé ne prouve pas que la formule est correcte.
    """
    if not balanced("".join(lines)) or "!" in lines:
        return True
    for i, line in enumerate(lines[:-1]):
        following = lines[i + 1]
        if line == "√" and re.search(r"[+−-]", following):
            return True  # La longueur du trait de racine a disparu.
        if re.search(r"[a-z]$", line) and re.fullmatch(r"\d+/\d+", following):
            return True  # Puissance fractionnaire ou fraction indépendante ?
    # Une limite suivie d'une fraction sur deux lignes est exploitable ;
    # plusieurs niveaux supplémentaires ne donnent plus sa barre de fraction.
    limit = LIM_RE.fullmatch(lines[0])
    body = lines[1:]
    if lines[0] == "lim" and len(lines) > 1:
        limit = LIM_RE.fullmatch("lim " + lines[1])
        body = lines[2:]
    if limit and not limit.group(3) and not limit.group(4) and not any("=" in line or "∑" in line for line in body):
        if len(body) > 2:
            return True
        if len(body) == 2 and not all(is_math_line(part, 500) for part in body):
            return True
    return False


def source_formula(lines, language="pdf"):
    """Bloc littéral : aucune formule, liste ou balise n'est interprétée dedans."""
    width = max([2] + [len(m.group()) for line in lines for m in re.finditer(r"`+", line)]) + 1
    fence = "`" * width
    return "\n".join([fence + language, *lines, fence])


def reflow(text):
    text = restore_large_parentheses(text)
    text = text.replace("̸=", "≠").replace("̸∼", "≁").replace("̸∈", "∉").replace("\u0338", "").replace("$", "＄")
    # La police PDF code parfois les primes par des zéros. Ne les restituer
    # que pour un indice explicitement introduit par un changement de variable.
    shifted = re.findall(r"(?:on pose|En posant)\s+([a-z])\s*([0⁰]{1,3})\s*=\s*\1\s*[+−-]\s*\d", text)
    for variable, zeros in sorted(set(shifted), key=lambda x: -len(x[1])):
        text = re.sub(r"\b" + variable + r"\s*[0⁰]{" + str(len(zeros)) + r"}(?![\w⁰])",
                      variable + "'" * len(zeros), text)
    lines = [l.strip() for l in text.split("\n")]
    split = []
    for l in lines:  # mise en page sur deux colonnes : "n(n + 1) 2. un ="
        split += [x.strip() for x in INLINE_ITEM_RE.split(l)] if l else [l]
    # Une équation peut commencer sur la même ligne qu'une fin d'explication.
    split = [part for line in split for part in re.split(r"(?<=[.!?])\s+(?=∑|[a-z]?X|[a-z][nk]\s*=)", line)]
    mixed = []
    for line in split:
        parts = re.split(r"\s+(?=(?:qui|avec|où|car|donc)\b|,\s*il\b)", line, maxsplit=1)
        mixed.extend(parts if len(parts) == 2 and math_only(parts[0]) else [line])
    split = mixed
    lines = [l for l in split if l]

    out, prose, formula = [], "", []
    embedded_formula = False
    indent = ""

    def flush_prose():
        nonlocal prose
        if prose:
            out.append(indent + inline_math(prose))
            prose = ""

    def flush_formula(inline=False):
        nonlocal prose, embedded_formula
        if formula:
            embedded = embedded_formula
            embedded_formula = False
            # Une parenthèse commencée dans la phrase n'est pas un nouveau
            # calcul : garder ce fragment avec sa prose, sans encadré isolé.
            if (prose or inline) and not balanced("".join(formula)) \
                    and not any(re.search(r"[=≠≤≥∼∑∏]|\blim", part) for part in formula):
                prose = glue(prose, inline_math(" ".join(formula)))
                formula.clear()
                return
            if ambiguous_formula(formula):
                flush_prose()
                out.append("\n".join(indent + line for line in source_formula(formula).split("\n")))
                formula.clear()
                return
            # Réparer seulement ce calcul : aucune opération ne peut consommer
            # le titre ou le repère de la question suivante.
            repaired = big_sums(repair_lines(formula.copy()))
            readable, shortened = readable_integral_steps(repaired)
            if shortened and not readable:
                flush_prose()
                out.append("\n".join(indent + line for line in source_formula(formula).split("\n")))
                formula.clear()
                return
            value = display_math(readable)
            scalar = len(formula) == 1 and re.fullmatch(r"[\wℝℕℤℂℚ⁰-⁹¹²³ⁿᵖ]+", formula[0])
            inline_expression = not any(command in value for command in (r"\begin", r"\sum", r"\prod", r"\lim"))
            embedded_expression = embedded and not any(command in value for command in (r"\begin", r"\int", r"\lim"))
            if embedded_expression or (inline and inline_expression) or (scalar and prose):
                prose = glue(prose, "$" + value + "$")
            else:
                flush_prose()
                out.append("\n".join(indent + l for l in ("$$\n" + value + "\n$$").split("\n")))
            if shortened:
                out.append("\n".join(indent + line for line in source_formula(formula, "pdf-steps").split("\n")))
            formula.clear()

    for line_number, line in enumerate(lines):
        heading = HEADING_RE.match(line)
        if heading:
            flush_formula()
            flush_prose()
            indent = ""
            title = line[:heading.start(2)].rstrip(" .:") if heading.group(2) else line.rstrip(" .:")
            title = re.sub(r"^Ex\.\s*", "Exercice ", title, flags=re.I)
            out.append("#### " + title)
            prose = heading.group(2)
            continue
        item = LIST_RE.match(line)
        bullet = BULLET_RE.match(line)
        if item:
            flush_formula()
            flush_prose()
            num = item.group(1) or item.group(2)
            prefix = num + "." if num.isdigit() else num + ")" if len(num) == 1 else "- **(" + num + ")**"
            out.append(prefix)
            indent = " " * (len(num) + 2 if len(num) == 1 or num.isdigit() else 2)
            line = item.group(3) or ""
        elif bullet:
            flush_formula()
            flush_prose()
            # Les puces d'une correction restent dans la question en cours.
            out.append(indent + "- " + inline_math(bullet.group(2)))
            continue
        if not line:
            continue
        if math_only(line):
            formula.append(line)
            continue
        flush_formula(inline=bool(re.match(r"^(?:qui |où |avec |,|\.)", line)))
        if prose and (BLOCK_START_RE.match(line) or ARROW_START_RE.match(line)
                      or re.match(r"^(?:On |En |Dans |Les .*sommes|Car |Donc |Ainsi )", line)):
            flush_prose()
        # Une fraction commence parfois dans la prose et continue à la ligne :
        # « La fonction f(t) = 1 » / « t ln t » / « est décroissante… ».
        # Même cas pour « la série ∑n≥2 » / « 1 » / « n ln n ».
        attached = re.search(r"(?<!\w)(?:[a-zA-Z]\([^()]+\)\s*=\s*.+|[∑∏].*)$", line)
        if attached and attached.start() and math_only(attached.group()) \
                and line_number + 1 < len(lines) and math_only(lines[line_number + 1]):
            continuation = [attached.group()]
            for following in lines[line_number + 1:]:
                if not math_only(following):
                    break
                continuation.append(following)
            # Si la parenthèse ferme dans la prose suivante, garder le chemin
            # de recollage existant plutôt que créer un calcul tronqué.
            if balanced("".join(continuation)):
                prose = glue(prose, line[:attached.start()].strip())
                formula.append(attached.group())
                embedded_formula = True
                continue
        # Les explications successives étaient souvent dans la même ligne PDF.
        phrases = re.split(r"(?<=[.!?])\s+(?=On |Donc |Ainsi |En posant )", line)
        for i, phrase in enumerate(phrases):
            if i:
                flush_prose()
            prose = glue(prose, phrase)
    flush_formula()
    flush_prose()
    return "\n\n".join(out).strip()


KNOWN_CMDS = set(FUNCTION_TEX.values()) | set("""begin end setminus sqrt dfrac sum prod int lim limits to infty in mathbb le ge sim approx neq partial times cdot
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
    return re.sub(r"(\$\$|\$)([^$]+)\1", lambda m: m.group(0) if valid_tex(m.group(2)) else detex(m.group(2)), md)


def to_md_blocks(text):
    return [{"type": "md", "text": sanitize(reflow(text))}]
